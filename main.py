import os
from pathlib import Path

dir_path    = "E:/Programming/Python/File Organizer/test/toorg/"

path    = [
            "E:/Programming/Python/File Organizer/test/orged/aud/",
            "E:/Programming/Python/File Organizer/test/orged/com/",
            "E:/Programming/Python/File Organizer/test/orged/doc/",
            "E:/Programming/Python/File Organizer/test/orged/oth/",
            "E:/Programming/Python/File Organizer/test/orged/pic/",
            "E:/Programming/Python/File Organizer/test/orged/vid/"
            ]

aud_formats = ('mp3','ogg','wav','amr')
com_formats = ('zip','rar','7z','tar')
doc_formats = ('doc','docx','ppt','xls','txt','pdf')
pic_formats = ('png','jpg','jpeg','gif','bmp')
vid_formats = ('3gp','avi','flv','mkv','mov','mp4','mpeg','webm','ts')


def getBase(name):
    return name[0:-len(name.split('.')[-1:][0])-1]

def check_folder():
    for a in path:
        b=Path(a)
        if(not b.is_dir()):
            os.mkdir(a)
    m_dir=path[5]+'movies/'
    if(not Path(m_dir).is_dir()):
        os.mkdir(m_dir)


def organize(dir_path):

    check_folder()
    
    for root, dirs, files in os.walk(dir_path): 
        for file in files:
            f=root+'/'+file
            try:
                file_size = os.stat(f).st_size/1048576
            except FileNotFoundError:
                continue
            print(file)

            if file.endswith(vid_formats):
                
                if(file_size > 500):
                    
                    srt_file=root+'/'+getBase(file)+'.srt'
                    movie_name=getBase(file)
                    movie_dir=Path(path[5]+'movies/'+movie_name)

                    if(not movie_dir.is_dir()):
                        os.mkdir(path[5]+'movies/'+movie_name)
                    
                    if(Path(srt_file).is_file()):
                        print(srt_file)
                        os.rename(srt_file,path[5]+'movies/'+movie_name+'/'+getBase(file)+'.srt')
                        
                    os.rename(f,path[5]+'movies/'+movie_name+'/'+file)
                    
                else:
                    os.rename(f,path[5]+file)
                
            elif file.endswith(aud_formats):
                os.rename(f,path[0]+file)
                
            elif file.endswith(com_formats):
                os.rename(f,path[1]+file)

            elif file.endswith(pic_formats):
                os.rename(f,path[4]+file)

            elif file.endswith(doc_formats):
                os.rename(f,path[2]+file)

            else:
                os.rename(f,path[3]+file)


organize(dir_path)
print('done')

