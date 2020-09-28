from sense_hat import SenseHat

sense = SenseHat()
number= 1 #To initialize the loop 

while True:
  events = sense.stick.get_events()
  for event in events:
    if event.action != "pressed":
        number+=1 #adding step
        if number%2 == 0: #loop condition
            sense.show_letter("R")
        else:
            sense.show_letter("M")