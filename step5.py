import requests
import datetime
import dateutil.parser

api_token = "09797cdc0cd67513285b361466f7bf87"
endPoint1 = "http://challenge.code2040.org/api/dating"
endPoint2 = "http://challenge.code2040.org/api/dating/validate"


def time(time):
	data = {"token" : api_token, "datestamp" :time}
	content = requests.post(endPoint2, json = data)
	print content.content   


def main():
	token = {"token": api_token}
	content = requests.post(endPoint1, json = token)
	jsonData = content.json()

	datestamp = jsonData['datestamp']
	interval =  jsonData['interval']

	current = dateutil.parser.parse(datestamp, ignoretz = True)
	changeDate = current + datetime.timedelta(hours = 0,seconds = interval)
	laterDate = changeDate.isoformat() + 'Z'
	time(laterDate)

    
if __name__  == "__main__":
    main()