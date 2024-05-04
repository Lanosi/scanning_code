from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDTextButton
from kivymd.icon_definitions import md_icons
from kivymd.icon_definitions import md_icons
from kivy.uix.image import Image
import time

from kivy.core.window import Window

import cv2
#2040000788063 - норм
#Window.size = (600, 700)

class Tab(MDFloatLayout, MDTabsBase):
    pass

class MainApp(MDApp):

    def build(self):
        #self.icon = 'icon.jpg'
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")

    def on_start(self):
        pass

    def treatment_data(self,code_prodict):
        ch1 = 0
        ch2 = 0
        try:
            if type(int(code_prodict)) == int:
                for i in range(1,len(code_prodict),2):
                    ch1 += int(code_prodict[i])
                ch1 = ch1 * 3
                for i in range(2, len(code_prodict)-1, 2):
                    ch2 += int(code_prodict[i])
                ch2 += int(code_prodict[0])
                ch3 = str(10 - int(str(ch1 + ch2)[1:]))
                if ch3 == code_prodict[-1]:
                    print("Все хорошо, вроде не подделка")
                    self.root.ids.label_state.text = "Все норм"
                    self.root.ids.label_state.text_color = "4ff054"
                else:
                    print("Подделка", code_prodict)
                    self.root.ids.label_state.text = "Подделка"
                    self.root.ids.label_state.text_color = "fc9090"

        except ValueError:
            print("Введите 13значный штирих код")
            self.root.ids.label_state.text = "Введите 13 значный штирих код"
            self.root.ids.label_state.text_color = "524ff0"


        if len(code_prodict) != 13:
            self.root.ids.label_state.text = "Введите 13 значный штирих код"
            self.root.ids.label_state.text_color = "524ff0"

    def print_anime(self):
        img = cv2.imread("myimage_20240415_185423.png")

        cv2.imshow("Result", img)

        cv2.waitKey(0)






MainApp().run()
