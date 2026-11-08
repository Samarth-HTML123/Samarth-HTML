class India():
    def capital(self):
        print("New Delhi is the Capital of India")
        
    def language(self):
        print("Hindi is the most widely spoken language of India")
        
    def type(self):
        print("India is a developing country")
        
        
    
class USA():
    def capital(self):
        print("New D.C. is the Capital of US")
        
    def language(self):
        print("English is the most widely spoken language of USA")
        
    def type(self):
        print("USA is a developed country")
        
        
obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
        
        