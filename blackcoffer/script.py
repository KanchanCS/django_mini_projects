# load the json data from the json file and store into
import datetime as dt
import json

from dashboard.models import IndustrySummary


def str_to_datetime(strdate):
    datetime_obj = None
    if strdate:
        format = "%B, %d %Y %H:%M:%S"
        datetime_obj = dt.datetime.strptime(strdate, format)
    return datetime_obj


def str_year_to_date(stryear):
    date = None
    if stryear:
        date_str = f"01-01-{stryear}" 
        date = dt.datetime.strptime(date_str, "%d-%m-%Y").date()
    return date


def load_data(filename):
    with open(filename) as file:
        json_data = json.load(file)
    return json_data


def script_load_data():
    file_name = "jsondata.json"
    objects = load_data(file_name)
    for obj in objects:
        summary = IndustrySummary.objects.create(
            topic=obj["topic"],
            region=obj["region"],
            sector=obj["sector"],
            country=obj["country"],
            pestle=obj["pestle"],
            sources=obj["source"],
            impact=obj["impact"],
            insight=obj["insight"],
            title=obj["title"],
            url=obj["url"],
            likelihood=obj["likelihood"] if obj["likelihood"] else None,
            relevance=obj["relevance"] if obj["relevance"] else None,
            intensity=obj["intensity"] if obj["intensity"] else None,
            start_year=str_year_to_date(obj["start_year"]),
            end_year=str_year_to_date(obj["end_year"]),
            add_date=str_to_datetime(obj["added"]),
            publish_date=str_to_datetime(obj["published"]),
        )
        summary.save()
    return "done"
