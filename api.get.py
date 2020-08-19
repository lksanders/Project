import requests
import json

url = 'https://nctc.beta.instructure.com443/api/v1/courses/1535/students'
headers = {'Authorization' : 'Bearer 1159~90NSnmXM8ixrCyCawxx3twJlZO3rzqtXl7YmkyD9Od83JWTsbFfXvsksnbUIUEgE'}

r = requests.get(url,headers = headers)

print(r.status_code)
print(r.text)
print(r.json)