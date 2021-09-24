from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout

Window.size = (400, 800)

Config.set('kivy', 'keyboard_mode', 'systemanddock')

class Main_menu(Screen):
    def change_text(self):
        pass

def get_ingridients_menu1(sht_ingr_menu1):
    menu1_ingr1 = str(round(sht_ingr_menu1 * 0.058, 2))
    menu1_ingr2 = str(round(sht_ingr_menu1 * 0.042, 2))
    menu1_ingr3 = str(round(sht_ingr_menu1 * 0.018, 2))

    return {'menu1_ingr1': menu1_ingr1,
            'menu1_ingr2': menu1_ingr2,
            'menu1_ingr3': menu1_ingr3
            }

def get_ingridients_menu2(sht_ingr_menu2):
    menu2_ingr1 = str(round(sht_ingr_menu2 * 0.048, 2))
    menu2_ingr2 = str(round(sht_ingr_menu2 * 0.032, 2))
    menu2_ingr3 = str(round(sht_ingr_menu2 * 0.014, 2))

    return {'menu2_ingr1': menu2_ingr1,
            'menu2_ingr2': menu2_ingr2,
            'menu2_ingr3': menu2_ingr3
            }

def get_ingridients_menu3(sht_ingr_menu3):
    menu3_ingr1 = str(round(sht_ingr_menu3 * 0.04, 2))
    menu3_ingr2 = str(round(sht_ingr_menu3 * 0.005, 2))
    menu3_ingr3 = str(round(sht_ingr_menu3 * 0.005, 2))

    return {'menu3_ingr1': menu3_ingr1,
            'menu3_ingr2': menu3_ingr2,
            'menu3_ingr3': menu3_ingr3
            }

def get_ingridients_menu4(sht_ingr_menu4):
    menu4_ingr1 = str(round(sht_ingr_menu4 * 0.09, 2))
    menu4_ingr2 = str(round(sht_ingr_menu4 * 1, 2))

    return {'menu4_ingr1': menu4_ingr1,
            'menu4_ingr2': menu4_ingr2
            }

def get_ingridients_menu5(sht_ingr_menu5):
    menu5_ingr1 = str(round(sht_ingr_menu5 * 1, 2))
    menu5_ingr2 = str(round(sht_ingr_menu5 * 0.12, 2))
    menu5_ingr3 = str(round(sht_ingr_menu5 * 1, 2))
    menu5_ingr4 = str(round(sht_ingr_menu5 * 8, 2))

    return {'menu5_ingr1': menu5_ingr1,
            'menu5_ingr2': menu5_ingr2,
            'menu5_ingr3': menu5_ingr3,
            'menu5_ingr4': menu5_ingr4
            }

def get_ingridients_menu6(sht_ingr_menu6):
    menu6_ingr1 = str(round(sht_ingr_menu6 * 0.044, 2))
    menu6_ingr2 = str(round(sht_ingr_menu6 * 0.044, 2))

    return {'menu6_ingr1': menu6_ingr1,
            'menu6_ingr2': menu6_ingr2
            }

def get_ingridients_menu7(sht_ingr_menu7):
    menu7_ingr1 = str(round(sht_ingr_menu7 * 1, 2))
    menu7_ingr2 = str(round(sht_ingr_menu7 * 0.65, 2))
    menu7_ingr3 = str(round(sht_ingr_menu7 * 0.35, 2))
    menu7_ingr4 = str(round(sht_ingr_menu7 * 15, 2))
    menu7_ingr5 = str(round(sht_ingr_menu7 * 2, 2))
    menu7_ingr6 = str(round(sht_ingr_menu7 * 5, 2))

    return {'menu7_ingr1': menu7_ingr1,
            'menu7_ingr2': menu7_ingr2,
            'menu7_ingr3': menu7_ingr3,
            'menu7_ingr4': menu7_ingr4,
            'menu7_ingr5': menu7_ingr5,
            'menu7_ingr6': menu7_ingr6
            }


