from kivy.app import App 
from kivy.uix.button import Button 
    
class MinhaApp(App):
    def build(self):
        return Button(text='Clique aqui', size_hint=(0.5, 0.5))

if __name__ == "__main__":
    MinhaApp().run()
    