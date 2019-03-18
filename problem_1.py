#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:29:28 2019

@author: heroname
"""

class Student:
    def __init__(self, cwid, first_name, last_name, gender, gpa):
        self._cwid = cwid
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._gpa = gpa
        
    def get_cwid(self):
        return self._cwid
    def set_cwid(self, cwid):
        self._cwid = cwid
    cwid = property(get_cwid, set_cwid)

    def get_first_name(self):
        return self._first_name
    def set_first_name(self, first_name):
        self._first_name = first_name
    first_name = property(get_first_name, set_first_name)
    
    def get_last_name(self):
        return self._last_name
    def set_last_name(self, last_name):
        self._last_name = last_name
    last_name = property(get_last_name, set_last_name)
    
    def get_gender(self):
        return self._gender
    def set_gender(self, gender):
        self._gender = gender
    gender = property(get_gender, set_gender)

    def get_gpa(self):
        return self._gpa
    def set_gpa(self, gpa):
        self._gpa = gpa
    gpa = property(get_gpa, set_gpa)
    
def student(student_list):
    student = Student(student_list[0], student_list[1], student_list[2], student_list[3], student_list[4])
    student.cwid = student_list[0]
    student.first_name = student_list[1]
    student.last_name = student_list[2]
    student.gender = student_list[3]
    student.gpa = student_list[4]
    return student
    
a_list = [12345678, 'brenda', 'song', 'f', 5.2]
new_student = student(a_list)
print(new_student)
    