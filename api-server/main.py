from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from src.flood_warning_api import insert_to_database, perform_flood_warning_get_api

app = FastAPI()


@app.get("/flood-warnings")
def get_flood_warnings():
    return [
        {
            "station_id": "3533102_CPKN0003",
            "station_name": "Sg. Pahang Tua di Rumah Pam Pahang Tua",
            "latitude": 3.55966,
            "longitude": 103.354,
            "district": "Pekan",
            "state": "PAHANG",
            "sub_basin": "Sg. Pahang Tua",
            "main_basin": "Sungai Pahang",
            "station_type": "RF,WL",
            "water_level_current": 9.1,
            "water_level_indicator": "DANGER",
            "water_level_normal_level": 5.5,
            "water_level_alert_level": 7,
            "water_level_warning_level": 9,
            "water_level_danger_level": 9,
            "water_level_increment": 0.1,
            "water_level_update_datetime": "2024-01-28 22:00:00",
            "water_level_update_date": "2024-01-28",
            "water_level_trend": "RISING",
            "rainfall_clean": 0,
            "rainfall_latest_1hr": 0,
            "rainfall_total_today": 0,
            "rainfall_indicator": "NO_RAINFALL",
            "rainfall_update_datetime": "2024-01-28 22:00:00",
            "rainfall_update_date": "2024-01-28",
            "water_level_display": "1",
            "rainfall_display": "0",
            "raw_water_level": 9.1,
            "raw_rainfall": 0,
            "station_status": "ON",
            "station_code": "RPPAHANGTUA",
            "water_level_status": "ON",
            "rainfall_status": "ON",
        }
    ]



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
    insert_to_database(data)
