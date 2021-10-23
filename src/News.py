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
import json

from database.database import database

from NextCloudNewsAPI.api import NextcloudNewsApi

sm = None

class SettingsScreen(Screen):
    pass

class MainScreen(Screen):

    def sync(self):
        folders = News.getFolders()
        
        for folder in folders["folders"]:
            data.addFolder(id=int(folder['id']),name=folder['name'])

class LoginScreen(Screen):
    
    def login(self):

        url_input = self.ids['url_input']
        username_input = self.ids['username_input']
        password_input = self.ids['password_input']

        url = url_input.text
        username = username_input.text
        password = password_input.text

        logging.info("NewsApp: url: " + url + " Username: " + username)

        if News.auth(nextcloudUrl=url, username=username, password=password):
            sm.current = "Main"
            
        


class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class NewsApp(App):

    def build(self):   
        global sm # God help me
        sm = Manager()
        return sm

if __name__ == "__main__":
    logging.basicConfig(filename='News.log', encoding='utf-8', level=logging.DEBUG)

    News = NextcloudNewsApi(appName="NewsApi")

    data = database()

    NewsApp().run()
