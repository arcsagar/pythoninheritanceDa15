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
        print(f'bike before varients are  {self.bikeSelectedVarient}')
        if name != '':
            self.bikeName = name
        if model != '':
            for bike in  self.bikeVarients:
                if bike['model'] == model:
                    self.bikeSelectedVarient.append(bike)
        
        print(f'bike name is {self.bikeName}')
        print(f'bike after varients are  {self.bikeSelectedVarient}')
    


# hunter350 = royalEnfield(name="hunter 350", model='hunter350')
# hunter350.bikeSelectedVarient = []
# print('-----')
# print('-----')
# print('-----')
# print('-----')
# classic350 = royalEnfield(name="classic 350", model='classic350')

class classic350(royalEnfield):
    
    def __init__(self, name='', model=''):
        self.bikeSelectedVarient = []
        super().__init__(name=name,model=model)

class hunter350(royalEnfield):
    
    def __init__(self, name='', model=''):
        self.bikeSelectedVarient = []
        super().__init__(name=name,model=model)



cl1 = classic350(name="classic 350", model='classic350')
print('---')
print('---')
print('---')
print('---')
ht1 = classic350(name="hunter 350", model='hunter350')