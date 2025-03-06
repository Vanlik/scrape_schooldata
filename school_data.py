# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter.font import Font
# from tkinter import messagebox
# from tkinter import ttk
import os
import sys
# import uploads
#Loading required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
import pandas as pd
import csv
import time
from datetime import datetime
from collections import OrderedDict
import re
import os
# from webdriver_manager.chrome import ChromeDriverManager
import shutil
import glob
from pathlib import Path #dealing with directory

# global list_grade
# global list_lower_subjects
# global list_upper_subjects
# global list_primary_subjects

list_grade = [7,8,9,10,11,12]
list_upper_subjects = [
'សេដ្ឋកិច្ចវិទ្យា',
'គេហវិជ្ជា',
'បច្ចេកវិទ្យាព័ត៌មាន',
'ផែនដីនិងបរិស្ថានវិទ្យា',
'សីលធម៌-ពលរដ្ឋវិជ្ជា',
'ភូមិវិទ្យា',
'គណិតវិទ្យា (កម្រិតខ្ពស់)',
'គណិតវិទ្យា',
'ភាសាខ្មែរ',
'គីមីវិទ្យា',
'ជីវវិទ្យា',
'រូបវិទ្យា',
'ប្រវត្តិវិទ្យា',
# 'english'
]
list_lower_subjects = [
'គេហវិជ្ជា',
'បច្ចេកវិទ្យាព័ត៌មាន',
'ផែនដីវិទ្យា',
'សីលធម៌-ពលរដ្ឋវិជ្ជា',
'ភូមិវិទ្យា',
'គណិតវិទ្យា',
'ភាសាខ្មែរ',
'គីមីវិទ្យា',
'ជីវវិទ្យា',
'រូបវិទ្យា',
'ប្រវត្តិវិទ្យា',
# 'english'
]
list_primary_subjects = [
"សិក្សាសង្គម",
"វិទ្យាសាស្ត្រ",
"សិក្សាសង្គម-វិទ្យាសាស្ត្រ",
"គណិតវិទ្យា",
"ភាសាខ្មែរ"]

list_vtype = ["standard", "other"]   


############## Initial variables ####################
JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"
# # Direct to upload section: Standard /other type of videos
# global standard 
# standard = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-category-option-dialog/div[2]/div/a[1]"
# global other 
# other = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-category-option-dialog/div[2]/div/a[2]"

doc_xpath = "/html/body/div[2]/div[2]/div/mat-dialog-container"
video_xpath = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-video-uploader-dialog/mat-dialog-actions/button"

######################################################

#Open the studio
driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://emis.moeys.gov.kh/#/pages/school-report-card")
time.sleep(1)


# Get to advance search
driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div/div/div/button[2]").click()
driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/form/div/div/div/div/div/div[1]/div/div[2]/div/div[4]").click()


# getting list of schools
list_province_2023 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div").text.split("\n")

# select province
driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/form/div/div/div/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[1]/div[1]/div[1]").click()



'''//*[@id="list-item-96-''' + str(enum_pro) + '''"]''' # enumerate len of province lsit to item list

# search result by province
driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/form/div/div/div/div/div/div[3]/div/but
ton[1]").click()

'''//*[@id="list-item-199-'''+ str(3) + '''"]''' # expand to "All"


 School Name៖ 


def check_if_complete(i_xpath):
    x1=0
    while x1==0:
        count=0
        try:
            if driver.find_element_by_xpath(i_xpath):
                count = count+1
                print("Please wait, thing is still uploading :(:(:( ...................." + str(datetime.now().strftime("%H:%M:%S")))
                x1=0
                time.sleep(5)
        except:
            x1=1
            print("Yay:):):)!!!!!!!!!!!!" + " it is up completely at: " + str(datetime.now().strftime("%H:%M:%S")))

def drop_files(element, files, offsetX=0, offsetY=0):
    driver = element.parent
    isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    paths = []
    
    # ensure files are present, and upload to the remote server if session is remote
    for file in (files if isinstance(files, list) else [files]) :
        if not os.path.isfile(file) :
            raise FileNotFoundError(file)
        paths.append(file if isLocal else element._upload(file))
    
    value = '\n'.join(paths)
    elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

