# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 13:42:36 2023

@author: GFCACACE
"""

import os

from Config.PATH import USER_SPACE_PATH
from Modules.Commons.TOKENS import Token

class Task:
    
    def __init__(self,
                 objective_prompt:str,
                 databases,
                 procedures,
                 ):
        self.objective_prompt=objective_prompt
        self.databases=databases
        self.procedures=procedures
        self.databases_path = os.path.join(self.service_name_path,"Databases")
        #Creo los nuevos directorios propios de la Tarea
        os.mkdir(self.databases_path)

        
    def add_procedure(self):
        """
        Creates a Procedure that belongs to the Task that generated it
        
        """
        pass
    def remove_procedure(self):
        """
        Removes a Procedure that belongs to the Task that generated it
        
        """
        pass    
    def config_procedure(self,Procedure):
        """
        Configures the params from the procedure that are indicated
        
        """        
        pass