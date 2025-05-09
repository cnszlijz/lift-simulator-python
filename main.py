import simulator

def update_state(lift):
    pass

if __name__=="__main__":
    bot=simulator.simulator(update_state)
    t=0
    while True:
        t+=1
        if(bot.run()):
            print(t)
    pass
