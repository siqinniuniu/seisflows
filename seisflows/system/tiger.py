
from seisflows.tools.config import loadclass
from seisflows.tools.config import ParameterError, SeisflowsParameters, SeisflowsPaths

PAR = SeisflowsParameters()
PATH = SeisflowsPaths()

""" For users of tiger.princeton.edu, determines whether
  slurm_sm, slurm_md, or slurm_lg should be used.
"""

# ensure number of processers per forward simulation is defined
if 'NPROC' not in PAR:
    raise Exception

# there are 16 processers per node on tiger
if 'NODESIZE' in PAR:
    assert(PAR.NODESIZE == 16)
else:
    PAR.NODESIZE = 16

# which system interface is appropriate?
if PAR.NPROC > PAR.NODESIZE:
    tiger = loadclass('system','tiger_lg')
elif PAR.NPROC > 1:
    tiger = loadclass('system','tiger_md')
else:
    tiger = loadclass('system','tiger_sm')

