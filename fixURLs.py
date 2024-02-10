from datetime import datetime
import qbittorrentapi

badURL="[BROKEN ANNOUNCE URL HERE]"
goodURL="[GOOD ANNOUNCE URL HERE]"

conn_info = dict(
    host="127.0.0.1",
    port=8080,
    username="admin",
    password="adminadmin",
)
qbt_client = qbittorrentapi.Client(**conn_info)
qbt_client.auth_log_in()

for torrent in qbt_client.torrents_info():
    for tracker in torrent.trackers:
        if badURL in tracker.url:
            torrent.remove_trackers(urls=[tracker.url])
            torrent.add_trackers(urls=goodURL)            
            print(f"fixed {torrent.name}")
