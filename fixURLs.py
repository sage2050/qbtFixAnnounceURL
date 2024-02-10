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

qbt_client.torrents_create_tags(tags="trackerless")

for torrent in qbt_client.torrents_info():
    for tracker in torrent.trackers:
        if badURL in tracker.url:
            torrent.add_tags(tags="trackerless")
            torrent.remove_trackers(urls=[tracker.url])
            print(f"Removed {tracker.url} from #{datetime.fromtimestamp(torrent.added_on)}# {torrent.name}")
            

for torrent in qbt_client.torrents_info():
    if  "trackerless" in torrent.tags:
        torrent.add_trackers(urls=goodURL)
        torrent.remove_tags(tags="trackerless")
        print(f"fixed {torrent.name}")
qbt_client.torrents_delete_tags(tags="trackerless")
