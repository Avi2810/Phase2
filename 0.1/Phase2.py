import pandas as pd
import numpy as np
import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time
import os, shutil
import sys
from io import StringIO
from tkinter import *
from threading import Thread
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
try:
    import lxml
except:
    os.system('pip install lxml')


####################################################################################################################


this_version = 0.1
from tkinter import Tk,Button,Frame,Label
import requests, threading, time
pop = Tk()
pop.geometry("300x200")
pop.attributes('-topmost',True)
pop.eval('tk::PlaceWindow . center')
pop.overrideredirect(True)


def te():
    global avl_version
    avl_version = 0
    time.sleep(1)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    try:
        avl_version = (requests.get(url='https://raw.githubusercontent.com/Avi2810/Phase2/main/version',headers=headers, timeout=10).text).strip()
    except:
        pass
    if float(avl_version) > this_version:
        f2.pack_forget()
        f3.pack(fill='both',expand=True,padx=10,pady=10)
    else:
        pop.destroy()

def update_app():
    pop.geometry("300x100")
    pop.config(background='#404040')
    f1.pack_forget()
    f4.pack(padx=5,pady=5,fill='both',expand=True)
    import requests
    import time
    time.sleep(2)
    version = (requests.get(url='https://raw.githubusercontent.com/Avi2810/Phase2/main/version').text).strip()
    with open(f"Phase2_v{version}.py",'w') as updated_file:
        updated_file.write(requests.get(url=f'https://raw.githubusercontent.com/Avi2810/Phase2/main/{version}/Phase2.py').text)
    with open(f"Phase2.bat",'w') as bat_file:
        bat_file.write(f"python Phase2_v{version}.py")
    label.config(text='Updates Installed Successfully')
    time.sleep(3)
    os._exit(1)

f1 = Frame(pop,background='#ccc4a7')
f1.pack(fill='both',expand=True)
f2 = Frame(f1,background='#d9d9d9')
f2.pack(fill='both',expand=True,padx=10,pady=10)
Label(f2,text="Checking for Updates...",font=('Ericsson Hilda',15,'bold'),background='#d9d9d9',foreground='#4a473d').place(relx=0.5, rely=0.5,anchor=CENTER)

f3 = Frame(f1,background='#d9d9d9')
# f3.pack(fill='both',expand=True,padx=10,pady=10)
Label(f3,text='New Update Available.\nDo you want to update?',font=('Ericsson Hilda',15,'bold'),background='#d9d9d9',foreground='#4a473d').pack(pady=20)
Button(f3,text='Yes',font=(None,12),width=9,command=threading.Thread(target=update_app).start).pack(side='left',padx=25)
Button(f3,text='No',font=(None,12),width=9,command=pop.destroy).pack(side='right',padx=25)


f4 = Frame(pop)
# f4.pack(padx=5,pady=5,fill='both',expand=True)
label = Label(f4,text='Installing Updates. \nPlease wait...',font=('Ericsson Hilda',15,'bold'))
label.pack(pady=20)

pop.after_idle(threading.Thread(target=te).start)
pop.mainloop()


###################################################################################################################


circles = ['AP','KK','MP','MH','BH','KO','WB','KL','CH','DL','JK','GJ','OR','JH','AS','NE','MU','UPW','UPE','PB','RJ','HR', 'HP','TN']

global user
user = os.getenv('username')
passw = 'Protyusha@2801'          # Paste your LAN password inside quotation
auth_code_string = ''


options = webdriver.EdgeOptions()
prefs={"download.default_directory":"C:\CM Automation"}
options.add_experimental_option("prefs",prefs)
service=Service(EdgeChromiumDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()
time.sleep(1)
driver.get('https://nextgentm-in.sdt.ericsson.net/arsys/forms/umt-ars-in/SHR%3ALandingConsole/Default+Administrator+View/?cacheid=c4ed3626')



from tkinter import Tk, Button, Entry, Label, StringVar

app = Tk()
app.geometry('600x300')
app.config(background='#709179')
app.attributes('-topmost',True)
code = StringVar()
def login(x=None):
    global auth_code_string
    auth_code_string = code.get()
    print(auth_code_string)
    app.destroy()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'domain')))
    domain_bar = driver.find_element(By.ID,'domain')
    domain_bar.send_keys('Emlpyee')
    login_btn = driver.find_element(By.ID,'loginBtn')
    login_btn.click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'login')))
    login = driver.find_element(By.ID,'login')
    login.send_keys(user)
    passwd = driver.find_element(By.ID,'passwd')
    passwd.send_keys(passw)
    login_btn = driver.find_element(By.ID,'loginBtn')
    login_btn.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'response')))
    aut_response = driver.find_element(By.ID,'response')
    aut_response.send_keys(auth_code_string)
    submit_btn = driver.find_element(By.ID,'ns-dialogue-submit')
    submit_btn.click()
    time.sleep(3)
    alert = Alert(driver)
    try:
        alert.accept()
    except:
        pass
