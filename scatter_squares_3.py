import matplotlib.pyplot as plt 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

ax.axis([0, 1100, 0, 1100000])

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show(block=False)
plt.pause(1)
input()
plt.close()

