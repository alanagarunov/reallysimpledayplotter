# reallysimpledayplotter
A really simple day plotter.
Uses the matplotlib library for plotting graphs. Link https://matplotlib.org/

This is setup as a sortof day or mood counter if you would like. You can change it to whatever you'd like by changing the axis labels.
Basically when you run this program it will ask if you will want to input a rating for a particular day. Type 'y' for yes and anything else for no, when its no itll break out of the loop and print the graph. 
If you did type 'y' then it will ask you to input a rating, an integer, then ask you if you want to add another day. All numbers are saved to a textfile and will leave off from the last day you inputted. 
You must do it day by day.

There is no search feature or start from specific date, yet. Right now it starts from whenever day 0 is and stops after . You can modify that by changing the x-axis min and max values and the start values. Also would probably be cool to make it more colorful in the future.

This only works on Python 3.6 for me.
