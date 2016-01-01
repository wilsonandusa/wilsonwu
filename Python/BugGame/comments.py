clr1 = (22,122,211)
clr2 = (254,44,123)
clr3 = (34,66,123)
'''screen.fill((123,i,i))
pygame.draw.line(screen,clr2,(0,0),(640,360),5)
pygame.draw.rect(screen,clr3,(40,40,300,45))    #x,y,width height
pygame.draw.circle(screen,clr1,(350,200),80,10)'''

img_bug = pygame.image.load("images/bug.png")
screen.blit(img_bug,(200,200))   #function display on screen

