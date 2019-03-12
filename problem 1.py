#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:29:28 2019

@author: heroname
"""

class Student:
    def __init__(self, cwid, first_name, last_name, gender, gpa):
        self.__cwid = cwid
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__gpa = gpa
    
    @property
    def get_cwid(self):
        return self.__cwid
    @set_cwid.setter
    def set_cwid(self, cwid):
        self.__cwid = cwid
        
    @property
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name
        
    @property
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    @property
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self.__gender = gender
        
    @property
    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, gpa):
        self.__gpa = gpa