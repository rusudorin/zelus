from deploy import *
from multiprocessing import Process

def stormtrooper(lots_of_args):
    p = Process(target=deploy_stormtrooper, args=lots_of_args)
    p.start()

   stormtrooper(('root', '10.141.0.151', 'mongodb', 'worker2', 4, 'worker2'))
   stormtrooper(('root', '10.141.0.152', 'mongodb', 'worker3', 4, 'worker3'))
   stormtrooper(('root', '10.141.0.153', 'mongodb', 'worker4', 4, 'worker4'))
   stormtrooper(('root', '10.141.0.154', 'mongodb', 'worker5', 4, 'worker5'))
   stormtrooper(('root', '10.141.0.155', 'mongodb', 'worker6', 4, 'worker6'))
   stormtrooper(('root', '10.141.0.156', 'mongodb', 'worker7', 4, 'worker7'))
   stormtrooper(('root', '10.141.0.157', 'mongodb', 'worker8', 4, 'worker8'))
   stormtrooper(('root', '10.141.0.158', 'mongodb', 'worker9', 4, 'worker9'))
   stormtrooper(('root', '10.141.0.159', 'mongodb', 'worker10', 4, 'worker10'))
