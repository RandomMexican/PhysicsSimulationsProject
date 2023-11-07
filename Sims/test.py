import pygame,sys,pymunk
#importing modules

def create_apple(space,pos):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,10)
    space.add(body,shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        posX  = int(apple.body.position.x)
        posY = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(posX,posY),10)

def static_ball(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (500,500)
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

def draw_static_balls(balls):
    for ball in balls:
        posX  = int(ball.body.position.x)
        posY = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(posX,posY),50)

pygame.init() # initiating pygame
screen = pygame.display.set_mode((800,800)) # creating the display surface
clock = pygame.time.Clock() # creates in game clock
space = pymunk.Space()
space.gravity = (0,400) #first argument is the gravity 

apples = []
balls = []

# balls.append(static_ball(space))

p0 = (0,0)
p1 = (800,800)
d = 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))
    

    screen.fill((217,217,217))#background color
    draw_apples(apples)
    draw_static_balls(balls)
    
    # make_wall(walls)
    space.step(1/50) #another loop that updates the sim
    pygame.display.update()#renders the frame
    clock.tick(120)#limiting the FPS to 120
    x0,y0 = p0
    x1,y1 = p1
    pts = [
        (x0,y0),(x1,y0),
        (x1,y1),(x0,y1)
    ]
    for i in range(4):
        segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], d)
        segment.elasticity = 1
        segment.friction = 1
        space.add(segment)