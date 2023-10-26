from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.version1.questions import router as QuestionRouterV1
from server.routes.version1.team_accounts import router as AccountRouterV1
from server.routes.version1.activities import router as ActivityRouterV1
from server.connection.database import init_db
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"], )
async def read_root():
    return {"message": "Server is up and running"}

app.include_router(QuestionRouterV1, tags=["Questions"], prefix="/v1/questions")
app.include_router(AccountRouterV1, tags=["Team Accounts"], prefix="/v1/team_accounts")
app.include_router(ActivityRouterV1, tags=["Activities"], prefix="/v1/activities")