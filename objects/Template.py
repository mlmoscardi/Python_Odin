#!/usr/bin/python

import os
from pathlib import Path
import shutil

class Template:
    def __init__(self, projType, projName, location):
        global cur_dir
        self.location = location
        self.projName = projName
        cur_dir = os.getcwd()
        if projType == 'basic':
            self.createBasicStructure(self.projName)
        else: 
            self.createAdvancedStructure(self.projName)            
            

    # Basic Structure
    def createBasicStructure(self, projName):
        # Create dir structure
        try:
            os.makedirs(self.location.get() + '/' + projName)
            print("Directory " , projName ,  " Created ")
        except FileExistsError:
            print("Directory " , projName ,  " already exists")

        if not os.path.exists(self.location.get() + '/' + projName):
            print("Directory " , projName ,  " no such directory")
        else:    
            os.makedirs(self.location.get() + '/' + projName + '/assets/images')
            os.makedirs(self.location.get() + '/' + projName + '/css')
            os.makedirs(self.location.get() + '/' + projName + '/scripts')

        input_files = ['index.html', 'css/app.css', 'scripts/app.js']
        BASE_DIR = cur_dir
        template_path = os.path.join(BASE_DIR, 'FileRes/basic')

        for file in input_files:
            try:
                # Copy sample file
                input_file = open(template_path + '/' + file, 'r')
                content = input_file.read()
                input_file.close()

                # Write content
                try:
                    path = self.location.get() + '/' + projName + '/' + file
                    print(path)
                    output_file = open(path, 'w')
                    output_file.write(content)
                    output_file.close()
                except:
                    print('\nFile could not be written')
            except:
                # new Error
                print('\nTemplate file could not be found')


    # Advanced Structure
    def createAdvancedStructure(self, projName):
        # Create dir structure
        try:
            os.makedirs(self.location.get() + '/' + projName)
            print("Directory " , projName ,  " Created ")
        except FileExistsError:
            print("Directory " , projName ,  " already exists")

        if not os.path.exists(self.location.get() + '/' + projName):
            print("Directory " , projName ,  " no such directory")
        else:    
            os.makedirs(self.location.get() + '/' + projName + '/assets/images')
            os.makedirs(self.location.get() + '/' + projName + '/css')
            os.makedirs(self.location.get() + '/' + projName + '/scripts')

        # copy files
        input_files = ['index.html', 'css/app.css', 'scripts/app.js']
        input_images = ['assets/images/body_bkg.jpg', 'assets/images/header_bkg.jpg']
        BASE_DIR = cur_dir
        template_path = os.path.join(BASE_DIR, 'FileRes/advanced')

        # Write images
        for jpgfile in input_images:
            # adding exception handling
            try:
                img_path = self.location.get() + '/' + projName + '/' + jpgfile
                shutil.copy(template_path + '/' + jpgfile, img_path)
                print(img_path)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                # new Error
                print('\nTemplate file could not be found')
            

        # Write files
        for file in input_files:
            try:
                # Copy sample file
                input_file = open(template_path + '/' + file, 'r')
                content = input_file.read()
                input_file.close()

                # Write content
                try:
                    path = self.location.get() + '/' + projName + '/' + file
                    print(path)
                    output_file = open(path, 'w')
                    output_file.write(content)
                    output_file.close()
                except:
                    print('\nFile could not be written')
            except:
                # Error
                print('\nTemplate file could not be found')