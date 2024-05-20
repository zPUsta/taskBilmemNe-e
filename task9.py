

import os
import shutil

try:
    os.makedirs("Example/subdirect")
except FileExistsError:
    pass
img_path = "img.png"
img_destination = os.path.join("img.png", "Example/subdirect")
shutil.move("img.png","Example/subdirect")
try:
    if os.path.exists(img_destination):
        print("fayl artıq mövcuddur")
except FileNotFoundError:
    print(img_path + "tapılmadı")
    
txt_files = [i for i in os.listdir("Example/subdirect/") if i.endswith(".txt")]

for txt in txt_files:
    shutil.copy(f"Example/subdirect/{txt}","Example/")
    
 