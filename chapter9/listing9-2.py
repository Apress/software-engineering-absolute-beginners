class AbstractService:
    SERVICE_MILES = 0
    TYPE = ''

    def __init__(self, previous_miles, current_miles):
        if current_miles < 0 or current_miles < previous_miles or previous_miles < 0:
            raise Exception('Incorrect miles entered.')
        self.previous_miles = previous_miles
        self.current_miles = current_miles

    def must_service(self):
        print('Calculating ' + self.TYPE + ' service mileage')
        return self.current_miles - self.previous_miles > self.SERVICE_MILES


class Service(AbstractService):
    SERVICE_MILES = 1000
    TYPE = 'normal'


class MajorService(AbstractService):
    SERVICE_MILES = 10000
    TYPE = 'major'


class Vehicle:

    def __init__(self, vehicle_type: str, numberplate: str):
        self.vehicle_type = vehicle_type
        self.numberplate = numberplate

    def time_for_service(self, serviceObject: AbstractService):
        return serviceObject.must_service()


vehicle = Vehicle('Ford', 'CAM123456')

print(vehicle.time_for_service(MajorService(1000, 20000)))
print(vehicle.time_for_service(Service(400, 453)))
