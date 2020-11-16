#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:21:28 2020

@author: shiwanshu
"""


import os


folder = "/Users/shiwanshu/Pictures/Diwali/"

    
def main():
    original          = [".HEIC",".heic"]
    desired_extension = ".jpg"
    
    try:
        for filename in os.listdir(folder):
            
            infilename = os.path.join(folder,filename)
            
            if not os.path.isfile(infilename): 
                continue
            
            oldbase = os.path.splitext(filename)
            
            if oldbase[1] in original:
                newname = infilename.replace(oldbase[1], desired_extension)
                os.rename(infilename, newname)
                
        print("Changed all your files from ",original[0],'to',desired_extension,'\n', 'Thank you:)')
                
    except:
        print("filename not found and directory doesnot exist!")
        
if __name__ == '__main__':
    main()
    
    