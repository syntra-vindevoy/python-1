kilometers = 10
minutes = 42
seconds = 42
totalseconds = minutes*60 + seconds
avpaceinseconds = totalseconds/(kilometers/1.61)
#print(avpaceinseconds%60)
print(f"average pace is {avpaceinseconds//60} minutes and {avpaceinseconds%60} seconds per mile")
print("average pace is " + str(int(avpaceinseconds//60)) +" minutes and " + str(avpaceinseconds%60) + " seconds per mile")
avspeed = (kilometers/1.61)/(totalseconds/3600)
print(f"average speed is {avspeed} miles per hour")
print("average speed is " +str(avspeed) + " miles per hour")




#print("average pace is " + str(kilometers))

