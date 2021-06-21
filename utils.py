from datetime import datetime, timedelta

import requests


def calculate_earth_time_with_martian_sol(landing_time, martial_sol):
    mars_date_seconds = int(martial_sol) * 88775
    earth_time_seconds = mars_date_seconds / 86400

    time = int(earth_time_seconds)
    landing_date = datetime.strptime(landing_time, "%Y-%m-%d")
    earth_date = landing_date + timedelta(time)
    formatted_earth_date = str(earth_date.date())

    return formatted_earth_date


def get_nasa_rovers_photos(host, topic, api_version, rover, api, query_params):
    request_url = host + topic + 'api/' + api_version + 'rovers/' + rover + api + query_params
    response = requests.get(request_url)

    assert response.status_code == 200
    return response
