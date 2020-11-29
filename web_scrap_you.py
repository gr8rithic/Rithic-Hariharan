import requests
url = "https://www.youtube.com/"

res = requests.get(url)

response = res.text

#print(response)

for i in response:
	if i == "search-querry":
		print("gotcha")
	else:
		continue