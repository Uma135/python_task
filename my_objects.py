class Vehicle:
  vehicle_type="Car"
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def get_vehicle_details():
    return f"Vehicle: {Vehicle.vehicle_type}\nBrand: {self.brand}\n Model:{self.model}"
    
v1=Vehicle("Ford","Mustang")
print(v1.get_vehicle_details())
    