WebElement.drop_files = drop_files

def get_subject(x):
    prime_level = [1,2,3,4,5,6]
    lower_level =[7,8,9]
    upper_level =[10,11,12]
    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[6]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]"))).click()
    #check subject code (1-7) (ex: "..option[6]" for Maths)
    time.sleep(1)
    
    if grade in [str(i) for i in upper_level]:
        for enum_sub, i_sub in enumerate(list_upper_subjects):
            if i_sub == x:
                sub_xpath = "/html/body/div[2]/div[2]/div/div/div/mat-option[" +str(list_upper_subjects.index(i_sub) + 1) + "]"
    elif grade in [str(i) for i in lower_level]:
        for enum_sub, i_sub in enumerate(list_lower_subjects):
            if i_sub == x:
                sub_xpath = "/html/body/div[2]/div[2]/div/div/div/mat-option[" +str(list_lower_subjects.index(i_sub) + 1) + "]"
    else:
        for enum_sub, i_sub in enumerate(list_lower_subjects):
            if i_sub == x:
                sub_xpath = "/html/body/div[2]/div[2]/div/div/div/mat-option[" +str(list_primary_subjects.index(i_sub) + 1) + "]"

    return(WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,sub_xpath))).click())

def get_subvideotype(y):
    list_type = [
    "មេរៀនតាមសៀវភៅគោល",
    "សំណួរ-ចម្លើយ",
    "សន្លឹកកិច្ចការមេរៀន",
    "សង្ខេបមេរៀន",
    "វីដេអូសំណួរ-ចម្លើយ",
    "វីដេអូសកម្មភាពក្នុងថ្នាក់",
    "ការបង្រៀនសង្ខេបនិងបញ្ញត្តិ"
    ]

    list_special_content = [
    'ការរៀបចំបង្កើតសៀវភៅសិក្សាថ្មី',
    'កម្មវិធីបណ្តុះបណ្តាលសិស្សពូកែ',
    'ធនាគារសំណួរតាមពីរ៉ាមីឌនៃពុទ្ធិសម្បទា',
    'មាតិកានៃការសិក្សាតាមការបង្កើតគម្រោង'
    ]

    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[4]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]"))).click()
    time.sleep(1)

# ## *************************
# if content_type == "secondary":
#     use list_type
# elif content_type == "special":
#     use list_special
#******************************
    for enum_type, i_type in enumerate(list_special_content): # if list_type, mat-option[" +str(list_type.index(i_type) + 1 )
        if i_type == y:
            sub_xpath = "/html/body/div[2]/div[2]/div/div/div/mat-option[" +str(list_special_content.index(i_type) + 1 ) + "]"
    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,sub_xpath))).click()
    time.sleep(1)

    #********
    #add pbl thumbnails
    driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[11]/div/input").send_keys(os.getcwd() + "\\pbl_pic.jpg")
    time.sleep(3)

def get_intropage():
    #log in credential
    WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-login/div/div[2]/form/mat-form-field[1]/div/div[1]/div[4]/input"))).send_keys("ministry_school")
    WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-login/div/div[2]/form/mat-form-field[2]/div/div[1]/div[4]/input"))).send_keys("Mstr@0102")
    time.sleep(1)
    ele_login = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[2]/form/button")
    ele_login.click()#click on lesson tap
    time.sleep(3)
    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-home/app-menu/ul/li[2]/a"))).click()
    time.sleep(2)
