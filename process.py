from CardReaderNew import readFile, processImage, analyzeInformation, imageData
import os
from datetime import datetime, timedelta
import pytz

PROJ_DATA_DIR = '/home/cddl/scans/'
SCAN_DIR = PROJ_DATA_DIR + 'scans/raw/'
JSON_DIR=PROJ_DATA_DIR+'scans/'
STATIC_DIR=PROJ_DATA_DIR+'www/nextstop/static/cards/exhibit/'
'''check the directory'''
mFile=readFile.checkCreate(JSON_DIR)

#   Get the file list in a directory
fileList=readFile.get_file_list(SCAN_DIR)

tz = pytz.timezone('America/New_York')
now = datetime.now(tz)
oneDay = timedelta(hours=24)
lastDayList = [f for f in fileList if ((now - datetime.fromtimestamp(os.path.getmtime(f),tz) <= one_day))]

if len(lastDayList) > 0:
    for i in range(len(last_day_list)):
        print("index:"+str(i)+"  "+str(fileList[i]))
        src=readFile.get_img(SCAN_DIR+fileList[i])

        '''return the checkbox information, inputbox information and rotated image'''
        check_info,input_info,srcc=processImage.pre_process_img(STATIC_DIR,fileList[i],src)

        '''statusCode   =   -2   blank page'''
        '''             =   -1   Not settled image'''
        '''             =   0-9  Settled image template id'''
        '''result               bool of image checked when statusCode is 2'''
        '''info                 checkbox information'''
        '''structure            question structure'''
        statusCode,result,info=analyzeInformation.analyze(check_info,input_info,srcc)
        if(statusCode>=0):
            print(imageData.image_TargeTitle[statusCode])
        '''Save to file'''
        readFile.WriteJson(fileList[i],i,statusCode,result,info,mFile,SCAN_DIR)

    mFile.close()

