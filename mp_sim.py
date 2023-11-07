import meep as mp
import numpy as np
import temp_global_var

def build(**kwargs):
    try:

        sim = mp.Simulation(
            
            cell_size = temp_global_var.get_value('cell_size'),
            boundary_layers = temp_global_var.get_value('boundary'),
            geometry = temp_global_var.get_value('geometry'),
            sources = temp_global_var.get_value('sources'),
            resolution = temp_global_var.get_value('resolution'),
            **kwargs
            
    
            
            )
        print('ssss')
        temp_global_var.set_value('sim_obj', sim)
        msg = 'Simulation Object is saved.'
        return msg
        
    except:
        msg = ('Please define at least a FDTD volume before build the Simulation.')
        return msg

def run():
    sim = temp_global_var.get_value('sim_obj')
    sim.run()

    
    
    