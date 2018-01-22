# -*- coding: utf-8 -*-
import requests

STYRIA_URL = 'https://ds-cloud.styria.hr/categorization/public/api/test/m0/categorize'  # noqa


def call_vision_api(image_filename, api_keys):
    api_key = api_keys['styria']

    # image_filename = os.path.abspath(image_filename)

    response = requests.post(
        headers={"Authorization": api_key},
        params={"verbose": 1},
        files={"image1": open(image_filename, "rb")})

    if response.status_code != 200:
        raise Exception("Error: {}".format(response.text))

    upload_result = response.json()
    return upload_result


def get_standardized_result(api_result):
    categories = api_result["data"]["categories"]
    output = {
        'captions': [(category["name"], None)
                     for category in categories],
    }

    return output
