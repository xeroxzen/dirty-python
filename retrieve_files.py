"""
@author:  Andile Mbele
program:  Retrieve files 
Date:     7 November 2022 
"""

import os
import shutil
import timeit   


def retrieve_files():
    """Retrieve files from a directory"""
    count = 0
    # Directories to look at are Desktop, Documents, Downloads, Pictures, Music, Videos
    directories = [os.path.join(os.path.expanduser('~'), 'Desktop'), os.path.join(os.path.expanduser('~'), 'Documents'), os.path.join(os.path.expanduser('~'), 'Downloads'), os.path.join(os.path.expanduser('~'), 'Pictures'), os.path.join(os.path.expanduser('~'), 'Music'), os.path.join(os.path.expanduser('~'), 'Videos'), \
        os.path.join(os.path.expanduser('~'), 'OneDrive'), os.path.join(os.path.expanduser('~'), 'Movies')]

    # Create a folder called "files" in the current directory
    if not os.path.exists('files'):
        os.makedirs('files')

    start_time = timeit.default_timer()
    
    # Loop through the directories
    for directory in directories:
        # Loop through the files in the directory and their subsequent subdirectories no matter how deep their location is
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    # If the file is a PDF, DOCX, TXT, XLSX, PPTX, JPG, PNG file, copy it to the "files" folder
                    if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xlsx') or file.endswith('.pptx') or file.endswith('.jpg') or file.endswith('.png') or file.endswith('.doc') or file.endswith('.mp4') or file.endswith('.mp3'):
                        shutil.copy(os.path.join(root, file), 'files')
                        count += 1
                        # Print the file name and the directory it was copied from
                        print(f"Copying {file} from {root}")
        except:
            print('Error: Could not access directory')

    print(f'{count} files were copied to the "files" folder.')
    # Display amount of time it took to run the program
    print(f'Time taken: {timeit.default_timer() - start_time} seconds')

if __name__ == '__main__':
    retrieve_files()
