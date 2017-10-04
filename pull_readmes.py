import json
import urllib.request

from pprint import pprint

with open("data.json") as open_file:
    data = json.load(open_file)

for blob in data:
    with urllib.request.urlopen(blob['file']) as response:
        readme_file = response.read()
    with open(blob['title']+'.md', 'wb') as readme_out:
        readme_out.write(readme_file)

    with open(blob['title']+'.md.meta', 'w') as readme_meta:
        readme_meta.write("title: " + blob['title'])
        readme_meta.write("\n") # we expect python to convert to os line-ending
        readme_meta.write("tags: " + blob['tags'])

