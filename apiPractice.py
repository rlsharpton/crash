import requests

resp = requests.head("http://api.open-notify.org/")
print(resp.status_code, resp.text, resp.headers)

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)

response = requests.get("http://api.open-notify.org/iss-pass.json")
print(response.status_code)


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

response = requests.get("http://api.open-notify.org/astros.json")
print(response.headers)


