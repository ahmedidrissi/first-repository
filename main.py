from distutils.command.config import config
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

Builder.load_file('main.kv')

class MyLayout(Widget):
	def remove(self):
		prior = self.ids.calc_input.text
		if prior == 'Error':
			self.ids.calc_input.text = '0'
		elif prior != '0':
			prior = prior[:-1]
			if prior == '':
				self.ids.calc_input.text = '0'
			else:
				self.ids.calc_input.text = prior

	def clear(self):
		self.ids.calc_input.text = '0'

	def pos_neg(self):
		prior = self.ids.calc_input.text
		if prior != '0':
			if prior[0] != '-':
				self.ids.calc_input.text = f'-{prior}'
			else:
				self.ids.calc_input.text = prior[1:]
		else:
			self.ids.calc_input.text = '-'

	def button_press(self, button):
		prior = self.ids.calc_input.text

		if "Error" in prior:
			prior = ''

		if prior == '0':
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	def math_sign(self, sign):
		prior = self.ids.calc_input.text
		self.ids.calc_input.text = f'{prior}{sign}'

	def dot(self):
		prior = self.ids.calc_input.text
		num_list = prior.split("+")

		if '+' in prior and '.' not in num_list[-1]:
			self.ids.calc_input.text = f'{prior}.'
		elif '.' in prior:
			pass
		else:
			self.ids.calc_input.text = f'{prior}.'

	def equals(self):
		prior = self.ids.calc_input.text

		try:
			answer = eval(prior)
			self.ids.calc_input.text = str(answer)

		except:
			self.ids.calc_input.text = "Error"

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()