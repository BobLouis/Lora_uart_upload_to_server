import http.client

conn = http.client.HTTPConnection("140.116.245.242:7165")

payload = "{\"name\":\"CK06\",\"lifeExpectancy\":4,\"type\":\"sporting\",\"origin\":\"Taiwan\"}\n\t"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "9f74b04f-dcdc-e793-5dcb-58015ab957e9"
}

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
