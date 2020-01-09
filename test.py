import requests

print (requests.__version__)
google = requests.get("https://www.google.com")
print(google)
var = requests.get("https://raw.githubusercontent.com/XuechunHou/CMPUT404Lab1/master/test.py")
print(var.content)

