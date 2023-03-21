




class Sphere(object):

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        print(self.radius, "Check radius")
        return self.radius, "Check radius"
    def get_mass(self):
        print(self.mass, "Check mass")
        return self.mass, "Check mass"
    def get_volume(self):
        # формула объемной сферы --- V=4/3πr**3
        pass
    def get_surface_area(self):
        # площадь поверхности сферы --- S=4πR**2
        pass
    def get_density(self):
        # плотность сферы
        pass






ball = Sphere(2,50)

ball.get_radius()                   #2, "Check radius"
ball.get_mass()                     #50, "Check mass"
# ball.get_volume()                   #33.51032, "Check volume"
# ball.get_surface_area()             #50.26548, "Check area"
# ball.get_density()                  #1.49208, "Check density"