def get_typevideo(video_type):
        if video_type == 'other':
            video_type = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-category-option-dialog/div[2]/div/a[2]"
            WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,video_type))).click()
            
            # Inserting process starts here by each video
            #content type selection (8)
            time.sleep(1)
            # ele_content_type = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]")
            # ele_content_type.click()
            driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]").click()
            time.sleep(2)

            # *******************************
                # if video_type == "secondary":
                # use list_type
                # elif video_type == "special content":
                # use list_special_content

            #check code content type from 1-8 (ex: "..option[8]"" for high school content) 
            # content_select = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[2]")
            # content_select.click()
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[2]").click()
            time.sleep(1)

            #video type selection (Screen Record, សកម្មភាពក្នុងថ្នាក់រៀន)
            get_subvideotype(video_content)

            # ele_video_type = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[4]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]")
            # ele_video_type.click()
            # time.sleep(1)
            # # choose ...option[4] for "screenrecord" & ...option[6] for "សកម្មភាពក្នុងថ្នាក់រៀន")
            # video_select = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[6]")
            # video_select.click()
            # time.sleep(1)
            
            #grade selection (12)
            ele_grade = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[5]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]")
            ele_grade.click()
            time.sleep(1)
            # driver.find_element_by_xpath("/html/body/app-root/app-course/div/div/h1/a").click()
            
            #check grade code (start from ooption[2] 1-12) (ex: "..option[2]" for grade 1) 
            grade_select = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[" + str(int(grade) + 1) + "]")
            grade_select.click()
            time.sleep(1)

            #subject selection
            get_subject(subject)
            time.sleep(1)

        elif video_type == 'standard':
            video_type = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-category-option-dialog/div[2]/div/a[1]"
            WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,video_type))).click()
            time.sleep(1)
            #grade selection (12)
            ele_grade = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[5]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]")
            ele_grade.click()
            time.sleep(1)
            # driver.find_element_by_xpath("/html/body/app-root/app-course/div/div/h1/a").click()
            
            #check grade code (start from ooption[2] 1-12) (ex: "..option[2]" for grade 1) 
            grade_select = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[" + str(int(grade) + 1) + "]")
            grade_select.click()
            time.sleep(1)

            #subject selection
            get_subject(subject)
            time.sleep(1)

def video_upload(less_path, chap_title):
    # Getting all lesson videos inside each chapter folders
    list_video = []
    for i in os.listdir(less_path):
        if not(i.endswith("pdf")):
            list_video.append(i)
# getting ordered list of videos in the directory
    list_ordered = []
    list_ordered_video = []
    for enum_order, i_order in enumerate(list_video):
        list_ordered.append(list_video[enum_order].split("-")[0])
        list_ordered = sorted(list_ordered, key=lambda v: [int(p) for p in v.split('.') if p.isdigit()]) #sorted sub number (ex: 1.2.3)
    for j in list_ordered:
        for k in list_video:
            if j == k.split("-")[0]:
                list_ordered_video.append(k)

    #taking lesson name from each file name
    dict_less_title = {}
    for enum_video, i_video in enumerate(list_ordered_video):
        if i_video.endswith(".mp4"):
            less_order = i_video.split("-")[1].replace("\u200b", "") #1 #3
            less_title = i_video.split("-")[2].replace("\u200b", "") #2 #4
            sub_less = i_video.split("-")[3].replace("\u200b", "") # 3 #5
            descr_title = i_video.split("-")[-1].split(".")[0].replace("\u200b", "")
            list_chap_title.append(chap_title)
            list_less_title.append(less_title)
            if "(" or ")" in sub_less:
                sub_less = i_video.split("-")[3].replace("\u200b", "").replace("(", "").replace(")", "") #3 #5
            time.sleep(3)
            if less_order in dict_less_title:
                dict_less_title[less_order].append(less_title + " " + sub_less)
                driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li[" + str(len(dict_less_title)) + "]/p/span[2]/button[2]" ).click()
                
            else:
                dict_less_title[less_order] = list()
                dict_less_title[less_order].append(less_title + " " + sub_less) # multiple lessons in one chapters
                
                # click on + ជំពូកថ្មី
                WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-content/h2/button"))).click() #add video
                time.sleep(3)
                # Add lesson title before  
                WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-module/div/app-form-title/mat-form-field/div/div[1]/div[3]/input"))).send_keys(less_order + " " + less_title)
                time.sleep(3)
                driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li[" + str(len(dict_less_title)) + "]/p/span[2]/button[2]" ).click()
            
            print(less_order + "_" + less_title + "_"+ str(datetime.now().strftime("%H:%M:%S")))
            # Add lesson title before  
            # WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-module/div/app-form-title/mat-form-field/div/div[1]/div[3]/input"))).send_keys(less_order + " " + less_title)
            
            # # click add new video for each lesson
            # time.sleep(1)
            # if len(dict_less_title) == 1:
            #   WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-content/h2/button"))).click() #add video
            #   time.sleep(1)
            #   # Add lesson title before  
            #   WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-module/div/app-form-title/mat-form-field/div/div[1]/div[3]/input"))).send_keys(less_order + " " + less_title)
            #   time.sleep(1)
            #   # driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li/p/span[2]/button[2]").click()
            # else:
            #   driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li[" + str(len(dict_less_title)) + "]/p/span[2]/button[2]" ).click()

            ele_add_video = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/button[1]")
            ele_add_video.click() #add video
            time.sleep(3)

            #inserting sub lesson title after and uploading
            ele_sub = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-video/div/app-form-title/mat-form-field/div/div[1]/div[3]/input")
            ele_sub.send_keys(less_title + " " + sub_less)
            drop_file = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-video/div/app-video-uploader/div/div")))
            drop_file.drop_files(less_path + "\\" + i_video) #put less_path
            time.sleep(5)
            #adding description
            driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-video/div/div[1]/mat-form-field/div/div[1]/div[3]/textarea").send_keys("ខ្លឹមសារ៖ "+ descr_title)
            
            # check if the download is completed    
            check_if_complete(video_xpath)
            time.sleep(5)
            list_lesson_done.append(i_video.split("-")[0].replace("\u200b", ""))

