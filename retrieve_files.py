"""
@author:  Andile Mbele
program:  Retrieve files 
Date:     28 October 2022 
"""

import os
import shutil


def retrieve_files():
    """
    Retrieve all files with the .docx, .pdf, .txt, .xlsx, .jpg, .jpeg, .png from the entire computer system and copy them to a folder called "files" in the current directory.
    """
    count = 0
    for root, dirs, files in os.walk('C:/Users/andile.mbele/Downloads/'):
        for file in files:
            if file.endswith('.docx') or file.endswith('.docx') or file.endswith('.pdf') or \
                    file.endswith('.txt') or file.endswith('.xlsx') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                if not os.path.exists('files'):
                    os.makedirs('files')
                shutil.copy(os.path.join(root, file), 'files')
                count += 1
                print(f'Copying {file} to files folder')
    print(f"{count} files copied")


if __name__ == '__main__':
    retrieve_files()
