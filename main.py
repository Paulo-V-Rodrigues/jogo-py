from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (360, 640)  # Tamanho de simulação para celular

class MenuScreen(Screen):
    pass

class JogoScreen(Screen):
    pass

class ConfigScreen(Screen):
    pass

class LojaScreen(Screen):
    pass

class SkinsScreen(Screen):
    pass

class MeuJogoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(JogoScreen(name='jogo'))
        sm.add_widget(ConfigScreen(name='config'))
        sm.add_widget(LojaScreen(name='loja'))
        sm.add_widget(SkinsScreen(name='skins'))
        return sm

if __name__ == '__main__':
    MeuJogoApp().run()