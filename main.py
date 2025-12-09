from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from schemas import URLRequest, URLResponse
from storage import save_url, get_url

app = FastAPI(title="Simple URL Shortener")

BASE_URL = "http://localhost:8000"


@app.post("/shorten", response_model=URLResponse)
def shorten_url(url: URLRequest):
    code = save_url(url.long_url)

    return URLResponse(
        long_url=url.long_url,
        short_url=f"{BASE_URL}/{code}"
    )


@app.get("/{code}")
def redirect_to_url(code: str):
    long_url = get_url(code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(long_url)
