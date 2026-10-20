#!/usr/bin/env python3
"""Generate and verify native catalogs from reviewed, immutable source pins."""
import argparse
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

def render():
    lock=json.loads((ROOT/'registry/plugins.lock.json').read_text(encoding='utf-8'))
    if lock['formatVersion']!=1:
        raise ValueError('Unsupported registry formatVersion; expected 1')
    entries=lock['plugins']
    names=[p['name'] for p in entries]
    if len(names)!=len(set(names)):
        raise ValueError('Duplicate package IDs in registry')
    if names!=sorted(names):
        raise ValueError('Registry package IDs must be sorted')
    codex=[]
    claude=[]
    for p in entries:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',p['name']):
            raise ValueError(f"Invalid package ID: {p['name']!r}")
        if not re.fullmatch(r'[0-9a-f]{40}',p['sha']):
            raise ValueError(f"{p['name']}: source pin must be a full lowercase commit SHA")
        if p['repository']!=f"Leotus-Richard/{p['name']}":
            raise ValueError(f"{p['name']}: repository does not match the approved owner/package")
        if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+',p['version']):
            raise ValueError(f"{p['name']}: version must use major.minor.patch")
        if p['name'] in {'swe','swe-audit','swe-debt','swe-gain','swe-help','swe-review'}:
            raise ValueError(f"Excluded package: {p['name']}")
        codex.append({'name':p['name'],'source':{'source':'url','url':f"https://github.com/{p['repository']}.git",'sha':p['sha']},'policy':{'installation':'AVAILABLE','authentication':'ON_USE'},'category':'Productivity'})
        claude.append({'name':p['name'],'source':{'source':'github','repo':p['repository'],'sha':p['sha']},'version':p['version'],'description':p['description']})
    return {
      '.agents/plugins/marketplace.json':{'name':'leorichard-library','interface':{'displayName':'LeoRichard Plugin Library'},'plugins':codex},
      '.claude-plugin/marketplace.json':{'name':'leorichard-library','owner':{'name':'Leotus-Richard'},'metadata':{'description':'Independent engineering plugins, each maintained in its own repository.'},'plugins':claude}
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    for relative,value in render().items():
        path=ROOT/relative
        content=json.dumps(value,indent=2)+'\n'
        if args.check:
            if path.read_text(encoding='utf-8')!=content:
                raise ValueError(f'Stale catalog: {relative}')
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8',newline='\n')
    print('Both catalogs match the immutable source registry.')

if __name__=='__main__':
    main()
