from apiclient.discovery import build
from .setup import *
from operator import itemgetter
import random


def get_datetime(filename):

    file = open(filename, "r+")
    date = file.read()

    if int(date) < 10:
        date = "0" + date

    datetime = "2021-08-" + date + "T00:00:00Z"

    file.close()
    return datetime


def update_datetime(filename):

    file = open(filename, "r+")
    date = file.read()
    file.close()

    date = str(random.randint(1,31))

    file = open(filename, "w+")
    file.write(date)
    file.close()


def youtube_query_search(search_query, max_results):

    youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    datetime = get_datetime(FILENAME)
    update_datetime(FILENAME)

    video_search = youtube_object.search().list(q=search_query, part="id, snippet", maxResults=max_results,
                                                relevanceLanguage='en', type="video", order="date",
                                                publishedAfter=datetime).execute()

    results = video_search.get("items", [])

    video_list = []

    for result in results:

        if result['id']['kind'] == "youtube#video":

            title = result['snippet']['title']
            description = result['snippet']['description']
            thumbnails = result['snippet']['thumbnails']['default']['url']
            video_id = result['id']['videoId']
            published_date = result['snippet']['publishedAt']

            video_list.append([title, description, thumbnails, video_id, published_date])

    return video_list


def get_json_data(video_data):

    data = []

    for video in video_data:

        json = {}

        json['id'] = video.id
        json['video_title'] = video.video_title
        json['description'] = video.description
        json['video_url'] = video.video_url
        json['video_id'] = video.video_id
        json['published_date'] = video.published_date

        data.append(json)


    data = sorted(data, key=itemgetter('published_date'), reverse=True)
    return data










