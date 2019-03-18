#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:39:27 2019

@author: heroname
"""
from problem_1 import student

class student_list(list):
    def __init__(self, data):
        self._data = data
    
        # define variables
        a_list = []
    
        # split data into sections
        data_list = data.split(', ')
        
        for e in data_list:
            # separate key and value from data sections
            key, value = e.split(':')
            # add key and value to student dictionary
            a_list.append({key:value})
        # ---------- end for loop (data_list) ----------
        
        return a_list
    
num_students = int(input("Number of students: "))
student_info = input("Student data: ")

print(student_list(student_info))