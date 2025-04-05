class royalEnfield:
    bikeName = 'baseName'
    bikeColor = 'BaseColor'
    bikeVarients= [
        {
        'model': 'classic350',
        'price': 100,
        'varient': 'blue'
        },
        {
        'model': 'classic350',
        'price': 110,
        'varient': 'black'
        },
          {
        'model': 'classic350',
        'price': 130,
        'varient': 'silver'
        },
          {
        'model': 'hunter350',
        'price': 90,
        'varient': 'yellow'
        },
         {
        'model': 'hunter350',
        'price': 110,
        'varient': 'green'
        },
         {
        'model': 'hunter350',
        'price': 150,
        'varient': 'dualTone'
        }
    ]


    def __init__(self,name = '',color = '', varients =[]):
        if name != '':
            self.bikeName = name
        if len(varients) != 0:
            self.bikeVarients = varients
        if color != '':
            self.bikeColor = color
        
        print(f'bike name is {self.bikeName}')
        print(f'bike color is {self.bikeColor}')
        print(f'bike varients are  {self.bikeVarients}')
    

classic350 = royalEnfield(name="classic 350", color='black', varients=[{}])