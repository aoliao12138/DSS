# import pydevd
# pydevd.settrace('10.20.204.83', port=10038, stdoutToServer=True, stderrToServer=True)

import json
import os

test_set = [1, 4, 9, 10, 11, 12, 13, 15, 23, 24, 29, 32, 33, 34, 48, 49, 62, 75, 77, 110, 114, 118]

filepath="/root/DSS/example_data/scenes/pix2pix_denoise_pointmvs.json"
# baseDir = os.path.dirname(os.path.realpath(filepath))
# filepath=os.path.join(baseDir,filepath)

def store(data,i):
    filepath="/root/DSS/example_data/scenes/scan/pix2pix_denoise_pointmvs_scan"+str(i)+".json"
    with open(filepath, 'w') as fw:
        json.dump(data,fw)

for i in test_set:
    with open(filepath, "r") as rfile:
        data = json.load(rfile)
        data['cmdLineArgs']['name']+='_scan'+str(i)

        store(data,i)


