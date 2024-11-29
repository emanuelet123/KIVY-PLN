########################################################################################################################
#######################################   IMPORTS AND GLOBAL VARIABLES   ###############################################
########################################################################################################################
from kivy import require
# Kivy version used in this project
require("2.3.0")

from kivy.utils import platform

from kivy.core.window import Window
if platform == "linux":
    Window.size = (360, 640)

# Keyboard animation when TextInput focus = True
Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}

# Bring the keyboard below TextInput when focus = True
Window.softinput_mode = "below_target"
########################################################################################################################
# Interface imports
from kivy.network.urlrequest import UrlRequest
from kivymd.toast import toast
from kivy.uix.anchorlayout import AnchorLayout
from kivy_garden.mapview import MapMarker
from kivy.uix.textinput import TextInput
from kivymd.uix.widget import MDWidget
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ListProperty, DictProperty
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivy.metrics import dp, sp


########################################################################################################################
################################################   MAIN SCREEN   #######################################################
########################################################################################################################
class MAIN(MDScreen):
    def go_to(self):
        """
        Change screen if if has data
        """
        # Verify which screen should it go
        if app.go_to == "App":
            # Go to App
            app.set_current_screen("ChoiceFIRST")
        elif app.go_to == "Login":
            # Go to Login
            app.set_current_screen("LoginScreen")
    
    def print_something(self):
        app.set_current_screen("MAIN2")

    def on_pre_enter(self):
        print("1")
    
    def on_enter(self):
        print("2")
    
    def on_pre_leave(self):
        print("3")
    
    def on_leave(self):
        print("4")


class MAIN2(MDScreen):
    def go_to(self):
        """
        Change screen if if has data
        """
        # Verify which screen should it go
        if app.go_to == "App":
            # Go to App
            app.set_current_screen("ChoiceFIRST")
        elif app.go_to == "Login":
            # Go to Login
            app.set_current_screen("LoginScreen")
    
    def print_something(self):
        app.set_current_screen("MAIN")

    def on_pre_enter(self):
        print("1")
    
    def on_enter(self):
        print("2")
    
    def on_pre_leave(self):
        print("3")
    
    def on_leave(self):
        print("4")
########################################################################################################################
################################################   OTHER WIDGETS   #####################################################
########################################################################################################################
class TestButton2(MDRectangleFlatButton):
    def print_something(self):
        print("Cliquei 2")


########################################################################################################################
##################################################   MAIN APP   ########################################################
########################################################################################################################
class MyApp(MDApp):
    """
    Main Kivy/KivyMD App
    """
    # ------------------------------------------------------------------------------------------------------------SYSTEM
    key = ""
    device_ID = ""
    window_width = 0
    window_height = 0
    keyboard_height = 0
    screens = {"MAIN": MAIN, "MAIN2": MAIN2}

    # -------------------------------------------------------------------------------------------------------WINDOW SIZE
    def get_window_size(self):
        """
        Get the window size (width and height)
        1 dp == 1.25 pt
        1 pt == 0.8 dp
        """
        self.window_width = Window.width
        self.window_height = Window.height

    # ------------------------------------------------------------------------------------------------MOBILE BACK BUTTON
    def key_input(self, window, key, scancode, codepoint, modifier):
        """
        What the App will do when some key is pressed on the keyboard

        *OBS
        return True - does nothing, but what is before it
        return False - have the default back button functionality (pauses the app)
        """
        # --------------------------------------------------------------------------------------------------------------
        # print(f"KEY CODE: {key}")
        self.key = key
        # --------------------------------------------------------------------------------------------------------------
        # 3 Ways to get the current screen
        sc = self.root.current
        # sc = self.sm.current
        # sc = app.sm.current
        # --------------------------------------------------------------------------------------------------------------

        # Deal with back button action
        if key == 27:
            if sc == "TestScreen":
                return True
        else:
            return False

    # ----------------------------------------------------------------------------------------------------CHANGE SCREENS
    def set_current_screen(self, screen_name: str, switch: bool = True):
        """
        Load screen_name.kv file if necessary, and change current screen to screen_name
        """
        # Load
        self.load_screen(screen_name)
        # Change
        if switch:
            self.sm.transition = FadeTransition(duration=0.2)
            self.sm.current = screen_name

    def load_screen(self, screen_name: str):
        """
        Load screen_name.kv file
        """
        if not self.sm.has_screen(screen_name):
            Builder.load_file(f"KVFiles/Screens/{screen_name}.kv")
            self.sm.add_widget(self.screens[screen_name]())

    # --------------------------------------------------------------------------------------------------------------INIT
    def on_start(self):
        """
        What the App will do when it starts
        """
        print("App started")

    def on_stop(self):
        """
        What the App will do when it ends
        """
        print("App ended")

    def on_pause(self):
        """
        What the App will do when it pauses
        """
        print("App paused")
        return True

    def on_resume(self):
        """
        What the App will do when it comes back from pause
        """
        print("App resumed")

    def build(self):
        """
        App building configuration
        """
        # Track key input
        Window.bind(on_keyboard=self.key_input)

        # Initialize the Screen Manager
        self.sm = MDScreenManager()

        # Call the first screen to be shown
        self.set_current_screen("MAIN")

        # Return Screen Manager
        return self.sm


########################################################################################################################
####################################################   RUN   ###########################################################
########################################################################################################################
if __name__ == "__main__":
    app = MyApp()
    app.run()