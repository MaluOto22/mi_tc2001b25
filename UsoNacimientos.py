import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import webbrowser as wb

def CreateFrame2():
    boton4 = sg.Button('Edad madre', key='BUTTON4')
    boton5 = sg.Button('Edad padre',key='BUTTON5')
    layout =[[boton4],[boton5]]
    frame2 =sg.Frame('Uso del frame 2',layout,key='FRAME2',visible= False,size=(250,250),background_color='cyan')
    return frame2

def CreateFrame():
    boton2 = sg.Button('Correlación edad gestacional vs peso',key='BUTTON2')
    boton3 = sg.Button('Estadísticas del peso', key='BUTTON3')
    multi1 = sg.Multiline(size=(30,10),key='MULTI1')
    boton6 = sg.Button('Ir a pantalla 2', key='BUTTON6')
    layout=[[boton3],[multi1],[boton2],[boton6]]
    frame=sg.Frame('Varios Elementos',layout,key='FRAME1',size=(400,400),background_color='magenta')
    return frame

def grafica(): 
    df['SEXO'].value_counts().plot(kind='pie',autopct='%0.2f%%')
    plt.show()

#programa principal
frame1 = CreateFrame()
frame2 = CreateFrame2()
layout = [[frame1,frame2]]
window = sg.Window('Window Title',layout,size=(800,700))    
df = pd.read_csv('MuestraNacimientos23.csv')
texto=df['PESO'].describe()
print(texto)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'BUTTON2':
       plt.scatter(df['EDADGESTACIONAL'],df['PESO'],color="navy")
       plt.title("Semanas de gestación vs Peso")
       plt.xlabel("Semanas")
       plt.ylabel("Gramos")
       plt.show()
    if event == 'BUTTON3':
        window['MULTI1'].update(texto)
    if event == 'BUTTON4':
        plt.hist(df['EDAD'],bins=20,edgecolor='black',color='pink')
        plt.title('Edad de la madre')
        plt.show()
    if event == 'BUTTON5':
        plt.hist(df['EDADPADRE'],bins=20,edgecolor='black',color='blue')
        plt.title('Edad del padre')
        plt.show()
    if event == 'BUTTON6':
        window['FRAME1'].update(visible=False)
        window['FRAME2'].update(visible=True)
  
window.close()
    
    
