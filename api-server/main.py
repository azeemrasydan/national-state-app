from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from src.flood_warning_api import upsert_to_database, perform_flood_warning_get_api
from src.mysql_db import execute_query

app = FastAPI()


@app.get("/flood-warnings")
def get_flood_warnings():
    return execute_query("SELECT * FROM water_station")


@app.get("/flood-warnings/count/group-by/state")
def get_flood_warnings_count_groupby_state():
    return [
        {
            "state": "Selangor",
            "count": 20
        }
    ]


@app.on_event("startup")
@repeat_every(seconds=30)  # CRON job runs every hour, adjust as needed
def scheduled_flood_warning_get_api():
    data = perform_flood_warning_get_api()
    upsert_to_database(data)
