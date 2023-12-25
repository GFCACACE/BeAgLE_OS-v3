# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:51:50 2023

@author: GFCACACE
"""
import os

from Config.PATH import USER_SPACE_PATH

class Organization:
    services=[]
    databases=[]
    def __init__(self,
                 name:str="Organization",
                 memory_limit:int=1073741824,#1GiB by default
                 ):
        """
        INITIALIZES A NEW ORGANIZATION WHEN IS CREATED
        """
        
        self.name=name
        self.memory_limit=memory_limit
        self.organization_path=os.path.join(USER_SPACE_PATH, name)#Generate a directory for the organization at the user space
        self.org_databases_path=os.path.join(self.organization_path,"Databases")
        self.org_services_path=os.path.join(self.organization_path,"Services")
        self.org_LLMS_path=os.path.join(self.organization_path,"LLMS")
        #Create all the required directories that an org has
        os.mkdir(self.organization_path)
        os.mkdir(self.org_databases_path)
        os.mkdir(self.org_services_path)
        os.mkdir(self.org_LLMS_path)
        

    def get_directory_size(self):
        directory = self.organization_path
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size
    
    def space_available(self)->int:

        org_size_in_bytes=self.get_directory_size()
        
        return self.memory_limit - org_size_in_bytes
    
    def create_database(self):
        """
        Creates a Database that belongs to the Organization that generated it
        
        """
        pass
    def remove_database(self):
        """
        Removes a Database that belongs to the Organization that generated it
        
        """
        pass
    def create_service(self):
        """
        Creates a Service that belongs to the Organization that generated it
        
        """
        pass
    def remove_service(self):
        """
        Removes a Service that belongs to the Organization that generated it
        
        """
        pass



org=Organization(name="Instatronic")
print(org.organization_path)
print(str(org.space_available()/1024.0/1024.0/1024.0) + "GiB")
# print(org.organization_path)