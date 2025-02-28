from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os
import json

schema = Schema(platform=TEXT(stored=True), content=TEXT)

if not os.path.exists("index"):
    os.mkdir("index")
    ix = create_in("index", schema)
else:
    ix = create_in("index", schema)

with open("cdp_docs.json", "r") as file:
    docs_data = json.load(file)

writer = ix.writer()
for cdp, content in docs_data.items():
    writer.add_document(platform=cdp, content=content)
writer.commit()
