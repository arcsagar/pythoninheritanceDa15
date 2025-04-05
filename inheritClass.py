class royalEnfield:
    bikeName = 'baseName'
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
    bikeSelectedVarient = []

    def __init__(self,name = '', model= ''):
        if name != '':
            self.bikeName = name
        if model != '':
            for bike in  self.bikeVarients:
                if bike['model'] == model:
                    self.bikeSelectedVarient.append(bike)
        
        print(f'bike name is {self.bikeName}')
        print(f'bike varients are  {self.bikeSelectedVarient}')
    

classic350 = royalEnfield(name="classic 350", model='classic350')