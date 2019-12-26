from datetime import datetime
import csv
import os
import pinboard

def add_to_pinboard(api, bookmark):
    added_at = datetime.fromtimestamp(int(bookmark['Timestamp']))
    title = bookmark['Title'] or input(f"Title for {bookmark['URL']}: ")
    api.posts.add(
        url=bookmark['URL'],
        description=title,
        extended=bookmark['Selection'],
        tags=[f"instapaper-{bookmark['Folder']}"],
        shared=False,
        toread=(bookmark['Folder'] == 'Unread'),
        dt=added_at,
        replace=False
    )

token = os.environ['PINBOARD_API_TOKEN'] or input("Pinboard API token: ")
pb = pinboard.Pinboard(token)

instapaper_csv = input("Path to instapaper-export.csv: ")
with open(instapaper_csv) as csvfile:
    instareader = csv.DictReader(csvfile)
    for row in instareader:
        try:
            add_to_pinboard(pb, row)
        except Exception as ex:
            title = row['Title']
            print(f"Failed to import {title} due to {ex}")
