#!/usr/bin/env python
import PySimpleGUI as sg
import cv2
import numpy as np
import PIL
from PIL import Image,ImageTk


"""
Demo program that displays a webcam using OpenCV
"""


def main():

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image', visible=True)],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14') ]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(0, 0))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    recording = False

    while True:
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Record':
            recording = True

        elif event == 'Stop':
            recording = False
            img=np.zeros((480, 640, 3), np.uint8)
            img = PIL.Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            # this is faster, shorter and needs less includes
            window['image'].update(data=imgtk)

        if recording:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = PIL.Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            window.FindElement('image').Update(data=imgtk)
            #cv2.imshow('img', frame)
    cap.release()
    #cv2.destroyAllWindows()


main()