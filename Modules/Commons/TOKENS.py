# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:57:53 2023

@author: Usuario
"""

from enum import Enum

class Token(Enum):
    #Service Tokens
    WAITING="WAITING"
    RUNNING="RUNNING"
    SUSPENDED="SUSPENDED"
    BLOCKED = "BLOCKED"
    READY="READY"