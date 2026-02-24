from fastapi import FastAPI
from routes import Search, watch, User

app = FastAPI(title="AbhiTube Pro")

app.include_router(Search.router, prefix="/api/search")
app.include_router(watch.router, prefix="/api/watch")
app.include_router(User.router, prefix="/api/user")
