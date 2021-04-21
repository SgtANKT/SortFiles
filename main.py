import os
import shutil
import json
import logging
import datetime


class FileHandle:
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    logging.basicConfig(filename=f"logs\\file_sort_{today_date}.txt", format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.info('Log file initiated')

    # logging.log('Log file initiated')
    def __init__(self):
        self.empty_folders = []
        # self.home_path = os.environ.get("USERPROFILE")
        pass

    def get_config(self):
        with open("config.json") as conf_file:
            config = json.load(conf_file)
        return config

    def remove_dirs(self, path):
        return shutil.rmtree(path)

    def find_files(self, path):
        for i in os.listdir(path):
            info = os.stat(os.path.join(path, i))
            for roots, dirs, files in os.walk(os.path.join(path, i), topdown=False):
                # print(os.path.join(path,i,roots))
                # print(roots)
                logging.info("Root Dirs"+roots)
                if len(os.listdir(os.path.join(path, i, roots))) >=1:
                    logging.info(f"Directory {os.path.join(path, i, roots)} wont be deleted as the folder has files")
                else:
                    logging.warning(f"Directory {os.path.join(path, i, roots)} will be deleted as there are no files in it")
                    self.remove_dirs(os.path.join(path, i, roots))
                # print("Directories Inside Current Directory: ", roots)
                # logging.info("Directory"+str(dirs))
                logging.info("Files inside directory"+str(files))
                # logging.log(logging.INFO, files)
                # print("files
                # Inside Current Directory: ", files)
                # return roots, dirs, files

    def organize(self, dir_path):
        count = 1
        for i in os.listdir(dir_path):

            if os.path.isdir(os.path.join(dir_path, i)):
                pass
            elif os.path.isfile(os.path.join(dir_path, i)):
                file1 = i.split(".")
                print(file1[-1])
                try:
                    logging.info('')
                    new_dir = os.path.join(dir_path, file1[-1].upper())
                    if os.path.exists(new_dir):
                        shutil.move(os.path.join(dir_path, i), new_dir)
                    else:
                        os.makedirs(new_dir)
                        shutil.move(os.path.join(dir_path, i), new_dir)
                except:
                    new_dir = os.path.join(dir_path, file1[-1].upper(), '(' + str(count) + ')')
                    if os.path.exists(new_dir):
                        shutil.move(os.path.join(dir_path, i), new_dir)
                    else:
                        os.makedirs(new_dir)
                        shutil.move(os.path.join(dir_path, i), new_dir)

                    count += 1




    def main(self):
        conf = self.get_config()
        print("Sorting files")
        dir_path = conf["Folder_Path"]
        self.find_files(dir_path)
        print('Deleting empty folders')
        self.organize(dir_path)
        logging.info("Your files have been organized")



if __name__ == '__main__':
    obj = FileHandle()
    obj.main()
