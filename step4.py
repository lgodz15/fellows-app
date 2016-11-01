import requests

api_token = "09797cdc0cd67513285b361466f7bf87"
endPoint1 = "http://challenge.code2040.org/api/prefix"
endPoint2 =  "http://challenge.code2040.org/api/prefix/validate"

def main():
	token = {"token": api_token}
	content = requests.post(endPoint1, json = token)
	jsonData = content.json()
	send_prefix(jsonData)

def prefix(jsonData):
	strings = jsonData['array']
	prefix = jsonData['prefix']
	array = []
	for item in strings:
		if prefix  not in item:
			array.append(item)
	return array

def send_prefix(jsonData):
	array = prefix(jsonData)
	data = {"token" : api_token, "array" : array}
	content = requests.post(endPoint2, json = data)   
	print content.content
    
if __name__  == "__main__":
    main()