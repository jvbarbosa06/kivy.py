from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        
        return AsyncImage(source='https://m.media-amazon.com/images/I/61yRoVRYHnL._AC_UF894,1000_QL80_DpWeblab_.jpg')
    
if __name__ == "__main__":
    MinhaApp().run()
    