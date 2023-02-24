#list of available cars and their prices
car_list = {'Tesla':900000,'Landcruiser':15000, 'Bentley':800000, 'Camry':20000, 'KIA':6000,
'Bugatti chiron':840000, 'Mclaren F1':647000, 'Ford Mustang':745800, 'Maserati':200471, 
'Honda Accord':502362, 'Lamborghini Diablo': 389456, 'Volkswagen Beetle':30589, 
'Corolla':65999, 'Jeep Gladiator':500477, 'Pagani Huayra':17008, 'Porsche 911 Carrera':40777, 
'Dodge Stealth':544789, 'Rolls Royce Phantom':999999, 'Henessey Venom':638741, 'Volvo':28796, 
'Lincoln':78945, 'Lexus':654785, 'Cadilac':874551, 'BMW':224788, 'Acura':7894, 'Audi':23369, 
'Jaguar':458788, 'Tundra':73144, 'Pathfinder': 47526, 'Ferrari':1000000}
#inquire the user input for car name 
car_name = input("Enter car_name: ")
if car_name in car_list:
    print("YES")
    car_cost = car_list[car_name]
    print(f"The price of {car_name} is ${car_cost}.")
else:
    print(f"Unfortunately, {car_name} is not available at the moment")
#https://github.com/Kwame-Gyimah/Data-Structures
