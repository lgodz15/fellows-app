import requests

api_token = "09797cdc0cd67513285b361466f7bf87"

#this is my github repository
github = "https://github.com/lgodz15/fellows-app.git"

#includes api token and the url to my github repository
data = {'token': api_token , 'github': github}

url = "http://challenge.code2040.org/api/register"

content = requests.post(url, json = data)

print content.content 
