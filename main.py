import os
import shutil

dir_path = r"C:\Users\ankit\Desktop\Test1"
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