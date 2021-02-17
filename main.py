import os
import shutil
import json


class FileHandle:
    def __init__(self):
        self.home_path = os.environ.get("USERPROFILE")

    def get_config(self):
        with open("config.json") as conf_file:
            config = json.load(conf_file)
        return config
    
    
    def find_files(self, path):
        for i in os.listdir(path):
            info = os.stat(os.path.join(path, i))
            # print(info)
            for roots, dirs, files in os.walk(os.path.join(path, i), topdown=False):
                print("Current Directory: ", roots)
                # print("Sub Directories Inside Current Directory: ", dirs)
                print("Files Inside Current Directory: ", files)
                # return "Current File: ", roots, "Sub Directories: ", dirs, "Current File: ", files
    
    def organize(self):
        conf = self.get_config()
        dir_path = conf["Folder_Path"]
        count = 1
      
        for i in os.listdir(os.path.join(self.home_path, dir_path)):
            
            if os.path.isdir(os.path.join(self.home_path, dir_path, i)):
                pass
            elif os.path.isfile(os.path.join(self.home_path, dir_path, i)):
                file1 = i.split(".")
                print(file1[-1])
                try:
                    new_dir = os.path.join(self.home_path, dir_path, file1[-1].upper())
                    if os.path.exists(new_dir):
                        shutil.move(os.path.join(self.home_path, dir_path, i), new_dir)
                    else:
                        os.makedirs(new_dir)
                        shutil.move(os.path.join(self.home_path, dir_path, i), new_dir)
                    
                except:
                    new_dir = os.path.join(self.home_path, dir_path, file1[-1].upper(), '('+str(count)+')')
                    if os.path.exists(new_dir):
                        shutil.move(os.path.join(self.home_path, dir_path, i), new_dir)
                    else:
                        os.makedirs(self.home_path, new_dir)
                        shutil.move(os.path.join(self.home_path, dir_path, i), new_dir)
                    
                    count+=1
        print("Your files have been organized")
        command = input("Do you want to see how is your data sorted? (Yes/No) ")
        if command.upper() == "YES":
            self.find_files(os.path.join(self.home_path, dir_path))
        else:
            pass
            
            
    def remove_dirs(self):
        conf = self.get_config()
        drive = conf["Servers"]
        paths = conf["Folders"]
        # a = [shutil.rmtree(os.path.join(v["drive_name", value, i])) for k, v in drive.items() if v["running"] == True for key, value in paths.items() for i in os.listdir(os.path.join(v["drive_name"], value))]
        # print(a)
        # quit()
        for k,v in drive.items():
            if v["running"] == True:
                for key, value in paths.items():
                    dir = os.listdir(os.path.join(v["drive_name"], value))
                    for i in dir:
                        if os.path.isdir(os.path.join(v["drive_name"],value, i)):
                            # print("======================================"'\n'"Folder"'\n',i)
                            shutil.rmtree(os.path.join(v["drive_name"],value, i))
                        else:
                            # print("======================================"'\n'"File"'\n',i)
                            os.remove(os.path.join(v["drive_name"],value, i))
                print(f"Files Removed for folder {v}")





obj = FileHandle()
obj.organize()