import shutil
import os
import imdb

path = input(
    "Enter path to folder you want to organise (default : current folder) :")
path = path or "."

# DEFINE FOLDER FOR MOVIE AND TV

if not os.path.exists(os.path.join(path, "TV")):
    os.makedirs(os.path.join(path, "TV"))

if not os.path.exists(os.path.join(path, "Movies")):
    os.makedirs(os.path.join(path, "Movies"))




def movieorg(title,year,file_):
    #sort into movies
    print("\n\nIT Movies:\n")
    print(file_)

   


def tvorg(title,year,file_,path):
    print("its tv")
    if not os.path.exists(os.path.join(os.path.join(path, "Movies"),title+"("+str(year)+")")):
        os.makedirs(os.path.join(os.path.join(path, "Movies"),title+"("+str(year)+")"))




def main(path):
    # list of all files
    filelist = os.listdir(path)
    ## TODO
    ### CHECK FOR FILES
    #### AND RECURSIVE
    # indexes every file
    
    for file_ in filelist:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]
        if (name == "Series" or name=="Movies") or (name == "organise" and ext == "py") or (name=="DeepOrganise" and ext == "py"):
            continue
        title = name.replace("."," ")
        print(title)
        ia = imdb.IMDb()
        movie_obj = ia.search_movie(title)
        el = ia.get_movie(movie_obj[0].movieID)
        title = el.get('title')
        year = str(el.get('year'))
        kind = str(el.get('kind'))
        if kind[0] == 't':
            movieorg(title,year,file_)
        else :
            tvorg(title,year,file_,path)


"""
#sort into series 
print("\n\nSeries:\n")

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

"""
if __name__ == '__main__':
    main(path)
    
