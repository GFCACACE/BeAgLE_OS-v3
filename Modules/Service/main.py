# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:43:44 2023

@author: GFCACACE
"""
import os

from Config.PATH import USER_SPACE_PATH
from Modules.Commons.TOKENS import Token

class Service:
    tasks=[]
    state=Token.BLOCKED
    services_path=os.path.join(USER_SPACE_PATH,"Services")
    def __init__(self,
                 name:str,
                 img_path:str,
                 grant_users:bool=False,#If False, only Admin can Interact with the service
                 max_instances:int=1,
                 ):
        self.name=name
        self.img_path=img_path
        self.grant_users=grant_users
        self.service_name_path=os.path.join(self.services_path,name)
        self.tasks_path = os.path.join(self.service_name_path,"Tasks")
        #Creo los nuevos directorios propios del Servicio
        os.mkdir(self.tasks_path)
        
        
    def create_task(self):
        """
        Creates a Task that belongs to the Service that generated it
        
        """
        pass
    def remove_task(self):
        """
        Removes a Task that belongs to the Service that generated it
        
        """
        pass
    def display_tasks(self):
        """
        Displays the tasks names from the service
        
        """
        task_names=[]
        for task in self.tasks:
            task_names.append(task.name)
        return task_names
    def num_instances(self):
        """
        Counts how many instances are Active at the moment of executing this function
        
        """
        pass
    def num_procedures(self):
        """
        Counts how many procedures are Imported in total on the service
        
        """
        pass
    def db_use(self):
        """
        Returns true if any of the tasks from the Service use a DB 
        
        """
        return any(task.db_use for task in self.tasks)
    
    