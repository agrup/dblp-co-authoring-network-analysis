
import json
# conn = http.client.HTTPSConnection("ai.google")

# payload = ""

# conn.request("GET", "/static/data/authors.json", payload)

# res = conn.getresponse()
# data = res.read()



# json_obj = json.loads(data)

# print(json_obj)
import requests

url = "https://ai.google/static/data/authors.json"

payload = ""
response = requests.request("GET", url, data=payload)

content =response.content
jsoncontent = json.loads(response.content)

print(json.loads(content))

# with open('goole.json', 'wb') as f:
#     f.write(response.content)


# Retrieve HTTP meta-data
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)