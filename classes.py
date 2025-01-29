class building:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def calculate_area(self):
        return self.length*self.width
    

#create instance of the class
build1=building(20,30)

area_=build1.calculate_area()
print(area_)
