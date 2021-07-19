from django.shortcuts import render
from django.contrib import messages
from googleapiclient.discovery import build
import re
from datetime import timedelta

def playtime(request):
    return render(request, 'youtube/playtime.html')

def result(request, playlist_link):
    playlist_link = request.POST['srh']
    index = playlist_link.rfind('=')
    if index == -1:
        playlist_link = None
        messages.error(request, "This Link is not Valid!")
        return render(request, 'youtube/playtime.html', {'playlist_link':playlist_link})
    else:
        playlist_link = playlist_link[index+1:]
        api_key = 'AIzaSyB7-6f_OcP1_QtzRZO7zC1UOs5hN5FOI8A'
        playlist = playlist_link
        try:
            youtube = build('youtube', 'v3', developerKey=api_key)
            hours_pattern = re.compile(r'(\d+)H')
            minutes_pattern = re.compile(r'(\d+)M')
            seconds_pattern = re.compile(r'(\d+)S')
            total_seconds = 0
            nextPageToken = None
            while True:
                pl_request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist,
                    maxResults=50,
                    pageToken=nextPageToken,
                )

                response = pl_request.execute()

                vid_ids = []
                for item in response['items']:
                    vid_ids.append(item['contentDetails']['videoId'])

                vid_request = youtube.videos().list(
                    part='contentDetails',
                    id=','.join(vid_ids)
                )
                vid_response = vid_request.execute()

                

                for item in vid_response['items']:
                    duration = item['contentDetails']['duration']
                    hours = hours_pattern.search(duration)
                    minutes = minutes_pattern.search(duration)
                    seconds = seconds_pattern.search(duration)

                    hours = int(hours.group(1)) if hours else 0
                    minutes = int(minutes.group(1)) if minutes else 0
                    seconds = int(seconds.group(1)) if seconds else 0
                    video_seconds = timedelta(
                        hours = hours,
                        minutes = minutes,
                        seconds = seconds
                    ).total_seconds()
                    total_seconds += video_seconds

                nextPageToken = response.get('nextPageToken')
                if not nextPageToken:
                    break

            total_seconds = int(total_seconds)
            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            playlist_link = {'hours':hours, 'minutes':minutes, 'seconds':seconds}
        except:
            playlist_link = None
        if playlist_link == None:
            messages.error(request, "This Link is not Valid!")

    return render(request, 'youtube/playtime.html', {'playlist_link':playlist_link})

