import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import webbrowser as wb

def CreateFrame2():
    texto1 = sg.Text('Ingresa un precio: ',key='TEXTO1',size=(20,1))
    input1 = sg.Input('',key = 'INPUT1')
    boton4 = sg.Button('Calcular IVA', key='BUTTON4')
    boton5 = sg.Button('Regresar',key='BUTTON5')
    layout =[[texto1,input1],[boton4],[boton5]]
    frame2 =sg.Frame('Uso del frame 2',layout,key='FRAME2',visible= False,size=(250,250),background_color='cyan')
    return frame2

def CreateFrame():
    boton2 = sg.Button('Mapa',key='BUTTON2')
    boton3 = sg.Button('Ir a frame 2', key='BUTTON3')
    texto1 = sg.Text('Ingresa el dato: ', key='TEXT1',size=(10,1)) #Etiqueta, label
    entrada1 = sg.Input('',key='INPUT1',size=(10,None))
    multi1 = sg.Multiline(size=(20,5),key='MULTI1')
    layout=[[texto1,entrada1],[boton3],[multi1,boton2]]
    frame=sg.Frame('Varios Elementos',layout,key='FRAME1',size=(300,250),background_color='magenta')
    return frame

def grafica(): 
    df['Pclass'].value_counts().plot(kind='pie')
    plt.show()

#programa principal
frame1 = CreateFrame()
frame2 = CreateFrame2()
layout = [[frame1,frame2]]
window = sg.Window('Window Title',layout,size=(800,700))    
df = pd.read_csv('trainLimpio.csv')
texto=df['Age'].describe()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event== 'BUTTON2':
        buscar ="Farmacias"
        url_mapa = f'https://www.google.com/maps/search/{buscar}'
        wb.open_new_tab(url_mapa)
    if event == 'BUTTON3':
        window['FRAME1'].update(visible=False)
        window['FRAME2'].update(visible=True)
    if event == 'BUTTON5':
        window['FRAME1'].update(visible=True)
        window['FRAME2'].update(visible=False)
    if event == 'BUTTON4':
        print("El IVA es el 16% ")
  
window.close()
    
    
