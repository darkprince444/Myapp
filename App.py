from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

DARK="""
Manage:
    FirstScreen: 
    SecondScreen:
        
<FirstScreen>:
    name: "login"
    MDIconButton:
        icon:"google"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release:
            app.root.current="home"
    MDLabel:
        text: "WATCH AND EARN"
        bold: True
        italic: True
        font_size: "60px"
        pos_hint: {'center_x':0.65,'center_y':0.85}
    MDLabel:
        text: "WELCOME TO MY APP"
        bold: True
        italic: True
        font_size: "60px"
        pos_hint: {'center_x':0.6,'center_y':0.9}


<SecondScreen>:
    name: "home"
    MDFlatButton:
        text: "WATCH ADS"
        theme_text_color:"Error"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.5,0.1)
        
    MDFlatButton:
        text: "withdraw"
        pos_hint: {'center_x':0.89,'center_y':0.94}
    MDIconButton:
        icon:"account"
        pos_hint: {'center_x':0.1,'center_y':0.94}
"""
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class Manage(ScreenManager):
    pass
class MyApp(MDApp):   
    def build(self):
        app=Builder.load_string(DARK)
        return app

MyApp().run()