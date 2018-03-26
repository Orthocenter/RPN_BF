import glob
import os

_exprid = 260

def run_cmd(cmd):
    print cmd
    os.system(cmd)

for exprid in range(_exprid , _exprid + 4):
    cmd = "sed 's/expr00/expr%d/' < experiments/script_expr00_rpn_caltech.m > experiments/script_expr%d_rpn_caltech.m" % (exprid, exprid)
    run_cmd(cmd)

    cmd = "sed 's/expr00/expr%d/' < experiments/+Dataset/caltech_expr00_trainval.m > experiments/+Dataset/caltech_expr%d_trainval.m" % (exprid, exprid)
    run_cmd(cmd)
