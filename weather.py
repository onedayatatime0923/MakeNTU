import urllib.request
import json

zip = input("Where do you live ? ")

API_key = "a9029960ce39fbbd"
url = 'http://api.wunderground.com/api/' + API_key + '/geolookup/conditions/q/PA/' + zip + '.json'
f = urllib.request.urlopen(url)
json_srt = f.read()
parse_json = json.loads(json_srt) 
#print(parse_json)
temperature = parse_json['current_observation']['temp_f']
print("temperature: {}".format((temperature-32)*5/9))