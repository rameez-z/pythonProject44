import glob
import os
import time

files = glob.glob('/home/ubuntu/Downloads/*.pdf')
modified_files = list()
current_time = time.time()
with open("/home/ubuntu/Downloads/test.txt", "w") as file1:
    for pdf_file in files:
        time_delta = current_time - os.path.getmtime(pdf_file)
        time_delta_days = time_delta / (60 * 60 * 24)
        if time_delta_days > 3:
            modified_files.append(pdf_file)
            file1.write(pdf_file)
            os.remove(pdf_file)
file1.close()
