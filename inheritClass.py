class royalEnfield:
    bikeName = 'baseName'
    bikeVarients= [{
        'model': 'base',
        'price': 100
    }]
    bikeColor = 'BaseColor'

    def __init__(self,name = '',varients =[], color = ''):
        if name != '':
            self.bikeName = name
        if len(varients) != 0:
            self.bikeVarients = varients
        if color != '':
            self.bikeColor = color
        
        print(f'bike name is {self.bikeName}')
        print(f'bike color is {self.bikeColor}')
        print(f'bike varients are  {self.bikeVarients}')
    