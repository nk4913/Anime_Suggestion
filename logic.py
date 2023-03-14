
import requests

def search_anime(name):


    url = "https://anime-db.p.rapidapi.com/anime"

    querystring = {"page":"1","size":"10","search":name,"genres":"Fantasy,Drama","sortBy":"ranking","sortOrder":"asc"}

    headers = {
        "X-RapidAPI-Key": "ac4b2b67e6msh85f2775b307ee58p1b5147jsnc4fe82aec600",
        "X-RapidAPI-Host": "anime-db.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    title = []
    gener = []
    image = []
    for x in data.values():
        for y in x:
            try :
                # print(y)
                title.append(y["title"])
                gener.append(y["genres"])
                image.append(y["image"])
                
            except Exception as e:
                pass

    return title , gener , image
    



