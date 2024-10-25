import matplotlib.pyplot as plt
import numpy as np
import math

# Constants
MASS = 0.145  
diameter = 0.1
radius = diameter / 2.0
p_air = 1.225  
V_HORIZONTAL = 244.0  
initial_conditions = [0, 100, V_HORIZONTAL, 0.0]  
g = 9.81  

AREA = math.pi * radius ** 2

def Drag(v_relative):
    if v_relative <= 0:
        return 0
    C_drag = 0.47  
    F_drag = 0.5 * p_air * v_relative**2 * C_drag * AREA
    return F_drag

def ball_trajectory(state, dt):
    x, y, v_x, v_y = state
    
    v_relative = math.sqrt(v_x ** 2 + v_y ** 2)
    F_drag = Drag(v_relative)

    drag_acc_x = -F_drag * (v_x / v_relative) / MASS if v_relative != 0 else 0
    drag_acc_y = -F_drag * (v_y / v_relative) / MASS if v_relative != 0 else 0
    
    v_x += drag_acc_x * dt
    v_y += drag_acc_y * dt - g * dt  

    x += v_x * dt
    y += v_y * dt

    return x, y, v_x, v_y

time_step = 0.01
total_time = 10.0  
num_steps = int(total_time / time_step)

state = initial_conditions
x_values = []
y_values = []

for _ in range(num_steps):
    state = ball_trajectory(state, time_step)
    if state[1] <= 0:  
        break
    x_values.append(state[0])
    y_values.append(state[1])

x_values.append(state[0])
y_values.append(0)

plt.plot(x_values, y_values)
plt.title("Ball Trajectory with Drag")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid()
plt.axis("equal")
plt.show()
