from random import random
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Element
 
sg.theme('Darkpurple4')
def win1_layout():   
    layout = [
            [sg.Text('E-mail:'), sg.Text(size=(15, 1), key='-email-'),],
            [sg.Input(key='-input1-')],
            [sg.Text('Full Name:'), sg.Text(size=(15, 1), key='-name-'),],
            [sg.Input(key='-input2-')],
            [sg.Text('Password:')],
            [sg.Input(key='input3')],
            [sg.Button('yes'), sg.Button('No')],
            
    ]

    return layout
win1 = sg.Window('tittel på programmer1', win1_layout())


while True: # event loop
    event, values = win1.read()
    print(event, values)
    if event in(None, 'Exit'):
        break
    if event == 'show':
        # update the "output" text element to be the value of "input" element
        win1['-name-'].update(values['-input2-'])
