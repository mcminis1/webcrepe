from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import os
# from bs4 import BeautifulSoup

from googleapiclient.discovery import build
import urllib.parse

developer_key = os.getenv('GCP_DEVELOPER_KEY')
search_engine_id = os.getenv('GCP_SEARCH_ENGINE_ID')

search_service = build("customsearch", "v1", developerKey=developer_key)

  
app = FastAPI()

class SearchResult(BaseModel):
    title: str
    link: str
    snippet: str

# class Entity(BaseModel):
#     label: str
#     text: str


# class PageResult(BaseModel):
#     text: str
#     entities: [Entity]


@app.get("/search")
def read_item(q: str)-> List[SearchResult]:
    parsed_qry =  urllib.parse.unquote_plus(q)

    qry = search_service.cse().list(
        q=parsed_qry,
        cx=search_engine_id,
    )
    res = qry.execute()
    rv = []
    for item in res['items']:
        if item['kind'] == 'customsearch#result':
            sr = SearchResult(title=item['title'], snippet=item['snippet'], link=item['link'])
            rv.append(sr)
    return rv

# @app.get("/page")
# def read_item(p: str)-> PageResult:
#     r = requests.get(p)
#     print(r.text())
#     soup = BeautifulSoup(r.content, 'html5lib')

