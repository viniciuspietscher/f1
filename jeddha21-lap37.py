import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd

# Setup plotting
plotting.setup_mpl()

# enable the cache
ff1.Cache.enable_cache('cache')

# Load the session data
race = ff1.get_session(2021, 'Jeddha', 'R')

# Collect all race laps
laps = race.load_laps(with_telemetry = True)

# Get laps of the drivers (BOT and HAM)
laps_ver = laps.pick_driver('VER')
laps_ham = laps.pick_driver('HAM')

# Extract lap 48
lap_ver = laps_ver.loc[laps_ver['LapNumber'] == 37]
lap_ham = laps_ham.loc[laps_ham['LapNumber'] == 37]

# Get telemetry from lap 48
telemetry_ver = lap_ver.get_car_data().add_distance()
telemetry_ham = lap_ham.get_car_data().add_distance()

fig, ax = plt.subplots(3)
fig.suptitle("Jeddha 2021 Race Lap 37 - Telemetry Comparison HAM vs VER")

ax[0].plot(telemetry_ver['Distance'], telemetry_ver['Speed'], label='VER')
ax[0].plot(telemetry_ham['Distance'], telemetry_ham['Speed'], label='HAM')
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")
ax[1].plot(telemetry_ver['Distance'], telemetry_ver['Throttle'], label='VER')
ax[1].plot(telemetry_ham['Distance'], telemetry_ham['Throttle'], label='HAM')
ax[1].set(ylabel='Throttle')
ax[2].plot(telemetry_ver['Distance'], telemetry_ver['Brake'], label='VER')
ax[2].plot(telemetry_ham['Distance'], telemetry_ham['Brake'], label='HAM')
ax[2].set(ylabel='Brakes')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for a in ax.flat:
    a.label_outer()
    
plt.show()