Label(app,text="Enter Microsoft Authentication Code",font=('Ericsson Hilda',15,'bold'),background='#709179').place(x=145,y=80)
Entry(app,font=('Ericsson Hilda',15),justify='center',textvariable=code).place(x=190,y=130)
Button(app,text='Login',font=('Ericsson Hilda',15),width=20,command=login).place(x=190,y=190)
app.bind('<Return>',login)
app.mainloop()

time.sleep(5)
while True:
    time.sleep(1)
    try:
        if driver.find_element(By.LINK_TEXT,'IT Home'):
            break
    except:
        pass

pyautogui.keyDown('ctrl')
pyautogui.press("-")
pyautogui.keyUp('ctrl')

import glob
import os.path
folder_path = 'C:\CM Automation'
file_type = '\*.xlsx'
files = glob.glob(folder_path + file_type)
file = max(files, key=os.path.getctime)
print(file)

# try:
#     shutil.rmtree("C:/CM Automation/Validated")
# except:
#     pass
try:
    os.mkdir("C:/CM Automation/Validated")
except:
    pass



def start():
    def showinfo(info):
        logs.config(state='normal')
        logs.insert('end', f'{info}\n')
        logs.see('end')
        logs.config(state='disabled')
    i = 1

    with pd.ExcelWriter(f"{folder_path}\\Validated\\"+file.rsplit('\\',1)[-1]+"_validated.xlsx") as writer: 
        for sheet in ['Expired', 'Daytime','Tonight L1, L2','Tonight L3, L4','Future L1, L2','Future L3, L4']:
            slot_data = pd.read_excel(file,sheet_name=sheet)
            df = slot_data[((slot_data['Operational Categorization Tier 1+']=='Core Config') | (slot_data['Operational Categorization Tier 1+']=='MPBN') | (slot_data['Operational Categorization Tier 1+']=='Packet Core') |(slot_data['Operational Categorization Tier 1+']=='IN Config') | (slot_data['Operational Categorization Tier 1+']=='SCM Core') | (slot_data['Operational Categorization Tier 1+']=='Infra')) & (slot_data['Signum'].str.contains(user,case=False))].loc[:]
            change_ids = list(df['Change ID*+'])
            # if len(change_ids) == 0:
            #     from tkinter import messagebox, Tk
            #     root = Tk()
            #     root.wm_attributes("-topmost", 1)
            #     root.withdraw()
            #     messagebox.showinfo("Info","No CR to validate")
            #     root.destroy()
            #     driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[1]/fieldset/div/div[2]/fieldset/a[5]').click()
            #     time.sleep(1)
            #     driver.close()
            #     driver.quit()
            #     exit()
            # else:
            #     pass
            
            for cr in change_ids:
                try:
                    showinfo("++++++++++++++++++++++++++++++++++++++++++++++++")
                    showinfo(f'{i}. {cr}')
                    i+=1
                    showinfo("")
                    driver.refresh()
                    while True:
                        time.sleep(1)
                        try:
                            if driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div/div/div[4]/div[2]/div/div/div[2]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div/div/div/div[1]/fieldset/div/div/div/div/div[2]/fieldset/div/div/div/div[4]/div[2]/div/div/div[1]/fieldset/div/div[1]/label').text == 'Show':
                                break
                        except:
                            pass
                    driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[1]/fieldset/div/div[2]/fieldset/a[1]').click()
                    time.sleep(1)
                    driver.find_element(By.LINK_TEXT,'Change Management').click()
                    driver.find_element(By.LINK_TEXT,'Search Change').click()
                    while True:
                        time.sleep(1)
                        try:
                            if driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div[1]/fieldset/div[1]/label").text == 'Change ID*+':
                                break
                        except:
                            pass
                    driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div[1]/fieldset/div[1]/textarea').send_keys(cr+Keys.ENTER)
                    while True:
                        time.sleep(1)
                        try:
                            if driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div[1]/fieldset/div[2]/textarea').get_attribute('value') != "":
                                break
                        except:
                            pass
                    time.sleep(1)
                    circle = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div[1]/fieldset/div[4]/textarea').get_attribute('value')
                    cr_class = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div[3]/fieldset/div[1]/div/input').get_attribute('value')
                    if circle not in circles:
                        showinfo("Change Location Remarks: NOK")
                        slot_data.loc[slot_data['Change ID*+']==cr,"Change Location Remarks"] = "NOK"
                    else:
                        showinfo("Change Location Remarks: OK")
                        slot_data.loc[slot_data['Change ID*+']==cr,"Change Location Remarks"] = "OK"
                        try:
                            driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[1]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div[4]/div[4]').click()
                            driver.switch_to.window(driver.window_handles[1])
                            time.sleep(1)
                            try:
                                table = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[4]/div[2]/div/div[2]/table').get_attribute('outerHTML')
                            except:
                                table = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[10]/div[2]/div/div[2]/table').get_attribute('outerHTML')
                            df = pd.read_html(StringIO(table))[0]
                            if len(df[~df['Site Group'].isna()]) > 0:
                                showinfo('Site Group Remarks: OK')
                                slot_data.loc[slot_data['Change ID*+']==cr,"Site Group Remarks"] = "OK"
                            else:
                                showinfo('Site Group Remarks: NOK')
                                slot_data.loc[slot_data['Change ID*+']==cr,"Site Group Remarks"] = "NOK"
                            driver.find_element(By.XPATH,'//div[text()="Close"]').click()
                        except:
                            driver.close()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])

                    driver.find_element(By.LINK_TEXT,'Categorization').click()
                    time.sleep(1)
                    service_affecting1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[2]/div[28]/div/input').get_attribute('value')
                    no = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[2]/div[3]/fieldset/div/span[1]/input').is_selected()
                    yes = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[2]/div[3]/fieldset/div/span[2]/input').is_selected()
                    if yes:
                        interdomain_cr_status2 = 'Yes'
                    elif no:
                        interdomain_cr_status2 = 'No'
                    driver.find_element(By.LINK_TEXT,'Relationships').click()
                    time.sleep(1)
                    table = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[4]/div[2]/div/div/div[2]/fieldset/div/div/div[2]/div/div[2]/table').get_attribute("outerHTML")
                    table = pd.read_html(StringIO(table))[0]
                    if len(table[(table['Request Type'] == 'CI Unavailability') & (table['Request Summary'].str.contains('AOT'))]) >= 1:
                        service_affecting2 = 'Yes'
                    else:
                        service_affecting2 = 'No'
                    
                    #####
                    driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[4]/div[2]/div/div/div[1]/fieldset/div/div[1]/fieldset/div[2]/a').click()
                    time.sleep(.5)
                    driver.find_element(By.XPATH,'//td[text()="Infrastructure Change"]').click()
                    table = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[4]/div[2]/div/div/div[2]/fieldset/div/div/div[2]/div/div[2]/table').get_attribute("outerHTML")
                    try:
                        table = pd.read_html(StringIO(table))[0]
                        interdomain_cr_status = 'Yes'
                    except:
                        interdomain_cr_status = 'No'

                    if cr_class == 'Emergency':
                        driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[4]/div[2]/div/div/div[1]/fieldset/div/div[1]/fieldset/div[2]/a').click()
                        time.sleep(.5)
                        driver.find_element(By.XPATH,'//td[text()="Incident"]').click()
                        table = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[4]/div[2]/div/div/div[2]/fieldset/div/div/div[2]/div/div[2]/table').get_attribute("outerHTML")
                        try:
                            table = pd.read_html(StringIO(table))[0]
                            incident_num_found = 'Yes'
                            showinfo("Emergency CR Remarks: OK")
                            slot_data.loc[slot_data['Change ID*+']==cr,"Emergency CR Remarks"] = "OK"
                        except:
                            incident_num_found = 'No'
                            showinfo("Emergency CR Remarks: NOK")
                            slot_data.loc[slot_data['Change ID*+']==cr,"Emergency CR Remarks"] = "NOK"

                    ###
                    driver.find_element(By.LINK_TEXT,'Additional Info 2').click()
                    time.sleep(1)
                    interdomain_CR = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[10]/div[5]/textarea').get_attribute('value')
                    driver.find_element(By.LINK_TEXT,'Categorization').click()
                    time.sleep(1)
                    if interdomain_cr_status == interdomain_CR == interdomain_cr_status2 == 'Yes':
                        showinfo('Interdomain Cr Remarks: OK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Interdomain Cr Remarks"] = "OK"
                    elif interdomain_cr_status == interdomain_CR == interdomain_cr_status2 == 'No':
                        showinfo('Interdomain Cr Remarks: Not Required')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Interdomain Cr Remarks"] = "Not Required"
                    else:
                        showinfo('Interdomain Cr Remarks: NOK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Interdomain Cr Remarks"] = "NOK"

                    driver.find_element(By.LINK_TEXT,'Work Detail').click()
                    time.sleep(1)
                    table = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[16]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/fieldset[1]/div[2]/div/div/div[2]/fieldset/div/div/div[2]/div/div[2]/table').get_attribute('outerHTML')
                    df = pd.read_html(StringIO(table))[0]
                    service_affecting0 = df[df['Type']=='Service Impact Assessment']['Notes'].iloc[0]
                    if 'NSA' in service_affecting0:
                        service_affecting0 = "No"
                    else:
                        if len(service_affecting0) > 5:
                            service_affecting0 = "Yes"
                        else:
                            service_affecting0 = ""
                    df = df.dropna(subset='Files')
                    if len(df[((df['Type']=='Install Plan')) & (df['Files'] > 2)]) == 0:
                        showinfo('Install Plan Remarks: OK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Install Plan Remarks"] = "OK"
                    else:
                        showinfo('Install Plan Remarks: NOK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Install Plan Remarks"] = "NOK"
                    if len(df[((df['Type']=='Backout Plan')) & (df['Files'] > 2)]) == 0:
                        showinfo('Backout Plan Remarks: OK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Backout Plan Remarks"] = "OK"
                    else:
                        showinfo('Backout Plan Remarks: NOK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Backout Plan Remarks"] = "NOK"
                    
                    if len(df[((df['Notes'].str.contains('CU')) | (df['Notes'].str.contains('Approval')) | (df['Notes'].str.contains(' Customer Approval'))) & (df['Files'] > 2)]) == 0:
                        showinfo('Customer Approval Remarks: OK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Customer Approval Remarks"] = "OK"
                    else:
                        showinfo('Customer Approval Remarks: NOK')
                        slot_data.loc[slot_data['Change ID*+']==cr,"Customer Approval Remarks"] = "NOK"
                        
                    if service_affecting0 == service_affecting1 == service_affecting2:
                        showinfo("Service Affecting Remarks: OK")
                        slot_data.loc[slot_data['Change ID*+']==cr,"Service Affecting Remarks"] = "OK"
                    else:
                        showinfo("Service Affecting Remarks: NOK")
                        slot_data.loc[slot_data['Change ID*+']==cr,"Service Affecting Remarks"] = "NOK"                
                except:
                    showinfo("Error While Execution")
            slot_data.to_excel(writer,sheet_name=sheet,index=False)
        writer.close()
        showinfo("_______________Completed________________")



root = Tk()
root.title("CM Automation Phase 2")
root.geometry('800x400')
root.wm_attributes("-topmost", 1)
frame = Frame(root,background='#545454',padx=10,pady=10)
frame.pack(fill='both',expand=True)

logs = Text(frame,background='#d4d4d4')
Scroll = Scrollbar(frame)
Scroll.configure(command=logs.yview)
logs.configure(yscrollcommand=Scroll.set,font=('Ericsson Hilda', 12))
Scroll.pack(side='right', fill='both')
logs.pack(fill='both',expand=True)
root.after(1000,Thread(target=start).start)
root.mainloop()


driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[1]/fieldset/div/div[2]/fieldset/a[5]').click()
time.sleep(1)
driver.close()
driver.quit()
