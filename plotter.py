import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-10, 10, 0.01)
y_raw = input("what is y equal to (eg : 2 * x + 10; 2 ^ 3 + 15 * x)(please leave spaces between expressions) : ")
y_list = y_raw.split(' ')
print(y_list)


y = []

for character in y_list:
    if character == 'x':
        y.append(character)
    elif character == '+':
        y.append(character)
    elif character == '-':
        y.append(character)
    elif character == "*":
        y.append(character)
    elif character == '/':
        y.append(character)
    elif character == '(':
        y.append(character)
    elif character == ')':
        y.append(character)
    elif character == '^':
        y.append('**')
    elif character == 'sin(':
        y.append('np.sin(')
    elif character == 'cos(':
        y.append('np.cos(')
    elif character == 'tan(':
        y.append('np.tan(')
    elif character == 'cosec(':
        y.append('np.arcsin(')
    elif character == 'cot(':
        y.append('np.arctan(')
    elif character == 'sec(':
        y.append('np.arccos(')
    else:
        try:
            buffer = int(character)
            y.append(f"float({character})")
        except:
            y = ["Error"]

if y[0] == "Error":
    print("Invalid inputs")
else:
    y_plot = eval(''.join(y))

ax = plt.gca()
try:
    ax.plot(x,y_plot)
except NameError:
    quit()
# except :
    # print("Some error occured")
    # quit()
ax.grid(alpha=.4,linestyle='--')

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.legend()
plt.show()
