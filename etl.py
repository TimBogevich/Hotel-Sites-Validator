#!/usr/bin/python3.5


from jsonschema import validate
import csv
import json
import urllib3
from multiprocessing.dummy import Pool as ThreadPool


#Define global variables
pool = ThreadPool(260)
schema = json.load(open("validation.json"))
input_file = open("hotels.csv","r")
out_valid_json = open("out_valid_hotels.json","w",-1)
out_invalid_json = open("out_invalid_hotels.json","w")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def iterator(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	results = pool.map(writer, reader)
	pool.close()
	pool.join()




def validator(json_obj):
	try:
		validate(json_obj,schema)
		uri = json_obj["uri"]
		print("DEBUG INFO: Checking url:   " + uri)
		urllib3.PoolManager().request('GET', uri, timeout=urllib3.Timeout(connect=2.0, read=2.0), retries=False).status
		a = True
	except:
		a = False
	return a


def writer(line_obj):
	line_obj["stars"] = int(line_obj["stars"])
	if validator(line_obj):
		json.dump(line_obj, out_valid_json, ensure_ascii=False, indent=4, sort_keys=True)
	else:
		json.dump(line_obj, out_invalid_json, ensure_ascii=False, indent=4, sort_keys=True)

if __name__ == "__main__":
	iterator(input_file)
