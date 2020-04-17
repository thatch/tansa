# Name for JSON
A filter to get the json file content, type a file name in regular expression. 

## Quick Start
The simple installation
	pip setup.py install

## Sample
	import tansa

	file_list = tansa.FileFinder("sample")
	# list of file path starts from sample

	tansa.JReader().json_dispenser(file_list)
	# list of json file contents