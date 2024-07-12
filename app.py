from config.config import Settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi_versioning import VersionedFastAPI
from fastapi import FastAPI


app = FastAPI(
    title=Settings().APP_NAME,
    version=Settings().APP_VERSION,
    description=Settings().APP_DESCRIPTION,
)


app = VersionedFastAPI(app, enable_latest=True, version_format='{major}',
    prefix_format='/v{major}')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


@app.get('/')
def index():
    return {
        "toninote": {
            "version": Settings().APP_VERSION,
            "description": Settings().APP_DESCRIPTION
        }
    }


@app.get("/healthcheck")
def api_healthcheck():
    return "OK 200 - app running successfully"


