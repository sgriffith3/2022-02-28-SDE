#task = "Take out the trash"
#dom = 7
#
#print(f"{type(task)} - {task}")
#print(f"{type(dom)} - {dom}")

class Vehicle:

    def __init__(self, name='car', color='yellow'):
        self.name = name 
        self.color = color
        self.pos = 0

    def __repr__(self):
        return f"""
        Style: car
        Color: {self.color}
        Name:  {self.name}
        """ 

    def drive(self, distance=1):
        self.pos += distance
        print(f"{self.name} is at {self.pos}")


class Truck(Vehicle):
    def __init__(self, name="truck", color="puce",  bed_size=5):
        super().__init__(name=name, color=color)
        self.bed = bed_size



blue_f150 = Truck(name="bluey", color="blue", bed_size=66)
print(blue_f150)
print(blue_f150.name)
print(blue_f150.color)
blue_f150.drive(99)
print(f"The bed size is {blue_f150.bed}")

red_ram = Vehicle(name="ramser", color="red")
print(red_ram)
print(red_ram.name)
print(red_ram.color)
