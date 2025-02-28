from fastapi import FastAPI
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

app = FastAPI()
ix = open_dir("index")

@app.get("/ask")
def ask_question(query: str):
    with ix.searcher() as searcher:
        query_parser = QueryParser("content", ix.schema)
        q = query_parser.parse(query)
        results = searcher.search(q, limit=3)

        if not results:
            return {"response": "No relevant documentation found."}

        response = [{"platform": r["platform"], "content": r["content"][:300]} for r in results]
        return {"response": response}

# Run API: uvicorn chatbot_api:app --reload
