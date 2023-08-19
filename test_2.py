import urllib.request

url="https://blog.csdn.net/qq_33160790"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')

print(data)