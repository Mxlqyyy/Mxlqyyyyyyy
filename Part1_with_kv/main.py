from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Osnova(Screen):
        ...

class Saww(Screen):
    def __init__(self, **kwargs):
        super(Saww, self).__init__(**kwargs)
    def login(self, username, password):
        if username == "Дима" or "дима" and password == "1234":
            self.manager.get_screen('user_info').set_user_info(username)
            self.manager.current = 'user_info'
        else:
            print("Данные введены неверно!")

class UserInfo(Screen):
    def set_user_info(self, username):
        
        #ids это словарь который содержит ссылки на виджеты (из NextLevel.kv) и позволяет обращаться к виджетам по их идентификаторам.
        self.ids.user_info_label.text = "Привет!, " + username + "!" 
        
class NextLevel(App):
    def build(self):
        ww = ScreenManager()
        ww.add_widget(Saww(name='saww'))
        ww.add_widget(Osnova(name='osnova'))
        ww.add_widget(UserInfo(name='user_info'))
    
        return ww


if __name__ == "__main__":
    NextLevel().run()
