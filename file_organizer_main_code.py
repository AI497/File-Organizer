# File Organizer Project
# Purpose:
    #- Scans a folder
    #- Detects file types
    #- Moves images, documents, videos, etc into smaller folders
    
from pathlib import Path
import os
import shutil
import time

files = os.listdir()
present_files = len(files)

# Types of Files:
    
documents = [".txt" , ".pdf", ".docx"]
images = [".png", ".jpg", ".jpeg"]
videos = [".mp4", ".mov"]
folder = [""]

os.makedirs("Document_Type", exist_ok=True)
os.makedirs("Image_Type", exist_ok=True)
os.makedirs("Video_Type", exist_ok=True)

for i in range(present_files):
    
    x = files[i]
    
    y = os.path.splitext(x)
    
    if y[1] in documents:
        print(y[0] + " is a document")
        
    elif y[1] in images:
        print(y[0] + " is an image")
        
    elif y[1] in videos:
        print(y[0] + " is a video")
        
    elif (y[1] in folder) or y[0] == "file_organizer_main_code":
        continue
        
    else:
        print(y[0] + " is an Unknown File Type")
        
       
def sortFiles(present_files_func):
    
    for i in range(present_files_func):
        
        x = files[i]
        
        y = os.path.splitext(x)
        
        if y[1] in documents:
            shutil.move(x, "Document_Type")
            
        elif y[1] in images:
            shutil.move(x, "Image_Type")
            
        elif y[1] in videos:
            shutil.move(x, "Video_Type")
            
        else:
            continue
    

n = True
        
while n:
    
    try:
        
        inp = input("Would you like to sort the files by their type? (y/n): ")
    
        if (inp == "y") or (inp == "Y"):
            
            print("Organizing Files. . .")
            sortFiles(present_files)
            time.sleep(1)
            print("Files Have Been Organized!")
            n = False
            
            
        elif (inp == "n") or (inp == "N"):
            
            print("Not Organizing Files")
            n = False
            
        else:
            
            raise TypeError
            
    except TypeError:
        
        print("Invalid Answer")
