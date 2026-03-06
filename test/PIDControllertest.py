import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

Kp, Ki, Kd = 0.3, 0.1, 0.1
setpoint = 100.0 #目標
pv = 20 #當前值
integral = 0
last_error = 0
dt = 0.1 #時間間隔

#儲存繪圖資料
time_data, pv_data, sp_data = [], [], []

def update_pid(current_pv):
    global integral, last_error
    error = setpoint - current_pv
    integral += error * dt
    derivative = (error - last_error)/dt
    output = Kp * error + Ki * integral + Kd * derivative
    last_error = error
    return output

fig, ax = plt.subplots()
line_pv, = ax.plot([], [], label='current temp (PV)', color='blue')
line_sp, = ax.plot([], [], 'r--', label='target(SP)')
ax.set_xlim(0,50)
ax.set_ylim(0,150)
ax.legend()

def animate(i):
    global pv
    #PID output
    control = update_pid(pv)

    #受控對象反應
    pv += control * 0.1

    #更新
    time_data.append(i * dt)
    pv_data.append(pv)
    sp_data.append(setpoint)

    line_pv.set_data(time_data, pv_data)
    line_sp.set_data(time_data, sp_data)
    return line_pv, line_sp


# 取得現在時間，格式為：20231027_143005 (年三月日_時分秒)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
target_path = f"/workspaces/Python-Practice/test/pid_{timestamp}.gif"

ani = FuncAnimation(fig, animate, frames=500, interval=50, blit=True)
print("正在生成動畫檔案...")
ani.save(target_path, writer='pillow')
print(f"檔案已儲存至：{target_path}")