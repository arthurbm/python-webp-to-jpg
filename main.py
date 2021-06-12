from PIL import Image
import PySimpleGUI as sg
import os

def pedir_arquivos(num_files):
    layout = [  [sg.Text('Caminhos dos arquivos')]] 

    list_filepath_send = []
    for x in range(0,num_files):
        layout.append([sg.Input(), sg.FileBrowse()])
    
    layout.append([sg.OK(), sg.Cancel()])

    window = sg.Window('Arquivos', layout)

    event, values = window.read()
    for y in range(0,num_files):
        list_filepath_send.append(values[y])

    window.close()

    return list_filepath_send

def pedir_varios_arquivos():
    event, values = sg.Window('Window Title').Layout([[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]]).Read()

    list_send = values['_FILES_'].split(';')
    print(list_send)

    return list_send

def listToString(s):  
    
    # initialize an empty string 
    str1 = "/" 
    
    # return string   
    return (str1.join(s))

list_files = pedir_varios_arquivos()



for file_img in list_files:
    img = Image.open(file_img).convert("RGB")
    file_img_name = file_img[:-5]
    file_img_name_list = file_img_name.split('/')
    file_img_name_list.insert(-1,'ifoodCM')
    file_img_name = listToString(file_img_name_list)
    img.save(f"{file_img_name}.jpg", "jpeg")
    print(f"Converti o arquivo {((file_img_name.split('/')[-1]))}")
