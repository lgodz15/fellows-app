import requests

api_token = "09797cdc0cd67513285b361466f7bf87"
endPoint1 = "http://challenge.code2040.org/api/reverse"
endPoint2 =  "http://challenge.code2040.org/api/reverse/validate"
 

def main():
	token = {"token": api_token}
	content = requests.post(endPoint1, json = token)
	send_word(content.content)

def send_word(word):
	#uses the reverse the word and stores in the variable
	reverseWord = word[::-1]
	data = {"token" : api_token, "string" : reverseWord}
	content = requests.post(endPoint2, json = data)
	print content.content   

    
if __name__  == "__main__":
    main()