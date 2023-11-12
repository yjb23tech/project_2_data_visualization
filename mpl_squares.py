import matplotlib.pyplot as plt 

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

#Passing the argument block=False in order to allow me to close the matplotlib window from the terminal by simply pressing 'Enter'
plt.show(block=False)
#Subsequent code below again contributes to my ability to close the window simply by pressing 'Enter' in the terminal
plt.pause(1)
input()
plt.close()