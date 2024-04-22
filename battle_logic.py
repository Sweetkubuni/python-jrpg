

#params might need to be enemies: List[Person], allies: List[Person]


main_loop:
    #(1) calculate the turn-order of each person
    #(2) enemy ai and human pre-empthaically selects moves for each person
    # in their party list
    #(3) events play out in processing_queue_event function
    #(4) if main character moral is 0 or  main character (hp is 0) and other
    #allies hp or moral is zero: you lose. if all enemies either have 0 moral or hp
    #then you win.
    # if no winners, go back to (1)