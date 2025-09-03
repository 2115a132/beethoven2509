#id, name, discription, category, tags, stock, price 
class product:
    def ___init__(self, id , name, description, category, tags, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price
    def  __str__(self):
        return f'[id={self.id}, name={self.name}, description={self.name}, category={self.category}, tags={self.tags}, stock={self.stock}, price={self.price}]'
    def __repr__(self):
        return self.__str__()
mobile_vivo = product(1001, 'vivo Y21', 'Good camera quality', 'Mobile', 'mobile. electronics,smart phone, androidphone', 10, 21000 )   #Product(1001,  description= 'Good camera quality', 'Mobile', 'mobile. electronics,smart phone, androidphone', 10, 21000, name ''vivo Y21') (keyword argument) for suffle the order
print(mobile_vivo)
mobile_sumsung = product(1001,  description= 'Good camera quality', category='Mobile', tags='mobile electronics,smart phone, androidphone', name='samsung A31', stock=10, price=21000 )
print(mobile_sumsung)