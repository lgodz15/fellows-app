import requests

api_token = "09797cdc0cd67513285b361466f7bf87"
endPoint1 = "http://challenge.code2040.org/api/haystack"
endPoint2 =  "http://challenge.code2040.org/api/haystack/validate"

def haystack_needle(jsonData):
	haystack = jsonData['haystack']
	needle = jsonData['needle']
	index = 0
	count = 0
	for item in haystack:
		if needle == item:
			index = count
		else:
			count = count + 1
	return index

def send_needle(jsonData):
	index = haystack_needle(jsonData)
	data = {"token" : api_token, "needle" : index}
	content = requests.post(endPoint2, json = data)
	print content.content   

def main():
	token = {"token": api_token}
	content = requests.post(endPoint1, json = token)
	jsonData = content.json()
	send_needle(jsonData)

    
if __name__  == "__main__":
    main()