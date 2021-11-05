import io
import os
import zipfile
import shutil

previous_files = {}
files = []
zips = "C:\\Users\\alexd\\OneDrive\\Desktop\\New folder\\"

def check_file_names(folder, project_name):

    files = os.listdir(folder)

    for file in files:
        if (file.endswith(".zip")):
            with zipfile.ZipFile(zips + file, "r") as z:
                z.extractall("temp_files\\" + project_name)
                
                if (previous_files.get(zips + str(file)) == None):
                    previous_files[zips + str(file)] = 0
                    z.extractall("projects\\" + project_name)
                else:
                    os.rename("temp_files\\" + project_name, previous_files[project_name] + 1)
                    previous_files[zips + str(file)] = previous_files[project_name] + 1
                    z.extractall("projects\\" + previous_files[project_name] + 1)
