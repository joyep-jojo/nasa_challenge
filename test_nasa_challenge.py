import configparser
import yaml
import utils

# Load config variables
file = open('config.yaml', 'r')
cfg = yaml.load(file, Loader=yaml.FullLoader)

config = configparser.ConfigParser()
config.read('config.ini')
host = cfg['host']
nasa_api_key = cfg['nasa_api_key']
topic = cfg['topic']
api_version = cfg['api_version']
landing_date = cfg['landing_date']

api = 'photos'
sol_date = '1000'
amount_images = 10


def test_get_curiosity_photos_martian_sol():
    query_params = '?sol=' + sol_date + '&page=1&api_key=' + nasa_api_key

    nasa_result = utils.get_nasa_rovers_photos(host, topic, api_version, 'curiosity/', api, query_params)

    curiosity_10_photos = nasa_result.json()['photos'][:amount_images]

    photos = []
    for photo in curiosity_10_photos:
        assert photo['img_src'] is not None
        photos.append(photo['img_src'])

    return photos


def test_get_curiosity_images_earth_date():
    earth_date = utils.calculate_earth_time_with_martian_sol(landing_date, sol_date)

    query_params = '?earth_date=' + earth_date + '&page=1&api_key=' + nasa_api_key

    nasa_result = utils.get_nasa_rovers_photos(host, topic, api_version, 'curiosity/', api, query_params)

    curiosity_10_photos = nasa_result.json()['photos'][:amount_images]

    photos = []
    for photo in curiosity_10_photos:
        assert photo['img_src'] is not None
        photos.append(photo['img_src'])

    return photos


def test_get_and_compare_photos_between_earth_date_martian_sol():
    photos_martian_sol = test_get_curiosity_photos_martian_sol()
    photos_earth_date = test_get_curiosity_images_earth_date()

    list_dif = [i for i in photos_martian_sol + photos_earth_date
                if i not in photos_martian_sol or i not in photos_earth_date]

    print("Difference of martian sol date and earth date photos: " + str(list_dif))

    if not list_dif:
        print("Both list photos are equal")
    else:
        print("List photos are NOT equal")

    # if list is not empty throw exception
    assert list_dif is not True


def test_curiosity_camera_photos_greater_than_10_times_other_cameras():
    total_cameras = cfg['cameras']
    total_amount_photos_curiosity = 0
    total_amount_photos_others = 0

    # Iterating through all the cameras
    for camera in total_cameras:
        query_params = '?sol=' + sol_date + '&camera=' + camera + '&api_key=' + nasa_api_key
        nasa_result = utils.get_nasa_rovers_photos(
            host, topic, api_version, 'curiosity/', api, query_params)
        total_amount_photos_curiosity = len(nasa_result.json()['photos']) + total_amount_photos_curiosity

        query_params = '?sol=' + sol_date + '&camera=' + camera + '&api_key=' + nasa_api_key
        nasa_result = utils.get_nasa_rovers_photos(
            host, topic, api_version, "opportunity/", api, query_params)
        total_amount_photos_others = len(nasa_result.json()['photos']) + total_amount_photos_others

        query_params = '?sol=' + sol_date + '&camera=' + camera + '&api_key=' + nasa_api_key
        nasa_result = utils.get_nasa_rovers_photos(
            host, topic, api_version, "spirit/", api, query_params)
        total_amount_photos_others = len(nasa_result.json()['photos']) + total_amount_photos_others

    total_amount_photos_others = total_amount_photos_others * 10

    print('Total amount of curiosity photos: ' + str(total_amount_photos_curiosity))
    print('Total amount of other cameras * 10: ' + str(total_amount_photos_others))

    assert total_amount_photos_curiosity > total_amount_photos_others
