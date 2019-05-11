#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 23:55:14 2019

@author: Michael_Keene
"""

def reverse():
    """Take a given sentence and reverse each word in place."""
    
    sentence = input('Enter a sentence: ')
    sentence_list = sentence.split(" ")
    reverse_words = [word[::-1] for word in sentence_list]
    return " ".join(reverse_words)

print(reverse())
