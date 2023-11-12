import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis="both", labelsize=14)

#Passing the argument block=False in order to allow me to close the matplotlib window from the terminal by simply pressing 'Enter'
plt.show(block=False)
#Subsequent code below again contributes to my ability to close the window simply by pressing 'Enter' in the terminal
plt.pause(1)
input()
plt.close()