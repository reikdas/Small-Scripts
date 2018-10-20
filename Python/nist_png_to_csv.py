import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import time

class_info = {}
for i in range(48, 58):
    class_info[i] = hex(i)[2:]
for i in range(65, 65+26):
    class_info[i] = hex(i)[2:]
for i in range(97, 97+26):
    class_info[i] = hex(i)[2:]

start = time.time()
data_list = []
total_count = 0

for i in class_info:
    print(i, '\t', time.time()-start, 'seconds', end='\t')
    path = 'nist_by_class/' + class_info[i] + '/train_' + class_info[i]
    count = 0
    for img in os.listdir(path):
        im = Image.open(path + '/' + img).convert('L').crop((32, 32, 96, 96))
        im_arr = np.array(im, dtype='uint8')
        flat_im_arr = im_arr.flatten()
        flat_im_arr_labelled = np.insert(flat_im_arr, 0, i)
        data_list.append(flat_im_arr_labelled)
        count += 1
    print(count, 'samples')
    total_count += count

data = np.array(data_list, dtype='uint8')
print('Total number of samples =', total_count)
print('Shape of final data =', data.shape)
print('Writing data to file...', time.time()-start, 'seconds')
np.savetxt('nist_byclass_full.csv', data, delimiter=',', fmt='%u')
print('Data written to file...', time.time()-start, 'seconds')
