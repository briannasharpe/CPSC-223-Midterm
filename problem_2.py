#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:39:27 2019

@author: heroname
"""
from problem_1 import Student

class student_list(list):
    pass # placeholder, no executed code
    
def main():
    student_data = student_list()
    the_list = ()
    
    num_students = int(input("Number of students: "))
    
    for a in num_students:
        data = input("Student data: ")
        
        # split data into sections
        data_list = data.split(', ')
        
        for e in data_list:
            # separate key and value from data sections
            key, value = e.split(':')
            
            the_list.append(value)
    

    # ---------- end for loop (data_list) ----------

print(student_list(student_info))