from fastapi import FastAPI, Request

app = FastAPI(
 title="Catalog movies"
)


@app.get("/")
def read_root(request: Request, name: str = "text",):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello {name}",
        "docs": str(docs_url),
    }