def pbl_upload(less_path, chap_title):
    ele_add = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/h2/button")
    ele_add.click() #add video
    time.sleep(1)
    cnt_pdf = 0
    cnt_mp4 = 0
    for i_file in sorted(os.listdir(less_path), key=lambda v: [int(p) for p in v.split('.') if p.isdigit()]):
        if i_file.endswith("pdf"):
            cnt_pdf += 1
            if cnt_pdf == 1:
                # Add lesson title before  
                WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-module/div/app-form-title/mat-form-field/div/div[1]/div[3]/input"))).send_keys("ឯកសារ")
                time.sleep(1)

            #click add new either ឯកសារ or វីដេអូ
            driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li[1]/p/span[2]/button[2]").click()
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/button[2]").click()
            time.sleep(1)
            # driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-document/div/app-form-title/mat-form-field/div/div[1]/div[3]/input").send_keys(i_file)

            ##uploading doc (not drag and drop)
            #add title
            ele_title_doc = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-document/div/app-form-title/mat-form-field/div/div[1]/div[3]/input")
            ele_title_doc.send_keys(i_file.split(".")[:2][-1])
            time.sleep(1)
            ele_duc = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-document/div/div[1]/div/input")
            ele_duc.send_keys(less_path + "\\" + i_file)
            time.sleep(5)
        else:
            if i_file.endswith(".mp4") or i_file.endswith(".MP4"): # in case there are more than 2 mp4 files
                cnt_mp4 += 1
                if cnt_pdf == 0 and cnt_mp4 == 1:
                    WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-module/div/app-form-title/mat-form-field/div/div[1]/div[3]/input"))).send_keys("វីដេអូ")
                    driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li[1]/p/span[2]/button[2]").click()
                    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/button[1]").click()
                    time.sleep(1)
                if cnt_mp4 == 1 and cnt_pdf != 0:
                    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-content/h2/button"))).click()
                    time.sleep(1)
                    WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-module/div/app-form-title/mat-form-field/div/div[1]/div[3]/input"))).send_keys("វីដេអូ")
                    time.sleep(3)
                    driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[1]/ul/li[2]/p/span[2]/button[2]").click()
                    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/button[1]").click()
                    time.sleep(1)
            #uploading video
            ele_video = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-video/div/app-form-title/mat-form-field/div/div[1]/div[3]/input")
            ele_video.send_keys(i_file.split(".")[:2][-1])
            time.sleep(1)
            drop_file = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-content/div/div[2]/app-create-video/div/app-video-uploader/div/div")))
            drop_file.drop_files(less_path + "\\" + i_file)
            time.sleep(5)

            # check if the download is completed    
            check_if_complete(video_xpath)

    print("grade" + " " + grade + "_" + subject + "_" +  chap_title+ "_"+ str(datetime.now().strftime("%H:%M:%S")))

################# Setting path in local###################

