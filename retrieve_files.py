"""
@author:  Andile Mbele
program:  Retrieve files 
Date:     7 November 2022 
"""

import os
import shutil


def retrieve_files():
    """Retrieve files from a directory"""
    count = 0
    # Directories to look at are Desktop, Documents, Downloads, Pictures, Music, Videos
    directories = [os.path.join(os.path.expanduser('~'), 'Desktop'), os.path.join(os.path.expanduser('~'), 'Documents'), os.path.join(os.path.expanduser('~'), 'Downloads'), os.path.join(os.path.expanduser('~'), 'Pictures'), os.path.join(os.path.expanduser('~'), 'Music'), os.path.join(os.path.expanduser('~'), 'Videos'), os.path.join(os.path.expanduser('~'), 'OneDrive'), os.path.join(os.path.expanduser('~'), 'Movies')]

    # Create a folder called "files" in the current directory
    if not os.path.exists('files'):
        os.makedirs('files')

    # Loop through the directories
    for directory in directories:
        # Loop through the files in the directory
        try: 
            for file in os.listdir(directory):
                # If the file is a .docx, .pdf, .txt, .xlsx, .jpg, .jpeg, .png file, copy it to the "files" folder
                if file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.txt') or file.endswith('.xlsx') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                    shutil.copy(os.path.join(directory, file), 'files')
                    count += 1
        except:
            print("Error: ", directory)

    print(f'{count} files were copied to the "files" folder.')

if __name__ == '__main__':
    retrieve_files()
