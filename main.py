from organizer import organizer
import os
albums = [
    {
        "title": "BRAT",
        "author": "Charli XCX",
        "rating": 10,
        "vidId": "bLJ-zfBmChA"
    },
    {
        "title": "Loveless",
        "author": "My Bloody Valentine",
        "rating": "classic",
        "vidId": "iG_0Exs9jTQ"
    }
]

if not os.path.exists("albums"):
    os.makedirs("albums")

for al in albums:
    organizer(al["vidId"],al["title"])
