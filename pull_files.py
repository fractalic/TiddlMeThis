import json
import urllib.request

from pprint import pprint

with open("data.json") as open_file:
    data = json.load(open_file)

for blob in data:
    with urllib.request.urlopen(blob['file']) as response:
        doc_file = response.read()
    with open(blob['title']+'.md', 'wb') as doc_out:
        doc_out.write(doc_file)

    with open(blob['title']+'.md.meta', 'w') as doc_meta:
        doc_meta.write("title: " + blob['title'])
        doc_meta.write("\n") # we expect python to convert to os line-ending
        doc_meta.write("tags: " + blob['tags'])

    with open('_importables', 'w') as importables_list:
        importables_list.truncate()
        importables_list.write(blob['title']+'.md'+'\n')


