import requests
import time

print("Start and wait 120 sec")
time.sleep(120)
r =requests.get('https://api.ipify.org?format=json')
print(r.text)
print("End")