import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt

def CreateFrame():
    boton1 = sg.Button('Estadísticas sobre edad', key='BUTTON1',button_color=('pink','blue'),font=("Helvetica", 16))
    boton2 = sg.Button('Grafica de Clase', key='BUTTON2',button_color=('red','cyan'))
    boton3 = sg.Button('Recuperar dato', key='BUTTON3')
    texto1 = sg.Text('Ingresa el dato: ', key='TEXT1',size=(10,1)) #Etiqueta, label
    entrada1 = sg.Input('',key='INPUT1',size=(10,None))
    opciones1 = ('Manzanas','Peras','Uvas','Naranjas')
    combo1 = sg.Combo(opciones1, key='COMBO1',default_value='Frutas')
    multi1 = sg.Multiline(size=(25,10),key='MULTI1')
    
    layout=[[texto1,entrada1],[boton1],[boton2,boton3,combo1],[multi1]]
    frame=sg.Frame('Varios Elementos',layout,key='FRAME1',size=(500,550),background_color='magenta')
    return frame

def grafica(): 
    df['Pclass'].value_counts().plot(kind='pie',autopct = '%0.2f')
    plt.title('Distribución de pasajeros del Titanic')
    plt.show()
    
def graficaHistograma():
    plt.hist(df['Age'],bins=15,color="red")
    plt.title('Edad de pasajeros del Titanic')
    plt.show()

#programa principal
frame1 = CreateFrame()
layout = [[frame1]]
window = sg.Window('Window Title',layout,size=(600,600))    
df = pd.read_csv('trainLimpio.csv')

print(df)
texto=df['Age'].describe()
print(df['Sex'].describe())
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'BUTTON1':
        '''
        name = values['INPUT1']   #nombre
        ap = values['INPUT2']
        age = int(value['INPUT3'])
        if age >=18:
            print(f"Buenas tardes {name} {ap}, debido a que tienes {age} años eres mayor de edad")
        else:    
            print(f"Buenas tardes {name} {ap}, debido a que tienes {age} años eres menor de edad")
        '''
        print('Hello!')
        window['MULTI1'].update(texto)
    if event == 'BUTTON2':
        grafica()
    elif event == 'BUTTON3':
        print('Hallo!')
        graficaHistograma()
        var = int(values['INPUT1'])
        print(var)
        if var>18:
            print("Mayor de edad")
        else:
            print("Menor de edad")
window.close()
    
    
