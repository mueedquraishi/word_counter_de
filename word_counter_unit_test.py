#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import re
import unittest
from word_counter_de import *


# In[ ]:


class TestWordCounter(unittest.TestCase):

    # test to check for removal of special chars either end of string    
    def test_remove_non_alphanum_spec_chars(self):
        result = remove_non_alphanum("  ^&*billy!@# ")
        self.assertEqual(result, "billy")

    # test for removal of special chars on empty strings
    def test_remove_non_alphanum_empty(self):
        result = remove_non_alphanum("")
        self.assertEqual(result, "")
        
    # test for checking if the file is being read properly        
    def test_file_reader_valid_file(self):
        test_str = 'zsdfdsfdfsdfsdf`sdf232 242 24 24242w we w'
        rand_file_name = 'zsdfkjfnsdkfjdkfnsf'
        with open(f'{rand_file_name}.txt', 'w', encoding='utf-8') as temp_file:
            temp_file.write(test_str)

        result = file_reader(f'{rand_file_name}.txt')
        os.remove(f'{rand_file_name}.txt')
        
        self.assertEqual(result, test_str)  
        
    # test if the string cleaning function works         
    def test_clean_string_func(self):
        result = clean_string("this is a ! test string!")
        self.assertEqual(result, ['this', 'is', 'a', 'test', 'string'])
            
    # test if the word counter function orders the data properly             
    def test_word_counter_order(self):
        word_list = ['orange','orange','apple', 'apple', 'apple','egg']
        expected_result = (('apple', 3), ('egg', 1))

        result = word_counter(word_list)
        first_last_entry = list(result.items())[0],list(result.items())[-1]
        
        self.assertEqual(first_last_entry, expected_result)

if __name__ == '__main__':
    unittest.main()


# In[ ]:




