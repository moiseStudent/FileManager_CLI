#!/usr/bin/env python3

import os
import shutil

class FileManager:
    def __init__(self) -> None:
        pass
    
    def organize_files(self, path: str) -> str:

        if path == os.getcwd():
            return "Error: This function cannot be executed in the script's root path."

        documents_type = [
            'images',
            'documents',
            'audios',
            'videos',
            'compressed',
            'executable',
            'dev'
        ]

        ### Extensions Dictionary 
        extensions = {
            documents_type[0]:['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg'],
            documents_type[1]:['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt'],
            documents_type[2]:['.mp3', '.wav', '.aac', '.flac'],
            documents_type[3]:['.mp4', '.avi', '.mkv', '.mov'],
            documents_type[4]:['.zip', '.rar'],
            documents_type[5]:['.exe', '.bat', '.deb'],
            documents_type[6]:['.html']
        }

        ### Gets the file list into the path given.
        files = os.listdir(path)

        for file in files:

            ### Verify that this elements is not neither hidden file or a folder.
            if not file.startswith('.') and os.path.isdir(file) == False:
                
                found = False
                i = 0
                
                while found == False and i <= 6:
                    ### Search the extension into the dict.
                    if str(os.path.splitext(file)[1]) in extensions[documents_type[i]]:
                        """
                        When it is True, mean that it has found the extension on
                        the current list, then Makes the folder if not exits and
                        move the file to there.
                        """
                        folder_name = documents_type[i]
                        os.makedirs(f"{path}/{folder_name}", exist_ok=True)
                        shutil.move(f"{path}/{file}", f"{path}/{documents_type[i]}")

                        found = True

                    else:

                        os.makedirs(f"{path}/unknown", exist_ok=True)
                        #print("The file will save into unknown folder")
                        found = False
                        i += 1

        return "The files have been organized"
