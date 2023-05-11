from positions import *
from PIL import Image, ImageFont, ImageDraw
import random

import pandas as pd
from datetime import datetime

def divide_into_days(birth_day, birth_month):
    if birth_day < 10:
        birth_day1 = 0
        
        birth_day2 = birth_day

    elif birth_day <20:
        birth_day1 = 1
        birth_day2 = list(str(birth_day))[1]

    elif birth_day <30:
        birth_day1 = 2
        birth_day2 = list(str(birth_day))[1]

    elif birth_day <32:
        birth_day1 = 3
        birth_day2 = list(str(birth_day))[1]

    if birth_month <10:
        birth_month1 = 0
        birth_month2 = list(str(birth_month))[0]

    else:
        birth_month1 =1 
        birth_month2 = list(str(birth_month))[1]

    return birth_day1,birth_day2,birth_month1,birth_month2


def print_to_image(excel_path):
    df1 = pd.read_excel(excel_path, "TEMPLATESHEET", skiprows =5, nrows =2000, usecols = "A:Z",na_filter=False)
    
    list_of_images =[]
    for index, row in df1.iterrows():
        print("Printing for ApplicantName",str(row["Applicant Name"]))
        print("ADMIN",str(row["ADMN"]).strip())
        print(str(row["Applicant Name"]).strip())
        print(str(row["Fathername"]).strip())
        print(str(row["Course"]))
        print(str(row["Start_Year"]))
        print(str(row["End_Year"]))
        date_of_joining = row["Date Of Joining"].date()
        new_image = Image.open("recpt.jpg")
        birth_date= row["Date Of Birth"]
        elob_birth_date = birth_date.strftime("%B %d, %Y")
        birth_month = birth_date.month
        birth_day = birth_date.day
        birth_year = birth_date.year
        birth_day1, birth_day2, birth_month1, birth_month2 = divide_into_days(birth_day,birth_month)
        birth_year1, birth_year2, birth_year3, birth_year4  = str(birth_year)[0],str(birth_year)[1],str(birth_year)[2],str(birth_year)[3]

        image_editable = ImageDraw.Draw(new_image)
        image_editable.text(pos_admission_n, str(row["ADMN"]).strip(), color_t, font=title_font)
        image_editable.text(pos_admission_date, str(date_of_joining).strip(), color_t, font=title_font)
        image_editable.text(pos_student_name, str(row["Applicant Name"]).strip(), color_t, font= title_font)
        image_editable.text(pos_father_name, str(row["Fathername"]).strip(), color_t, font= title_font)
        image_editable.text(pos_group, str(row["Course"]),color_t, font=title_font)
        image_editable.text(pos_studied_from,str(row["Start_Year"]), color_t, font=title_font)
        image_editable.text(pos_studied_to,str(row["End_Year"]), color_t, font=title_font)
        image_editable.text(pos_dob_day_1,str(birth_day1), color_t, font=title_font)
        image_editable.text(pos_dob_day_2,str(birth_day2), color_t, font=title_font)
        image_editable.text(pos_dob_mon_1,str(birth_month1), color_t, font=title_font)
        image_editable.text(pos_dob_mon_2,str(birth_month2), color_t, font=title_font)
        image_editable.text(pos_dob_year_1,str(birth_year1), color_t, font=title_font)
        image_editable.text(pos_dob_year_2,str(birth_year2), color_t, font=title_font)
        image_editable.text(pos_dob_year_3,str(birth_year3), color_t, font=title_font)            
        image_editable.text(pos_dob_year_4,str(birth_year4), color_t, font=title_font)
        image_editable.text(pos_dob_string,str(elob_birth_date), color_t, font=title_font)
        image_editable.text(pos_conduct,str(random.choice(["GOOD","SATISFACTORY"])),color_t,font=title_font)       
        new_image_name = str(row["ADMN"]).strip()+".png"
        new_image.save(new_image_name)
        list_of_images.append(new_image_name)

    
    new_list_images=[]
    for i in list_of_images:
        image_i = Image.open(i)
        new_list_images.append(image_i)
    
    im_obj = Image.open("recpt.jpg")
    im_obj.save("reciepts.pdf",save_all=True,append_images=new_list_images)


excel_path = "ADMNREGISTER_dummy.xlsx"
print_to_image(excel_path)


