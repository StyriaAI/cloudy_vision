# -*- coding: utf-8 -*-
import requests
from io import BytesIO

from PIL import Image

STYRIA_URL = 'https://ds-cloud.styria.hr/categorization/api/general/categorize'  # noqa


def _load_and_resize_image(image_path, out_longer_side=256):
    out_img = BytesIO()
    image = Image.open(image_path)
    image.thumbnail((out_longer_side, out_longer_side))
    image.save(out_img, format="JPEG", quality=70)
    return out_img.getvalue()


def call_vision_api(image_filename, api_keys):
    api_key = api_keys['styria']

    # image_filename = os.path.abspath(image_filename)

    response = requests.post(
        STYRIA_URL,
        headers={"Authorization": api_key},
        params={"verbose": 1},
        files={"image1": _load_and_resize_image(image_filename)})

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
