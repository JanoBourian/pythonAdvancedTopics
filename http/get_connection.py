import http.client 

conn = http.client.HTTPSConnection("flagicons.lipis.dev")
conn.request("GET", "/")
response = conn.getresponse()
print(response.status, response.reason)
conn.close()
