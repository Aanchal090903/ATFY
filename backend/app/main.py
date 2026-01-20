from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from app.core.rate_limit import limiter
from app.core.config import settings
from app.routes import tools, usecases, prompts, submit

app = FastAPI(title=settings.PROJECT_NAME)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(tools.router)
app.include_router(usecases.router)
app.include_router(prompts.router)
app.include_router(submit.router)

@app.get("/")
def health():
    return {"status": "ok"}
