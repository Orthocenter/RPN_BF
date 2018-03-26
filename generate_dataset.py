import os
import glob
import shutil
import sys

num = 10000
noisy_annot = sys.argv[1]

skip = 40000 / num
annots = glob.glob(noisy_annot + '/*.txt')
annots.sort()

sannot_path = 'annotations'

if os.path.exists(sannot_path):
    print 'remove dir', sannot_path
    shutil.rmtree(sannot_path)
os.makedirs(sannot_path)

cnt = 0
for j in xrange(len(annots)):
    if j % skip == 0:
        cnt += 1

        cmd = 'cp ' + annots[j] + ' ' + sannot_path
        os.system(cmd)

        if cnt >= num:
            break

