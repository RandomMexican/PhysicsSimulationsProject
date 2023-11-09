import pygame,sys,Buttons

class main():
    pygame.init()

    window_size = (800,800) #what we want the res to be
    window = pygame.display.set_mode(window_size) #setting the windows res
    pygame.display.set_caption("pygame window") # giving the windo a caption

    # load images
    gravIMG = pygame.image.load('Images/SandGravIMG.png').convert_alpha()
    GOLIMG = pygame.image.load('Images/GOLimg.png').convert_alpha()


    # create new button instances
    GravSim = Buttons.button(100,200,gravIMG,0.8)
    GOLSim = Buttons.button(450,200, GOLIMG,0.8)

    # starts loop
    running = True
    while running:
    # handles events

        for event in pygame.event.get():
            # ends the loop
            if event.type == pygame.QUIT:
                running = False
        window.fill((128,128,128))
        
        if GravSim.draw(window):
            from Sims.SandGrav import SandGrav
            SandGrav()
        if GOLSim.draw(window):
            print("GOLsim")
        
        pygame.display.flip()
        

pygame.quit

