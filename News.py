from typing import List
from kivy.app import App
from kivy.uix.behaviors import button 
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import ListProperty
from kivy.properties import ObjectProperty

import logging
import random

from NextCloudNewsAPI.api import NextcloudNewsApi

# class ScatterTextWidget(BoxLayout):

#     text_color = ListProperty([1,0,0,1])

#     def add_text(self):
#         logging.info("add_text")
#         root = self.ids['float']
#         root.add_widget(Label(text="Test",color=self.text_color))
    
#     def change_label_color(self, *args):
#         color = [random.random() for i in range(3)] +[1]
#         self.text_color = color

class SettingsScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class LoginScreen(Screen):
    
    def login(self):

        url_input = self.ids['url_input']
        username_input = self.ids['username_input']
        password_input = self.ids['password_input']

        url = url_input.text
        username = username_input.text
        password = password_input.text

        logging.info("NewsApp: url = " + url + " Username: " + username)
        


class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class NewsApp(App):
    def build(self):   
        return Manager()

if __name__ == "__main__":
    logging.basicConfig(filename='News.log', encoding='utf-8', level=logging.DEBUG)
    NewsApp().run()
