mode=int(input("Choose the mode of game.\n1) Normal\n2) Hard\n>>> "))

if(mode==1):
    import normal
    normal.trigger()
elif(mode==2):
    import hard
    hard.trigger()
else:
    print("Wrong Input!")
