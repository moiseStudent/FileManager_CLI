import os
import shutil
from send2trash import send2trash

# from prompt_toolkit.shortcuts import yes_no_dialog
from InquirerPy import prompt, inquirer


class FileManager:
    def __init__(self) -> None:
        pass

    def organize_files(self) -> None:

        documents_type = [
            "images",
            "documents",
            "audios",
            "videos",
            "compressed",
            "executable",
            "dev",
        ]

        ### Extensions Dictionary
        extensions = {
            documents_type[0]: [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".tiff",
                ".bmp",
                ".svg",
            ],
            documents_type[1]: [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt"],
            documents_type[2]: [".mp3", ".wav", ".aac", ".flac"],
            documents_type[3]: [".mp4", ".avi", ".mkv", ".mov"],
            documents_type[4]: [".zip", ".rar"],
            documents_type[5]: [".exe", ".bat", ".deb"],
            documents_type[6]: [".html"],
        }

        ### Getting list the files into the curret directory
        files = os.listdir()

        for file in files:
            ### Check that it is not a hidden file.
            if not file.startswith("."):
                if os.path.splitext(file)[1] == "":  ### Chekc that it's not a folder.
                    pass

                else:
                    search = False
                    i = 0

                    while search == False and i <= 6:
                        ### Search the extension into the dict.
                        if (
                            str(os.path.splitext(file)[1])
                            in extensions[documents_type[i]]
                        ):
                            """
                            When it is True, mean that it has found the extension on
                            the current list, then Makes the folder if not exits and
                            move the file to there.
                            """

                            os.makedirs(documents_type[i], exist_ok=True)
                            shutil.move(file, documents_type[i])

                            search = True

                        else:
                            print("Guardar en sin clasificar")

                            search = False
                            i += 1

    def DeleteFile(self, path):
        try:
            fileStats = os.stat(
                path
            )  # show file info before delete the file in the delete dialog of prompt_toolkit

            result = inquirer.confirm(
                f"do you want delete this file => fileName= {os.path.basename(path)}, file weight= {fileStats.st_size} Bytes ?",
                default=False,
            ).execute()
            if result:
                send2trash(path)
        except FileNotFoundError:
            print("Error: El archivo que deseas eleminar no existe")


###! Ejecucio unicamente de prueba - It's only for a test
manager = FileManager()
statInfo = manager.DeleteFile("prueba.txt")
print(statInfo)