class Menu1(Screen):
    def calc_menu1(self):
        try:
            kol_ingr_menu1 = int(self.menu1_input.text)
        except:
            kol_ingr_menu1 = 0

        ingridients_menu1 = get_ingridients_menu1(kol_ingr_menu1)

        self.menu1_ingr1.text = ingridients_menu1.get('menu1_ingr1') + ' Кг'
        self.menu1_ingr2.text = ingridients_menu1.get('menu1_ingr2') + ' Кг'
        self.menu1_ingr3.text = ingridients_menu1.get('menu1_ingr3') + ' Кг'
    pass

class Menu2(Screen):
    def calc_menu2(self):
        try:
            kol_ingr_menu2 = int(self.menu2_input.text)
        except:
            kol_ingr_menu2 = 0

        ingridients_menu2 = get_ingridients_menu2(kol_ingr_menu2)

        self.menu2_ingr1.text = ingridients_menu2.get('menu2_ingr1') + ' Кг'
        self.menu2_ingr2.text = ingridients_menu2.get('menu2_ingr2') + ' Кг'
        self.menu2_ingr3.text = ingridients_menu2.get('menu2_ingr3') + ' Кг'
    pass

class Menu3(Screen):
    def calc_menu3(self):
        try:
            kol_ingr_menu3 = int(self.menu3_input.text)
        except:
            kol_ingr_menu3 = 0

        ingridients_menu3 = get_ingridients_menu3(kol_ingr_menu3)

        self.menu3_ingr1.text = ingridients_menu3.get('menu3_ingr1') + ' Кг'
        self.menu3_ingr2.text = ingridients_menu3.get('menu3_ingr2') + ' Кг'
        self.menu3_ingr3.text = ingridients_menu3.get('menu3_ingr3') + ' Кг'
    pass

class Menu4(Screen):
    def calc_menu4(self):
        try:
            kol_ingr_menu4 = int(self.menu4_input.text)
        except:
            kol_ingr_menu4 = 0

        ingridients_menu4 = get_ingridients_menu4(kol_ingr_menu4)

        self.menu4_ingr1.text = ingridients_menu4.get('menu4_ingr1') + ' Кг'
        self.menu4_ingr2.text = ingridients_menu4.get('menu4_ingr2') + ' Гр'
    pass

class Menu5(Screen):
    def calc_menu5(self):
        try:
            kol_ingr_menu5 = int(self.menu5_input.text)
        except:
            kol_ingr_menu5 = 0

        ingridients_menu5 = get_ingridients_menu5(kol_ingr_menu5)

        self.menu5_ingr1.text = ingridients_menu5.get('menu5_ingr1') + ' Кг'
        self.menu5_ingr2.text = ingridients_menu5.get('menu5_ingr2') + ' Кг'
        self.menu5_ingr3.text = ingridients_menu5.get('menu5_ingr3') + ' Гр'
        self.menu5_ingr4.text = ingridients_menu5.get('menu5_ingr4') + ' Гр'
    pass

class Menu6(Screen):
    def calc_menu6(self):
        try:
            kol_ingr_menu6 = int(self.menu6_input.text)
        except:
            kol_ingr_menu6 = 0

        ingridients_menu6 = get_ingridients_menu6(kol_ingr_menu6)

        self.menu6_ingr1.text = ingridients_menu6.get('menu6_ingr1') + ' Кг'
        self.menu6_ingr2.text = ingridients_menu6.get('menu6_ingr2') + ' Кг'
    pass

class Menu7(Screen):
    def calc_menu7(self):
        try:
            kol_ingr_menu7 = int(self.menu7_input.text)
        except:
            kol_ingr_menu7 = 0

        ingridients_menu7 = get_ingridients_menu7(kol_ingr_menu7)

        self.menu7_ingr1.text = ingridients_menu7.get('menu7_ingr1') + ' Кг'
        self.menu7_ingr2.text = ingridients_menu7.get('menu7_ingr2') + ' Кг'
        self.menu7_ingr3.text = ingridients_menu7.get('menu7_ingr3') + ' Кг'
        self.menu7_ingr4.text = ingridients_menu7.get('menu7_ingr4') + ' Гр'
        self.menu7_ingr5.text = ingridients_menu7.get('menu7_ingr5') + ' Гр'
        self.menu7_ingr6.text = ingridients_menu7.get('menu7_ingr6') + ' Гр'
    pass


class TestApp(App):
    pass

if __name__ == '__main__':
    TestApp().run()