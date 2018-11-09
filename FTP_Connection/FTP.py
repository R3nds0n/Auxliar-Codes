from ftplib import FTP
import io,os,datetime

def connectString():

    connect = open('connect.config', 'r').read()
    ftp = FTP(connect.split(';')[0],connect.split(';')[1], connect.split(';')[2])
    return ftp


def downloadFile():

    file = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, file.write, 1024)

    ftp.quit()
    file.close()


def uploadFile():
    for path in os.listdir(filename):
        for root, dirs, files in os.walk(filename):
            if files != []:
                for file in files:
                    ftp = connectString()
                    doc = filename+path+'/'+file
                    try:
                        ftp.mkd(path)
                    except:
                        pass

                    ftp.cwd(path)
                    blob = open(doc, 'rb')
                    ftp.storbinary('STOR '+file, blob)
                    ftp.quit()
                    datedir = filename+\
                              str(datetime.datetime.today())[0:10].replace('-','')
                    try:
                        os.system('mkdir "' + datedir + '"')
                    except:
                        pass
                    print('move /y "' + doc + '" "' + datedir +'/'+path+'/'+file+'"')
                    os.system('move /y "' + doc + '" "' + datedir +'/'+path+'/'+file+'"')


if __name__ == '__main__':
    filename = 'C:/temp/'
    uploadFile()



