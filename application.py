from TikTokApi import TikTokApi
from flask import Flask, jsonify

import asyncio
import os

application = Flask(__name__)
app = application

ms_token = os.environ.get("ms_token", None)  # set your own ms_token

async def fetch_trending_videos():
    async with TikTokApi() as api:
        await TikTokApi().create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        trending_videos = []
        async for video in TikTokApi().trending.videos(count=10):
            trending_videos.append(video.as_dict)
        return trending_videos
    
@application.route('/')
def hello_world():
    return 'Hello world.'

@application.route('/get_trending')
def get_trending():
    try:
        trending_videos = asyncio.run(fetch_trending_videos())
        return jsonify(trending_videos)
    except Exception as e:
        return jsonify({"error": str(e)})


@application.route('/get_user', methods=['GET'])
def get_user():
    trending_videos = asyncio.run(fetch_trending_videos())
    return jsonify(trending_videos)


