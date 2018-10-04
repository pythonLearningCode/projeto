from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
	pass


class Menu(Screen):
	pass 


class Sala(Screen):
	pass


class Aplicativo(App):

	def onOff(self, lab):
	def build(self):
		return Gerenciador()


if __name__ == '__main__':
	Aplicativo().run()
