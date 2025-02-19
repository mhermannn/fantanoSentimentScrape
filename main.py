from organizer import organizer
import os

albums = [
    {
        "title": "BRAT",
        "author": "Charli XCX",
        "rating": "10/10",
        "vidId": "bLJ-zfBmChA"
    },
    {
        "title": "Vultures 1",
        "author": "Kanye West & Ty Dolla $ign",
        "rating": "unreviewable",
        "vidId": "M0jEngxUFz4"
    },
    {
        "title": "Preacher's Daughter",
        "author": "Ethel Cain",
        "rating": "6/10",
        "vidId": "oyLkPLnoDlo"
    },
    {
        "title": "To Pimp A Butterfly",
        "author": "Kendrick Lamar",
        "rating": "10/10",
        "vidId": "qTmHuavOXNg"
    },
    {
        "title": "Speedin' Bullet 2 Heaven",
        "author": "Kid Cudi",
        "rating": "0.94721/10",
        "vidId": "CJDcbwpsjU0"
    },
    # {
    #     "title": "Loveless",
    #     "author": "My Bloody Valentine",
    #     "rating": "classic",
    #     "vidId": "iG_0Exs9jTQ"
    # },
    # {
    #     "title": "Angelic 2 The Core",
    #     "author": "Corey Feldman",
    #     "rating": "NOT GOOD",
    #     "vidId": "L3E0kq9YkjA"
    # },
    # {
    #     "title": "My Beautiful Dark Twisted Fantasy",
    #     "author": "Kanye West",
    #     "rating": "6/10",
    #     "vidId": "Jo4S2qlQGs0"
    # },
    # {
    #     "title": "REDUX My Beautiful Dark Twisted Fantasy",
    #     "author": "Kanye West",
    #     "rating": "6/10",
    #     "vidId": "rNaT3KazKoE"
    # },
    # {
    #     "title": "Swimming",
    #     "author": "Mac Miller",
    #     "rating": "3/10",
    #     "vidId": "UgwPxFUUg94"
    # },
    # {
    #     "title": "REDUX Swimming",
    #     "author": "Mac Miller",
    #     "rating": "8/10",
    #     "vidId": "Cg3HTairH5g"
    # },
    # {
    #     "title": "Hypochondriac",
    #     "author": "brakence",
    #     "rating": "5/10",
    #     "vidId": "iirPux8sPGA"
    # },
    # {
    #     "title": "Certified Lover Boy",
    #     "author": "Drake",
    #     "rating": "3/10",
    #     "vidId": "k6ppxsRfZMA"
    # },
    # {
    #     "title": "Circles",
    #     "author": "Mac Miller",
    #     "rating": "8/10",
    #     "vidId": "7ndtSyn6dVg"
    # },
    # {
    #     "title": "Nurture",
    #     "author": "Porter Robinson",
    #     "rating": "8/10",
    #     "vidId": "NKtqB-SFIaw"
    # },
    # {
    #     "title": "LP!",
    #     "author": "JPEGMAFIA",
    #     "rating": "9/10",
    #     "vidId": "bbsD3mRmQn4"
    # },
    # {
    #     "title": "Scaring the Hoes",
    #     "author": "JPEGMAFIA & Danny Brown",
    #     "rating": "9/10",
    #     "vidId": "bh3b0684RuU"
    # },
    # {
    #     "title": "Untrue",
    #     "author": "BURIAL",
    #     "rating": "classic",
    #     "vidId": "3d1rxJTIJX8"
    # },
    # {
    #     "title": "Saturation",
    #     "author": "BROCKHAMPTON",
    #     "rating": "9/10",
    #     "vidId": "iBHjkRZQbv8"
    # },
    # {
    #     "title": "Hood Hottest Princess (Deluxe)",
    #     "author": "Sexyy Red",
    #     "rating": "8/10",
    #     "vidId": "fN1d3HWOd54"
    # },
    # {
    #     "title": "Arular",
    #     "author": "M.I.A",
    #     "rating": "classic",
    #     "vidId": "0o18WjNo6tA"
    # }
]

if not os.path.exists("albums"):
    os.makedirs("albums")

for al in albums:
    organizer(al["vidId"],al["title"])
