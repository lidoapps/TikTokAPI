from TikTokApi import TikTokApi
from flask import Flask, jsonify

import asyncio
import os

app = Flask(__name__)

ms_token = os.environ.get("ms_token", None)  # set your own ms_token

async def fetch_trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        trending_videos = []
        async for video in api.trending.videos(count=10):
            trending_videos.append(video.as_dict)
        return trending_videos

@app.route('/get_trending', methods=['GET'])
def get_trending():
    trending_videos = asyncio.run(fetch_trending_videos())
    return jsonify(trending_videos)


@app.route('/get_user', methods=['GET'])
def get_user():
    trending_videos = asyncio.run(fetch_trending_videos())
    return jsonify(trending_videos)

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5000)

