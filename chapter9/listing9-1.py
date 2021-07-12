class Mileage:

    def __init__(self, previous_miles: int, current_miles: int):
        if current_miles < 0 or current_miles < previous_miles or previous_miles < 0:
            raise Exception('Incorrect miles entered.')
        self.current_miles = current_miles
        self.previous_miles = previous_miles

    def miles_current(self):
        return self.current_miles

    def miles_previous(self):
        return self.previous_miles


class Service:

    SERVICE_MILES = 1000

    def __init__(self, mileage: Mileage):
        self.mileage = mileage

    def must_service(self):
        return self.mileage.miles_current() - self.mileage.miles_previous() > self.SERVICE_MILES


class Vehicle:

    def __init__(self, vehicle_type: str, numberplate: str, mileage: Mileage):
        self.vehicle_type = vehicle_type
        self.numberplate = numberplate
        self.mileage = mileage

    def time_for_service(self):
        service = Service(self.mileage)
        return service.must_service()


mileage = Mileage(1000, 2900)
vehicle = Vehicle('Ford', 'CAM123456', mileage)

print(vehicle.time_for_service())
