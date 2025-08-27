import PySimpleGUI as sg

def CreateFrame():
    b1 = sg.Button('Da click aquí!', key='BUTTON1',button_color=('yellow','magenta'))
    b2 = sg.Button('Otro botón',key='BUTTON2',button_color=('red','pink'))
    texto1 = sg.Text('Introduce la contraseña: ', key='TEXT1',size=(20,1)) 
    entrada1 = sg.Input('',key='INPUT1',size=(10,None))
    layout=[[b1],[b2],[texto1,entrada1]]
    frame=sg.Frame('Probando',layout,key='FRAME1',size=(600,150),background_color="cyan")
    return frame

frame1 = CreateFrame()
layout = [[frame1]]
window = sg.Window('Diabetes y enfermedades crónicas en México',layout,size=(715, 200))    
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'BUTTON1':    #diste click en el boton1
        print('Hello')
   
window.close()