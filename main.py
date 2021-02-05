import os
import shutil
import json



def get_config():
    with open("config.json") as conf_file:
        config = json.load(conf_file)
    return config


def organize():
    conf = get_config()
    dir_path = conf["Folder_Path"]
    count = 1
    for i in os.listdir(dir_path):
        
        if os.path.isdir(os.path.join(dir_path, i)):
            pass
        elif os.path.isfile(os.path.join(dir_path, i)):
            file1 = i.split(".")
            print(file1[-1])
            try:
                new_dir = os.path.join(dir_path, file1[-1].upper())
                if os.path.exists(new_dir):
                    shutil.move(os.path.join(dir_path, i), new_dir)
                else:
                    os.mkdir(new_dir)
                    shutil.move(os.path.join(dir_path, i), new_dir)
                
            except:
                new_dir = os.path.join(dir_path, file1[-1].upper(), '('+str(count)+')')
                if os.path.exists(new_dir):
                    shutil.move(os.path.join(dir_path, i), new_dir)
                else:
                    os.mkdir(new_dir)
                    shutil.move(os.path.join(dir_path, i), new_dir)
                
                count+=1
        print("Your files have been organized")
            
            
def remove_dirs():
    conf = get_config()
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



if __name__ == '__main__':
    organize()