# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
  
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

num_hurdles = 6
#for hurdle in range(num_hurdles):
#    jump()
    
while num_hurdles > 0:
    jump()
    num_hurdles -= 1
    print(num_hurdles)
