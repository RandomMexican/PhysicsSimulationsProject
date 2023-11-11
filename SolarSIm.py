import pygame,math
import Buttons
pygame.init()



width = 800
height = 800

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Solar Sim")


backIMG = pygame.image.load('Images/mainmenu.png').convert_alpha()
# create main menu button
MMB = Buttons.button(100,100,backIMG,0.5)


white = (255,255,255)
yellow = (255,255,0)
blue = (100,148,237)
red = (188,39,50)
dark_grey = (80,78,81)

class Planet:
    # astronomical units to simplified for later (km to M)
    AU = 149.6e6 * 1000
    # gravitational constant used to find the force of attraction between obj
    G = 6.67428e-11
    # scale
    SCALE = 250 / AU # 1 AU = 100 pixels
    # how time is simulated to not spend hours 
    # watching the planet shift slightly
    TIMESTEP = 3600 * 24 # 1 day


    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        # keeps track of planets orbit to later draw a path
        self.orbit = []
        # if thing is sun to draw or not draw
        self.sun = False
        # update for every planet to know its distance and draw it on screen
        self.distance_to_sun = 0



        # velocity on the x and y axis to make a circle 
        # at a constant speed
        self.x_vel = 0
        self.y_vel = 0

    def draw(self,win):

        x = self.x * self.SCALE + width / 2 
        y = self.y * self.SCALE + height / 2 

        if len(self.orbit) > 2:
            # getting a list of updated points
            updated_points = []
            for point in self.orbit:
                # x,y cords to scale
                x,y = point
                x = x* self.SCALE + width/2
                y = y* self.SCALE + height/2
                updated_points.append((x,y))

            # takes list of points and draws lines on them
            pygame.draw.lines(win, self.color,False,updated_points,2)
        pygame.draw.circle(win,self.color,(x,y), self.radius)
    

    # a bunch of math that uses trigonometry to determine attraction
    def attraction(self,other):
        # calc distance between 2 objects
        other_x,other_y = other.x,other.y
        distance_x = other_x -self.x
        distance_y = other_y -self.y
        distance = math.sqrt(distance_x **2 + distance_y **2)

        # determine if obj is sun
        if other.sun:
            self.distance_to_sun = distance
        
        # actually calculating force of attraction
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_pos(self,planets):
        # total forces exerted on this planet from others
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # calculating the x,y velocity 
        self.x_vel += total_fx/self.mass * self.TIMESTEP
        self.y_vel += total_fy/self.mass * self.TIMESTEP

        # update pos using velocity from above
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        # append pos to draw orbit later
        self.orbit.append((self.x,self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    # creating planets and the sun
    sun = Planet(0, 0, 30, yellow, 1.98892 * 10**30) # mass in KG
    sun.sun = True
    # planets also need pre existing y velocity to start moving
    earth = Planet(-1* Planet.AU,0,16,blue,5.9742 *10**24)
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.524 * Planet.AU, 0, 12, red, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    mercury = Planet(0.387 * Planet.AU,0,8, dark_grey, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    venus = Planet(0.723 * Planet.AU, 0 , 14, white, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000
    planets = [sun,earth,mars,mercury,venus]


    while run:
        clock.tick(60)
        win.fill((0,0,0))
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw planets
        for planet in planets:
            planet.update_pos(planets)
            planet.draw(win)
        if MMB.draw(win):
            import main
            main()

        pygame.display.update()


    pygame.quit

main()