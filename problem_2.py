#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:39:27 2019

@author: heroname
"""
from problem_1 import student

class student_list(list):
    pass # placeholder, no executed code
    
def main():
    student_data = student_list()
    
    num_students = int(input("Number of students: "))
    
    for a in range(int(num_students)):
        temp_list = []
        
        data = input("Student data: ")
        
        # split data into sections
        data_list = data.split(', ')
        
        for e in data_list:
            # separate key and value from data sections
            key, value = e.split(':')
            # append to temp_list
            temp_list.append(value)
        # ---------- end for loop (data_list) ----------
        # create student
        a_student = student(temp_list)
        # append student to student database
        student_data.append(a_student)
    # ---------- end for loop (range(int(num_students))) ----------
    
    print(student_data)
    # ----- end main() -----

main()