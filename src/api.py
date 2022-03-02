import codecs

from requests import get

from config import Config


def api_download_video(url: str, config: Config):
    video_url = api_get_video_url(url, config)
    resp = get(video_url)
    return resp.content


def api_get_video_url(url: str, config: Config):
    resp = get(
        url,
        headers={
            "user-agent": config.user_agent,
        },
    )
    html = resp.text
    x = html.find("downloadAddr")
    x = html.find("\"", x)
    x = html.find("\"", x + 1)
    x += 1
    y = html.find("\"", x)
    url = html[x:y]
    url = codecs.decode(url, 'unicode-escape')
    return url
