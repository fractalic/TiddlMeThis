import json
import urllib.request
import os

from pprint import pprint

with open("file_props.json") as open_file:
    data = json.load(open_file)

group_dir = 'importables'
try:
    os.mkdir('./importables')
except FileExistsError:
    print("importables exists")

os.chdir('./importables')

with open('_importables', 'w') as importables_list:
        importables_list.truncate()

for blob in data:
    with urllib.request.urlopen(blob['file']) as response:
        doc_file = response.read()
    with open(blob['meta']['title']+'.md', 'wb') as doc_out:
        doc_out.write(doc_file)

    with open(blob['meta']['title']+'.md.meta', 'w') as doc_meta:
        for prop in blob['meta']:
            doc_meta.write(prop + ': ' + blob['meta'][prop])
            doc_meta.write("\n") # we expect python to convert to os line-ending

    with open('_importables', 'w') as importables_list:
        importables_list.write(group_dir + '/' + blob['meta']['title']+'.md'+'\n')


