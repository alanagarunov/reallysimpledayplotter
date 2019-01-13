import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np   #why import this if you're not going to use it?? Well its recommended to use it instead of lists.

#initial constants
start = 0
date = []
rate = []
plt.style.use('fivethirtyeight')  #styling package used, one of the defaults
mpl.rcParams['font.size'] = 10    #the text kinda went off screen, had to change
mpl.rcParams['figure.subplot.bottom'] = 0.11  #ditto for above

def runnormalinput(start):
	while True:
		i = input("Input a rating for the day? ")
		if i == 'y':
			start = start + 1    #this value we add is how we increment the day.
			j = int(input("Rate it from 1 - 10: "))
			with open("data.txt", 'a', encoding = 'utf-8') as s:     #replace data.txt with the file path of your file
				s.write(str(j))
				s.write("\n")
		elif i == 's':
			count = 0;
			ans = int(input("Which day would you like to search for? "))
			with open("data.txt", 'r', encoding = 'utf-8') as n:    #notice it is open as read only
				for days in n:
					if count == ans:
						print("Todays ranking was: " + days)
						break
					else:
						count = count + 1
		else:
			break
		
def runfromdatabase(start, date, rate):
	with open("data.txt", encoding = 'utf-8') as f:              #replace data.txt with the file path of your file
		for i in f:
			start = start + 1    #make sure its the same as the one above.
			date.append(start)
			rate.append(int(i))
	
runnormalinput(start)
runfromdatabase(start, date, rate)

#here our date range is defined. This goes from day 0 to 365, it starts arbitrarily. You can modify it with any integer.
plt.xlim(right = 365)
plt.xlim(left = 0)

plt.plot(date, rate)

#labels and such
plt.title('nice ranking of the days')	
plt.ylabel('ranking')
plt.xlabel('days since new year')
plt.show()  #displays the graph
