import pgzrun
WIDTH = 1000 #window width
HEIGHT = 740 #window height

#game variables
play_time = 60
beep1 = tone.create('D5', 0.1)
beep2 = tone.create('D5', 0.5)
beep3 = tone.create('D3', 0.1)

actual_differences = [[Actor('transparent_star_blue', pos = (860, 700)), False],[Actor('transparent_star_blue',pos = (880,240)),False], [Actor('transparent_star_blue', pos = (820, 140)), False], [Actor('transparent_star_blue', pos = (775, 645)), False]]
discovered_differences = []

def draw():
    global play_time, game_ends
    screen.blit('spot_the_difference', pos=(0,0) )

    screen.draw.text(str(play_time), pos=(30, 30), fontname='itckrist', fontsize=48, color='orange', gcolor='red', owidth=0.5, ocolor='black')
    screen.draw.text('Score: '+ str(len(discovered_differences)) + '/'+ str(len(actual_differences)), pos=(30, 100), fontname='itckrist', fontsize=48, color='orange', gcolor='red', owidth=0.5, ocolor='black')
    for diff in discovered_differences:
        diff.draw()

    if play_time > 0:
        if play_time > 3 and play_time < 11:
            beep1.play()
        elif play_time > 0 and play_time < 4:
            beep2.play()
    else:
        for act_diff in actual_differences:
            if not act_diff[1]:
                act_diff[0].draw()


def on_mouse_down(pos, button):
    global actual_differences, discovered_differences, play_time
    if play_time > 0:
        if button == mouse.LEFT:
            i =0
            flag = False
            while i < len(actual_differences):
                if actual_differences[i][1] == False:
                    if actual_differences[i][0].collidepoint(pos):
                        discovered_differences.append(Actor('transparent_star', pos = pos))
                        flag = True
                        actual_differences[i][1] = True
                        break
                i+=1

            if flag == False:
                beep3.play()

def timer():
    global play_time
    if play_time > 0:
        play_time-=1

clock.schedule_interval(timer, 1)
pgzrun.go()