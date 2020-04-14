import shutil
import os

path = input(
    "Enter path to folder you want to organise (default : current folder) :")
path = path or "."

# list of all files
filelist = os.listdir(path)

#sort into series 
print("\n\nSeries:\n")
for file_ in filelist:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if (name == "Series" or name=="Movies") or (name == "organise" and ext == "py"):
        continue
    segments = name.split(".")
    for i in range(len(segments)):
        if (len(segments[i])==3 and segments[i][0].lower()=="s" and segments[i][1].isnumeric() and segments[i][2].isnumeric()) or (len(segments[i])==6 and (segments[i][0].lower()=="s" and segments[i][3].lower()=="e") and (segments[i][1].isnumeric() and segments[i][2].isnumeric() and segments[i][4].isnumeric() and segments[i][5].isnumeric() )):
            season = segments[i][0].lower()+segments[i][1:3]
            tv = ""
            for c in range(i):
                tv = tv + segments[c] + " "
            tv = tv.strip()    
            print(tv,":Season ",season)
            if os.path.exists(os.path.join(path, "Series")):
                
                if not os.path.exists(os.path.join(path,"Series", tv)):
                    os.makedirs(os.path.join(path,"Series", tv) )

                    if not os.path.exists(os.path.join(path,"Series", tv,season)):
                        os.makedirs(os.path.join(path,"Series", tv,season) )
                else:

                    if not os.path.exists(os.path.join(path,"Series", tv,season)):
                        os.makedirs(os.path.join(path,"Series", tv,season) )
                

            else:
                if not os.path.exists(os.path.join(path,"Series", tv)):
                    os.makedirs(os.path.join(path,"Series", tv) )

                    if not os.path.exists(os.path.join(path,"Series", tv,season)):
                        os.makedirs(os.path.join(path,"Series", tv,season ))
                else:

                    if not os.path.exists(os.path.join(path,"Series", tv,season)):
                        os.makedirs(os.path.join(path,"Series", tv,season ))
       
            shutil.move(os.path.join(path, file_),os.path.join(path,"Series", tv,season ))
            break

#sort into movies
print("\n\nMovies:\n")
filelist = os.listdir(path)
for file_ in filelist:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]

    if (name == "Series" or name=="Movies") or (name == "organise" and ext == "py"):
        continue

    print(file_)
    if os.path.exists(os.path.join(path, "Movies")):
        shutil.move(os.path.join(path, file_), os.path.join(path, "Movies"))
    else:
        os.makedirs(os.path.join(path, "Movies"))
        shutil.move(os.path.join(path, file_), os.path.join(path, "Movies"))
