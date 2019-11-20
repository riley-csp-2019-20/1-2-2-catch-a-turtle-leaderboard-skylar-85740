# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random as rand
import leaderboard as lb
#-----game configuration----
fruit = trtl.Turtle()
fruit.shape("circle")
fruit.shapesize(4)
fruit.fillcolor("red")
fruit.speed(6)
score = 0
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(0,-300)
score_writer.pendown()
score_writer.speed(4)
#-----countdown writer-----
counter =  trtl.Turtle()
counter.penup()
counter.goto(0,300)
counter.pendown()
#-----initialize turtle-----

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----game functions--------
def fruit_clicked(x, y):
    change_position()   
    update_score() 
    countdown()
    score_writer.write(score, font=font_setup)
        
def change_position():
    fruit.penup()
    fruit.hideturtle()
    if not timer_up:
      fruitx = rand.randint(-400,400)
      fruity = rand.randint(-200,200)
      fruit.goto(fruitx,fruity)
      fruit.st()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)
    
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        if timer <= 0:
            counter.write("Time's Up", font=font_setup)
            timer_up = True
            manage_leaderboard()
        else:

    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)





#-----events----------------
fruit.onclick(fruit_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()