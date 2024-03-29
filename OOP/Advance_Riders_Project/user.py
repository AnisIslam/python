import hashlib
from random import random, randint
from brta import BRTA
from vehicle import Bike, Car, Cng
from rideManager import uber

class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f'User: {email} already exists.')
        super().__init__(*args)
license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exists = False
          #check duplicate mail user
        with open('users.txt', 'r') as file:
            if email in file.read():
                already_exists = True
                
                # print(f'User: {email} already exists.')
        file.close()
        if already_exists == False:
            with open('users.txt', 'a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
            file.close()
        # print(self.name, 'user created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    # print(line)
                    stored_password = line.split(' ')[1]
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print('valid user')
            return True
        else:
            print('invalid user')
            return False
       
class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def get_trip_history(self):
        return self.__trip_history
    
    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare, trip_info):
        # print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)

class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        self.vehicle = None

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print('Sorry WRONG!, try again')
            self.license = None
        else: 
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self )
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self )
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print('You are not a valid driver')
    def start_a_trip(self, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        self.__trip_history.append(trip_info)


# user1 = User('user 1', 'user1@gmail.com', 'user0pass')
# User.log_in('user1@gmail.com', 'user0pass')

# driverShaheb1 = Driver("Montu", "monto@gmail.com", 'omontujawkoi', 65, 4577)
# result = license_authority.validate_license(driverShaheb1.email, driverShaheb1.license)
# print(result)
# driverShaheb1.take_driving_test

rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 5000)
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 5000)
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 5000)
for i in range(0,100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}', randint(0, 100), randint(1000, 5999))
    driver1.take_driving_test()
    driver1.register_a_vehicle('car', randint(10000, 59999), 10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider1, 'car', randint(1, 100))

print(rider1.get_trip_history())
#driver overwrite