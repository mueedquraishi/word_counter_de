#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import argparse


# In[110]:


def remove_non_alphanum(word):
    start = 0 
    end = len(word)
    
    while start < end and not word[start].isalnum():
        start += 1
    while end > start and not word[end -1].isalnum():
        end -= 1
    word = (word[start:end])
    return word

def file_reader(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return 'incorrect file path'
    
def clean_string(input_str):
    if input_str is None or len(input_str) == 0:
        raise ValueError('no data in the file')
    
    words = input_str.replace('\n',' ').split(' ')
    cleaned_list = [remove_non_alphanum(a).lower() for a in words if remove_non_alphanum(a) != '']
    return cleaned_list
    
def word_counter(word_list):
    word_counts = {}
    
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_items = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

def runner(path):
    file_string = file_reader(path)
    cleaned_list  = clean_string(file_string)
    word_count = word_counter(cleaned_list)
    
    result = ''
    for word, count in word_count.items():
        result += f'{word}: {count}\n'
    return result 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    print(runner(args.path))


# In[ ]:




