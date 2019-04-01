import urllib.request 
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?' #where you send a request to
api_key = AIzaSyByTFozs_qCIQ0OMKkgSOIKZ1T8R4HqMIs
origin = input('Where are you?')
destination = input('Where do you want to go?')

nav_request = 'origin={} &destination{} &key={}'.format(origin, destination, api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print directions

