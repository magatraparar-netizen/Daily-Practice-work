from abc import ABC, abstractmethod

print("---- Python OOP Project : Vehicle Rental Management System ----")
print()


#  Vehicle Class 
class Vehicle(ABC):

    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.__rental_price = rental_price
        self.__is_available = True

    # Getter Method
    def get_rental_price(self):
        return self.__rental_price

    # Getter Method
    def get_is_available(self):
        return self.__is_available

    # Setter Method
    def set_is_available(self, status):
        self.__is_available = status

    # Abstract Method
    @abstractmethod
    def display(self):
        pass


# Car Class

class Car(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price,
                 number_of_seats, fuel_type):

        super().__init__(vehicle_id, brand, model, rental_price)

        self.number_of_seats = number_of_seats
        self.fuel_type = fuel_type

    def display(self):

        print()
        print("---- Car Details ----")
        print(f"Vehicle ID : {self.vehicle_id}")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Rental Price : {self.get_rental_price()}")
        print(f"Number of Seats : {self.number_of_seats}")
        print(f"Fuel Type : {self.fuel_type}")

        if self.get_is_available():
            print("Status : Available")
        else:
            print("Status : Rented")

        print()


# Bike Class

class Bike(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price,
                 bike_type):

        super().__init__(vehicle_id, brand, model, rental_price)

        self.bike_type = bike_type

    def display(self):

        print()
        print("---- Bike Details ----")
        print(f"Vehicle ID : {self.vehicle_id}")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Rental Price : {self.get_rental_price()}")
        print(f"Bike Type : {self.bike_type}")

        if self.get_is_available():
            print("Status : Available")
        else:
            print("Status : Rented")

        print()


#Main Program 
car = None
bike = None

while True:

    print("---- Choose an Operation ----")
    print("1. Add a Car")
    print("2. Add a Bike")
    print("3. Rent a Vehicle")
    print("4. Return a Vehicle")
    print("5. Show Vehicle Details")
    print("6. Exit")

    print()

    choice = int(input("Enter your choice (1 - 6) : "))

    print()


    #  Add Car 
    if choice == 1:

        print("Car Details -----")

        car = Car(
            input("Enter Vehicle ID : "),
            input("Enter Brand : "),
            input("Enter Model : "),
            float(input("Enter Rental Price per day : ")),
            int(input("Enter Number of Seats : ")),
            input("Enter Fuel Type : ")
        )

        print()

        print(
            f"Car created with ID : {car.vehicle_id}, "
            f"Brand : {car.brand}, "
            f"Model : {car.model}."
        )

        print()


    #  Add Bike 
    elif choice == 2:

        print("Bike Details -----")

        bike = Bike(
            input("Enter Vehicle ID : "),
            input("Enter Brand : "),
            input("Enter Model : "),
            float(input("Enter Rental Price per day : ")),
            input("Enter Bike Type : ")
        )

        print()

        print(
            f"Bike created with ID : {bike.vehicle_id}, "
            f"Brand : {bike.brand}, "
            f"Model : {bike.model}."
        )

        print()


    #  Rent Vehicle 
    elif choice == 3:

        vehicle_id = input("Enter Vehicle ID to rent : ")

        print()

        if car is None and bike is None:

            print("No vehicle is added.")
            print()

        elif car is not None and vehicle_id == car.vehicle_id:

            if car.get_is_available():

                car.set_is_available(False)

                print(
                    f"Car {car.brand} {car.model} "
                    f"has been rented successfully."
                )

                print(f"Rental Price per day : {car.get_rental_price()}")

            else:

                print("This car is already rented.")

            print()


        elif bike is not None and vehicle_id == bike.vehicle_id:

            if bike.get_is_available():

                bike.set_is_available(False)

                print(
                    f"Bike {bike.brand} {bike.model} "
                    f"has been rented successfully."
                )

                print(f"Rental Price per day : {bike.get_rental_price()}")

            else:

                print("This bike is already rented.")

            print()


        else:

            print("Vehicle ID does not exist.")
            print()


    #  Return Vehicle 
    elif choice == 4:

        vehicle_id = input("Enter Vehicle ID to return : ")

        print()

        if car is None and bike is None:

            print("No vehicle is added.")
            print()

        elif car is not None and vehicle_id == car.vehicle_id:

            if not car.get_is_available():

                car.set_is_available(True)

                print(
                    f"Car {car.brand} {car.model} "
                    f"returned successfully."
                )

            else:

                print("This car is already available.")

            print()


        elif bike is not None and vehicle_id == bike.vehicle_id:

            if not bike.get_is_available():

                bike.set_is_available(True)

                print(
                    f"Bike {bike.brand} {bike.model} "
                    f"returned successfully."
                )

            else:

                print("This bike is already available.")

            print()


        else:

            print("Vehicle ID does not exist.")
            print()


    #  Show Details 

    elif choice == 5:

        print("Choose vehicle type to show :")
        print("1. Car")
        print("2. Bike")
        print("3. All Vehicles")

        print()

        show_choice = int(input("Enter your choice : "))

        print()


        if show_choice == 1:

            if car is None:
                print("Car is not added.")
            else:
                car.display()


        elif show_choice == 2:

            if bike is None:
                print("Bike is not added.")
            else:
                bike.display()


        elif show_choice == 3:

            if car is None and bike is None:
                print("No vehicles are added.")

            else:

                if car is not None:
                    car.display()

                if bike is not None:
                    bike.display()


        else:

            print("Invalid choice.")

        print()


    # Exit 

    elif choice == 6:

        print("Exiting the Programme. Thank You!")

        print()

        print("Goodbye!")

        break


    else:

        print("Invalid Choice Entered!")

        print()

    print("--- Choose another Operation ---")
    print()