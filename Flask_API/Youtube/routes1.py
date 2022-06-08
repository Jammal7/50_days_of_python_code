import requests

from jmespath import search
from isodate import parse_duration
from flask import Blueprint, render_template, current_app, request, redirect

main=Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    channel_url = 'https://www.googleapis.com/youtube/v3/channels'

    all_data = []

    if request.method == 'POST':
        id_params = {
            'key': current_app.config['YOUTUBE_API_KEY'],
            'q' : request.form.get('query'),
            'part': 'snippet',
            'type': 'channel'
        }
        r = requests.get(search_url, params=id_params)
        results = r.json()['items']
        channel_ids = []
        for result in results:
            channel_ids.append(result['id']['channelId'])

        Channel_params = {
            'key': current_app.config['YOUTUBE_API_KEY'],
            'id' : ','.join(channel_ids),
            'part': 'snippet, contentDetails, statistics',
        }
        r = requests.get(channel_url, params=Channel_params)
        results = r.json()['items'] 
        for result in results:
            channel_data = {
                'Channel_name' : result['snippet']['title'],
                'Subscribers' : result['statistics']['subscriberCount'],
                'Views' : result['statistics']['viewCount'],
                'Total_videos' : result['statistics']['videoCount'],
                'playlist_id' : result['contentDetails']['relatedPlaylists']['uploads']
            }
            all_data.append(channel_data)

    return render_template('index1.html', videos=all_data)