
import os
import textwrap
def rename_files():
    file_list = os.listdir("/home/rjshekar90/Desktop/prank/prank")
    print file_list

    os.chdir("/home/rjshekar90/Desktop/prank/prank")
    for file_name in file_list:
        z =  file_name.translate(None, "0123456789")
        print os.rename(file_name, z)



        #os.rename()
rename_files()