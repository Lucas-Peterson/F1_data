import fastf1 as f1
import matplotlib.pyplot as plt

session = f1.get_session(2024, 'Belgium', 'R')
session.load()


ver_laps = session.laps.pick_driver('VER')
pia_laps = session.laps.pick_driver('PIA')


ver_lap = ver_laps.pick_fastest()
pia_lap = pia_laps.pick_fastest()

ver_telemetry = ver_lap.get_telemetry()
pia_telemetry = pia_lap.get_telemetry()

plt.figure(figsize=(10, 6))
plt.plot(ver_telemetry['Distance'], ver_telemetry['Speed'], label='Verstappen', color='blue')
plt.plot(pia_telemetry['Distance'], pia_telemetry['Speed'], label='Piastri', color='orange')
plt.title('Speed Comparison - Belgium GP 2024 (Race)')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.show()
