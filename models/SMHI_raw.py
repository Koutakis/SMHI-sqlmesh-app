from sqlmesh import model
from sqlmesh.core.model.kind import ModelKindName
from sqlmesh import ExecutionContext
import pandas as pd
import typing as t
from datetime import datetime
import requests

@model(
    "smhi.weather_warnings",
    kind=dict(name=ModelKindName.FULL),
    columns={
        "warning_id": "int",
        "event_code": "text",
        "event_en": "text",
        "mho_code": "text",
        "area_id": "int",
        "area_name": "text",
        "warning_level": "text",
        "event_description": "text",
        "approximate_start": "datetime",
        "published": "datetime",
        "created": "datetime"
    }
)
def execute(
    context: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
) -> pd.DataFrame:

    # Fetch SMHI warning data
    url = "https://opendata-download-warnings.smhi.se/ibww/api/version/1/warning.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    rows = []

    # Each warning in the list
    for warning in data:
        event = warning.get("event", {})
        event_code = event.get("code")
        event_en = event.get("en")
        mho_code = event.get("mhoClassification", {}).get("code")

        for area in warning.get("warningAreas", []):
            row = {
                "warning_id": warning.get("id"),
                "event_code": event_code,
                "event_en": event_en,
                "mho_code": mho_code,
                "area_id": area.get("id"),
                "area_name": area.get("areaName", {}).get("sv"),
                "warning_level": area.get("warningLevel", {}).get("en"),
                "event_description": area.get("eventDescription", {}).get("en"),
                "approximate_start": area.get("approximateStart"),
                "published": area.get("published"),
                "created": area.get("created")
            }
            rows.append(row)

    df = pd.DataFrame(rows)

    # Convert datetimes
    for col in ["approximate_start", "published", "created"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    print(df.head())
    return df