#**********************************************************************************#
#                               Uncomment here for testing 
#----------------------------------------------------------------------------------#
grade = "11"
subject = "សេដ្ឋកិច្ចវិទ្យា" #copy from subject.txt
video_type = 'other' #choose either standard or other
# video_content = "សង្ខេបមេរៀន"
video_content = 'មាតិកានៃការសិក្សាតាមការបង្កើតគម្រោង'
local_path = "G:\\PBL_to_upload\\"
#**********************************************************************************

# Get intro page
get_intropage()
# for grade in [sorted(os.listdir(local_path), key=lambda v: [int(p) for p in v.split('.') if p.isdigit()])[2]]:
#     for subject in [sorted(os.listdir(local_path + grade), key=lambda v: [int(p) for p in v.split('.') if p.isdigit()])[2]]:
# Local path
#tap 2 for auto all
main_path = local_path + grade + '\\' + subject 
# first page getting list of chapters
list_chap = []
if subject == "សេដ្ឋកិច្ចវិទ្យា":
    list_file = os.listdir(main_path)[1:]
else:
    list_file = os.listdir(main_path)
for i in list_file:
    if not(i.endswith(".mp4")):
        list_chap.append(i)

# Second page getting list of videos name (For one chapter)
list_chap_title = []
list_less_title = []
list_lesson_done = []
cnt = 0
for j_chap in range(len(list_chap)):
    # driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/mat-dialog-container") is not None :
    time.sleep(5)
    ele_new = driver.find_element_by_xpath("/html/body/app-root/app-course/div/div/h1/a")
    ele_new.click() # click on creating new
    get_typevideo(video_type)
    chap_title = list_chap[j_chap].replace("\u200b", "")
    chap_title = chap_title.split("-")[-1] # for pbl video upload stucture
    less_path = main_path + "\\" + list_chap[j_chap]
    list_chap_title.append(list_chap[j_chap])

    # inserting chapter name
    ele_chap_name = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/div/div[2]/mat-form-field/div/div[1]/div[3]/input")
    ele_chap_name.send_keys(chap_title)
    time.sleep(3)

    # Second page (click next)
    ele_second = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-overview/div/form/p/button")
    ele_second.click()

    # Doc upload process
    # Drop and drag
    try:
        for i_pdf in os.listdir(less_path + "\\pdf"):
            WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-resource/div/h2/button"))).click() #create new
            WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/div/div/button[1]"))).click() #choose doc
            pdf_path = less_path + "\\pdf\\" + i_pdf
            drop_file = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-upload-file-dialog/mat-dialog-content/div")))
            drop_file.drop_files(pdf_path) #put less_path
            WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/mat-dialog-container/app-upload-file-dialog/mat-dialog-actions/button[2]"))).click()
            
            #check if things are completed
            check_if_complete(doc_xpath)
            time.sleep(5)
    except:
        pass

    # Third page (video upload section)
    ele_thrid = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-resource/div/p[2]/button[2]")))
    time.sleep(1)
    ele_thrid.click() #click next
    time.sleep(1)
    # click on + ជំពូកថ្មី
    # WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-content/h2/button"))).click() #add video

    # click add new video for each lesson
    # WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cdk-drop-list-0']/li[1]/p/span[2]/button[2]"))).click()

    # video_upload(less_path, chap_title)
    pbl_upload(less_path, chap_title)

    # next to submission 
    ele_submission = driver.find_element_by_xpath("/html/body/app-root/app-create-course/div/app-content/p/button[2]")
    ele_submission.click()
    time.sleep(1)
    
    # Go to publishing page
    ele_publish = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-create-course/div/app-preview/div/p/button[2]")))
    ele_publish.click()
    time.sleep(1)
    #confirm
    ele_confirm = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-confirm-dialog/div/mat-dialog-actions/button[2]")))
    ele_confirm.click()
    time.sleep(1)
    # Go back to first page
    ele_back = WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-success/div/h1/a")))
    ele_back.click()
    print("Done uploading for folder number: " + str(j_chap + 1) + "!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(5)

print("Done uploading for grade: " + grade + ", " + "subject: " + subject + " @ " + str(datetime.now().strftime("%H:%M:%S")))