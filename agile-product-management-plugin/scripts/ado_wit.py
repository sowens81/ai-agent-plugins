#!/usr/bin/env python3
"""Minimal Azure DevOps WIT REST helper; approval is enforced by the calling agent."""
import argparse, base64, json, os, subprocess, sys, urllib.request, urllib.error, urllib.parse
RESOURCE='499b84ac-1321-427f-aa17-267ca6975798'
def auth():
    pat=os.environ.get('AZURE_DEVOPS_PAT')
    if pat: return 'Basic '+base64.b64encode((':'+pat).encode()).decode()
    try:
        p=subprocess.run(['az','account','get-access-token','--resource',RESOURCE,'--query','accessToken','-o','tsv'],capture_output=True,text=True,check=True)
        token=p.stdout.strip()
        if token:return 'Bearer '+token
    except (FileNotFoundError,subprocess.CalledProcessError):pass
    raise RuntimeError('Authenticate with az login or set AZURE_DEVOPS_PAT')
def request(method,url,body=None):
    data=None if body is None else json.dumps(body).encode()
    req=urllib.request.Request(url,data=data,method=method,headers={'Authorization':auth(),'Accept':'application/json','Content-Type':'application/json-patch+json' if isinstance(body,list) else 'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=30) as resp:
            raw=resp.read();return json.loads(raw) if raw else {'status':resp.status}
    except urllib.error.HTTPError as e:
        detail=e.read().decode(errors='replace')[:1200]
        raise RuntimeError(f'ADO HTTP {e.code}: {detail}') from None
def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['auth-check','get','create','update','delete','link']);p.add_argument('id',nargs='?');p.add_argument('other_id',nargs='?');p.add_argument('relation',nargs='?',choices=['parent','child','predecessor','successor']);p.add_argument('--json');p.add_argument('--rev',type=int);p.add_argument('--confirm-id');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
    if a.action=='auth-check':auth();print('Authentication available');return
    org=os.getenv('ADO_ORG_URL','').rstrip('/');project=os.getenv('ADO_PROJECT','')
    if not org or not project:raise RuntimeError('Set ADO_ORG_URL and ADO_PROJECT')
    base=f'{org}/{urllib.parse.quote(project,safe="")}/_apis/wit/workitems'
    suffix='?api-version=7.1'
    if a.action=='get':
        if not a.id:raise RuntimeError('Provide work item ID')
        print(json.dumps(request('GET',base+'/'+a.id+'?$expand=all&api-version=7.1'),indent=2));return
    if a.action=='delete':
        if not a.id or a.confirm_id!=a.id:raise RuntimeError('Deletion requires --confirm-id matching item ID, AFTER explicit consumer approval')
        url=base+'/'+a.id+suffix;ops=None;method='DELETE'
    elif a.action=='link':
        if not (a.id and a.other_id and a.relation and a.rev is not None):raise RuntimeError('link needs ID, other ID, relation, --rev')
        refs={'parent':'System.LinkTypes.Hierarchy-Reverse','child':'System.LinkTypes.Hierarchy-Forward','predecessor':'System.LinkTypes.Dependency-Reverse','successor':'System.LinkTypes.Dependency-Forward'}
        if a.id==a.other_id:raise RuntimeError('Cannot self-link')
        other=f'{org}/_apis/wit/workItems/{a.other_id}'
        ops=[{'op':'test','path':'/rev','value':a.rev},{'op':'add','path':'/relations/-','value':{'rel':refs[a.relation],'url':other}}];url=base+'/'+a.id+suffix;method='PATCH'
    else:
        if not a.json:raise RuntimeError('Provide --json payload path')
        obj=json.load(open(a.json,encoding='utf-8'))
        ops=[]
        if a.action=='update':
            if not a.id or a.rev is None:raise RuntimeError('update requires ID and --rev')
            ops.append({'op':'test','path':'/rev','value':a.rev})
        for k,v in obj.get('fields',{}).items():ops.append({'op':'add','path':'/fields/'+k,'value':v})
        for k,v in obj.get('markdown_fields',{}).items():
            if not isinstance(v,str):raise RuntimeError('Markdown field must be a string')
            ops.append({'op':'add','path':'/fields/'+k,'value':v})
            ops.append({'op':'add','path':'/multilineFieldsFormat/'+k,'value':'Markdown'})
        for rel in obj.get('relations',[]):ops.append({'op':'add','path':'/relations/-','value':rel})
        if a.action=='create':
            if not a.id:raise RuntimeError('create requires work item type, e.g. "User Story"')
            url=base+'/$'+urllib.parse.quote(a.id,safe='')+suffix;method='POST'
        else:url=base+'/'+a.id+suffix;method='PATCH'
    if a.dry_run:
        print(json.dumps({'method':method,'url':url,'operations':ops},indent=2));return
    result=request(method,url,ops)
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    try:main()
    except (RuntimeError,ValueError,FileNotFoundError) as e:print(f'Error: {e}',file=sys.stderr);sys.exit(1)
