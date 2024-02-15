from Kivy import App
from Kivy.uix.button import Button

# Trabalhando com Kivy para interfaçe grafica 

class ExemploApp(App):
    def build(self):
        return Button(text = "Olá Mundo!")