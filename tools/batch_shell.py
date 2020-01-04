# import pydevd
# pydevd.settrace('10.20.204.83', port=10038, stdoutToServer=True, stderrToServer=True)

import os

#test_set = [1, 4, 9, 10, 11, 12, 13, 15, 23, 24, 29, 32, 33, 34, 48, 49, 62, 75, 77, 110, 114, 118]
test_set=[1,4,9,10,11,23]
for i in test_set:
    command="CUDA_VISIBLE_DEVICES=2 python learn_image_filter.py example_data/scenes/scan/pix2pix_denoise_pointmvs_scan"\
            +str(i)+".json --cloud example_data/pointmvs_pointcloud/dtu_wde3/LANCZOS4_3ITER_flow3_ip0.2_fp0.1_d0.12_nc3/scan"\
    +str(i)+"/final3d_model.ply"
    os.system(command)
