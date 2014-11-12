"""
Zips up all the bundles and adds them to `index.json`.
"""

import zipfile, json, os

index = []
for filename in os.listdir('.'):
	name, ext = os.path.splitext(filename)
	if ext == '.bundle':
		zipped = zipfile.ZipFile(name + ".zip", "w")
		for (dir, dirs, files) in os.walk(filename):
			for f in files:
				zipped.write(os.path.join(dir, f), os.path.join(dir, f))
		zipped.close()
		info = json.load(open(os.path.join(filename, 'info.json')))
		info['zip_url'] = name + ".zip"
		index.append(info)
comment = "This index is automatically generated by generate_index.py"
json.dump({"plugins": index, "comment": comment}, open("index.json", "w"), sort_keys=True, indent=4, separators=(',', ': '))
