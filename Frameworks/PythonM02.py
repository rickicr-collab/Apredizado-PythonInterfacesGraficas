from flexx import flx

# realizandoo teste para a instalaçao do flexx

class Exemplo(flx.Widget):
    
    def init(self):
        flx.Button(text = 'Olá')
        flx.Button(text = 'Mundo!')

if __name__ == '__main__':
    a = flx.App(Exemplo, Title = 'flexx Demonstração')
    m = a.launch()
    flx.run()