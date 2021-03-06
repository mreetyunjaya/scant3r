#!/usr/bin/env python3
import re
from core import *
parameters = [
"file=",
"document=",
"folder=",
"root=",
"path=",
"pg=",
"style=",
"pdf=",
"template=",
"php_path=",
"doc=",
"page=",
"name=",
"cat=",
"dir=",
"action=",
"board=",
"date=",
"detail=",
"download=",
"prefix=",
"include=",
"inc=",
"locate=",
"show=",
"site=",
"type=",
"view=",
"content=",
"layout=",
"mod=",
"conf=",
"daemon=",
"upload=",
"dir=",
"download=",
"log=",
"ip=",
"cli=",
"cmd=",
"exec=",
"command=",
"execute=",
"ping=",
"query=",
"jump=",
"code=",
"reg=",
"do=",
"func=",
"arg=",
"option=",
"load=",
"process=",
"step=",
"read=",
"function",
"req=",
"feature=",
"exe=",
"module=",
"payload=",
"run=",
"print=",
"template=",
"preview=",
"id=",
"view=",
"activity=",
"name=",
"content=",
"redirect="
"q=",
"s=",
"search=",
"lang=",
"keyword=",
"query=",
"page=",
"keywords=",
"year=",
"view=",
"email=",
"type=",
"name=",
"p=",
"callback=",
"jsonp=",
"api_key=",
"api=",
"password=",
"email=",
"emailto=",
"token=",
"username=",
"csrf_token=",
"unsubscribe_token=",
"id=",
"item=",
"page_id=",
"month=",
"immagine=",
"list_type=",
"url=",
"terms=",
"categoryid=",
"key=",
"l=",
"begindate=",
"enddate=",
'id=',
'select=',
'report=',
'role=',
'update=',
'query=',
'user=',
'name=',
'sort=',
'where=',
'search=',
'params=',
'process=',
'row=',
'view=',
'table=',
'from=',
'sel=',
'results=',
'sleep=',
'fetch=',
'order=',
'keyword=',
'column=',
'field=',
'delete=',
'string=',
'number=',
'filter='
]


def run(opts):
    for i in opts['url']:
        for par in parameters:
            r = re.search(par,i)
            try:
                if r.group() != None:
                    print(i.replace(r.group(),f'{red}{r.group()}{rest}'))
            except:
                continue
