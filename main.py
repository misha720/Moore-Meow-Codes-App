'''
	Мур Мяу кодировка v2.0
	Графическое окружение
'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from mmc import Convert

Window.clearcolor = (59/255, 58/255, 59/255, 1)
Window.title = "Мур Мяу Кодировка"

class Main(App):
	def __init__(self, path):
		super(Main,self).__init__()
		self.engine = Convert() # Подключение Конвертера
		self.key_path = self.engine.read_key(path) # Подключение ключа шифрования

		self.mmc_text_textbox = Label(text='Текст',
			font_size=20,
			size_hint=(1, .2))
		self.mmc_text_inputbox = TextInput(hint_text='Введите кодируемый текст', 
			multiline=True, 
			padding_x=20,
			padding_y=20)

		self.mmc_code_textbox = Label(text='Код',
			font_size=20,
			size_hint=(1, .2))
		self.mmc_code_inputbox = TextInput(hint_text='Введите раскодируемый код', 
			multiline=True, 
			padding_x=20,
			padding_y=20)

		self.mmc_text_inputbox.bind(text=self.on_mmc_text)
		self.mmc_code_inputbox.bind(text=self.on_mmc_code)
	
	def on_mmc_text(self, instance, value):
		data = self.mmc_text_inputbox.text
		if data != "":
			self.mmc_code_inputbox.text = self.engine.encode(data)

	def on_mmc_code(self, instance, value):
		data = self.mmc_code_inputbox.text
		if data != "":
			self.mmc_text_inputbox.text = self.engine.decode(data)

	def build(self):
		box = BoxLayout(orientation='vertical', padding=[10,0,10,10])

		box.add_widget(self.mmc_text_textbox)
		box.add_widget(self.mmc_text_inputbox)

		box.add_widget(self.mmc_code_textbox)
		box.add_widget(self.mmc_code_inputbox)

		return box

#	RUN
if __name__ == '__main__':
    app = Main(path="config.json")
    app.run()