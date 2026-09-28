import pygame
import time
import random
pygame.init()
Height, Width = 600,800
Win=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Space Dodge")
BG=pygame.transform.scale(pygame.image.load("39610.jpg"), (Width, Height))
player_height, player_width = 60, 40
player_velocity = 3
star_width, star_height = 10, 20
star_velocity=3
font=pygame.font.SysFont("comicsans",30)

def draw(player,elapsed_time,stars):
    Win.blit(BG, (0, 0))

    time_text=font.render(f"Time: {round(elapsed_time)}s", 1,'white')
    Win.blit(time_text,(10,10)) 
 
    pygame.draw.rect(Win,'white',player)

    for star in stars:
        pygame.draw.rect(Win,'yellow',star)

    pygame.display.update()

def main():
    run = True
    player=pygame.Rect(200,(Height-player_height),player_width,player_height)
    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0
    star_add_increment=2000
    star_count=0
    stars=[]
    hit=False

    while run:
        star_count+=clock.tick(60)
        elapsed_time=time.time()-start_time

        if star_count>star_add_increment:
            for i in range(3):
                star_x=random.randint(0,Width-star_width)
                star=pygame.Rect(star_x,-star_height,star_width,star_height)
                stars.append(star)
            star_add_increment=(max(200,star_add_increment-50))
            star_count=0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x>0:
            player.x-=player_velocity
        if keys[pygame.K_RIGHT] and player.x<Width-player_width:
            player.x+=player_velocity

        for star in stars[:]:
            star.y+=star_velocity
            if star.y>Height:
                stars.remove(star)
            elif star.y+star_height>=player.y and star.colliderect(player):
                stars.remove(star)
                hit=True
                break
        if hit:
            lost_text=font.render("You Lost!",1,'red')
            Win.blit(lost_text,(Width/2-lost_text.get_width()/2,Height/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player,elapsed_time,stars)
    pygame.quit()
main()