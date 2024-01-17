from dataclasses import dataclass


@dataclass
class Car:
    fuel: float = 100
    distance: float = 0

    def show_tank(self):
        print(f"The car contains {self.fuel} liters of gasoline.")
        print("-" * 50)

    def drive(self, km: float):
        lost_fuel = (km * 5) / 100
        self.fuel -= lost_fuel

        if self.fuel >= 10:
            self.distance += km
            print(f"You drove {km} kilometers.\nThe car has {self.fuel} liters of gasoline left.")
        elif 10 > self.fuel > 0:
            self.distance += km
            print(f"You drove {km} kilometers.\nYou are almost out of fuel! The car has {self.fuel} liters of gasoline left.")
        else:
            over_km: float = (-self.fuel * 100) / 5
            last_km = km - over_km
            self.distance += last_km
            print(f"You drove only {last_km} kilometers.\nYou're out of fuel! Please fill up the tank.")

        print("-" * 50)

    def refuel(self):
        self.fuel = 100
        self.distance = 0
        print("Your tank is full, you can go.")
        print("-" * 50)

    def driven_distance(self):
        print(f"You drove a total of {self.distance} kilometers since last fill-up.")
        print("-" * 50)


if __name__ == "__main__":
    my_car = Car()

    my_car.show_tank()
    my_car.drive(50)
    my_car.drive(1000)
    my_car.driven_distance()
    my_car.drive(875)
    my_car.driven_distance()
    my_car.drive(100)
    my_car.driven_distance()


