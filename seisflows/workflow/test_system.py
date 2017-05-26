
import sys
import time

from seisflows.config import ParameterError

PAR = sys.modules['seisflows_parameters']
PATH = sys.modules['seisflows_paths']

system = sys.modules['seisflows_system']


class test_system:
    """ Tests system interface
    """

    def check(self):
        if 'NTASK' not in PAR:
            raise Exception

        if 'NPROC' not in PAR:
            setattr(PAR,'NPROC',1)

        if 'VERBOSE' not in PAR:
            setattr(PAR,'VERBOSE',0)


    def main(self):
        system.run('workflow', 'hello',  
            hosts='head', 
            msg='Hello from 0')

        system.run('workflow', 'hello', 
            hosts='all',
            msg='Hello from %d')

        print ''


    def hello(self, msg='Hello from %d'):
        """ Prints hello message
        """
        time.sleep(1)
        try:
            print msg % system.taskid()+1 
        except:
            print msg

        print ''

