from django.shortcuts import render
from .models import YoutubeVideoModel
from .utils import *
from .setup import *


def index(request):

    video_list = youtube_query_search(QUERY, MAX_RESULTS)

    for i in range(len(video_list)):

        video = video_list[i]

        video_object = YoutubeVideoModel(i, video[0], video[1], video[2], video[3], video[4])

        if video_object not in list(YoutubeVideoModel.objects.all()):
            video_object.save()

    data = get_json_data(YoutubeVideoModel.objects.all())

    return render(request, 'index.html', {"data": data})

