import matplotlib.pyplot as plt
import fastf1.plotting


fastf1.Cache.enable_cache('cache')  # replace with your cache directory

# enable some matplotlib patches for plotting timedelta values and load
# FastF1's default color scheme
fastf1.plotting.setup_mpl()

# load a session and its telemetry data
quali = fastf1.get_session(2021, 'Brazil', 'R')
laps = quali.load_laps(with_telemetry=True)


# Get laps of the drivers (BOT and HAM)
laps_ver = laps.pick_driver('VER')
laps_ham = laps.pick_driver('HAM')

# Extract lap 48
lap_ver = laps_ver.loc[laps_ver['LapNumber'] == 48]
lap_ham = laps_ham.loc[laps_ham['LapNumber'] == 48]

ver_tel = lap_ver.get_car_data().add_distance()
ham_tel = lap_ham.get_car_data().add_distance()

rbr_color = fastf1.plotting.team_color('RBR')
mer_color = fastf1.plotting.team_color('MER')

fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color=rbr_color, label='VER')
ax.plot(ham_tel['Distance'], ham_tel['Speed'], color=mer_color, label='HAM')

ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Lap 48 \n "
             f"{quali.weekend.name} {quali.weekend.year} Race")

plt.show()