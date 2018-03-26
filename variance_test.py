import glob
import os

exprid = 233
nworkers = 1
fs = []

for i in range(nworkers):
    fs.append(open('variance_test_%d.m' % (i + 1), 'w'))

def run_cmd(cmd):
    print cmd
    os.system(cmd)

lst = glob.glob('/tmp/cv/*')
lst.sort()
for ds in lst:
    exprid += 1

    if os.path.exists('datasets/caltech_expr%d' % exprid):
        run_cmd("rm -r datasets/caltech_expr%d" % exprid)
    if os.path.exists('models/expr%d_caltech' % exprid):
        run_cmd("rm -r models/expr%d_caltech" % exprid)

    cmd = "cp -r datasets/caltech_expr datasets/caltech_expr%d" % exprid
    run_cmd(cmd)

    cmd = "ln -s ../../caltech/train/images_s10k datasets/caltech_expr%d/train/images" % exprid
    run_cmd(cmd)

    cmd = "cp -r %s datasets/caltech_expr%d/train/" % (ds, exprid)
    run_cmd(cmd)
    
    cmd = "cd datasets/caltech_expr%d/train && " % exprid + \
          "python generate_dataset.py %s" % (os.path.basename(ds))
    run_cmd(cmd)

    cmd = "cp -r models/expr00_caltech models/expr%d_caltech" % exprid
    run_cmd(cmd)

    cmd = "sed 's/expr00/expr%d/' < experiments/script_expr00_rpn_caltech.m > experiments/script_expr%d_rpn_caltech.m" % (exprid, exprid)
    run_cmd(cmd)

    cmd = "sed 's/expr00/expr%d/' < experiments/+Dataset/caltech_expr00_trainval.m > experiments/+Dataset/caltech_expr%d_trainval.m" % (exprid, exprid)
    run_cmd(cmd)

    f = fs[exprid % nworkers]
    f.write('script_expr%d_rpn_caltech\n' % exprid)

for i in range(nworkers):
    fs[i].close()
