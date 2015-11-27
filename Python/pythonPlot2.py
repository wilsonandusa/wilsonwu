# exactly the same as the very first example:

x = np.linspace(0, 5, 10)
y = x ** 2 

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x, y, 'r--')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('y = x^2')

axes[1].plot(y, x, 'g*-')
axes[1].set_xlabel('y')
axes[1].set_ylabel('x')
axes[1].set_title('x = sqrt(x)')
    
fig.tight_layout()
