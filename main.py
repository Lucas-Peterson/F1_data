import fastf1 as f1
import matplotlib.pyplot as plt
import asyncio

# Load the race session
session = f1.get_session(2024, 'Monaco', 'R')
session.load()

# Get data for Verstappen and Piastri
ver_lap = session.laps.pick_driver('VER')
pia_lap = session.laps.pick_driver('PIA')

ver_laps = ver_lap.pick_fastest()
pia_laps = pia_lap.pick_fastest()

ver_telemetry = ver_laps.get_telemetry()
pia_telemetry = pia_laps.get_telemetry()

# Maximum and minimum speed for Verstappen
max_speed_ver = ver_telemetry['Speed'].max()
min_speed_ver = ver_telemetry['Speed'].min()

# Maximum and minimum speed for Piastri
max_speed_pia = pia_telemetry['Speed'].max()
min_speed_pia = pia_telemetry['Speed'].min()

# Coordinates for maximum and minimum speed
max_speed_ver_dist = ver_telemetry['Distance'][ver_telemetry['Speed'].idxmax()]
min_speed_ver_dist = ver_telemetry['Distance'][ver_telemetry['Speed'].idxmin()]

max_speed_pia_dist = pia_telemetry['Distance'][pia_telemetry['Speed'].idxmax()]
min_speed_pia_dist = pia_telemetry['Distance'][pia_telemetry['Speed'].idxmin()]


# Asynchronous function for plotting the graph
async def plot_speeds():
    await asyncio.sleep(0.1)  # Small delay for async behavior

    # Plotting the graph
    plt.figure(figsize=(12, 6))

    # Lines for Verstappen
    plt.plot(ver_telemetry['Distance'], ver_telemetry['Speed'], label='Verstappen', color='blue')
    plt.axhline(y=max_speed_ver, color='blue', linestyle='--', label='Max Verstappen Speed', alpha=0.7)
    plt.axhline(y=min_speed_ver, color='blue', linestyle='--', label='Min Verstappen Speed', alpha=0.7)

    # Displaying maximum and minimum speed for Verstappen
    plt.text(max_speed_ver_dist, max_speed_ver, f'{max_speed_ver:.2f} km/h', color='blue', fontsize=10,
             verticalalignment='bottom')
    plt.text(min_speed_ver_dist, min_speed_ver, f'{min_speed_ver:.2f} km/h', color='blue', fontsize=10,
             verticalalignment='top')

    # Lines for Piastri
    plt.plot(pia_telemetry['Distance'], pia_telemetry['Speed'], label='Piastri', color='orange')
    plt.axhline(y=max_speed_pia, color='orange', linestyle='--', label='Max Piastri Speed', alpha=0.7)
    plt.axhline(y=min_speed_pia, color='orange', linestyle='--', label='Min Piastri Speed', alpha=0.7)

    # Displaying maximum and minimum speed for Piastri
    plt.text(max_speed_pia_dist, max_speed_pia, f'{max_speed_pia:.2f} km/h', color='orange', fontsize=10,
             verticalalignment='bottom')
    plt.text(min_speed_pia_dist, min_speed_pia, f'{min_speed_pia:.2f} km/h', color='orange', fontsize=10,
             verticalalignment='top')

    # Graph styling
    plt.title('Speed Comparison - Monaco GP 2024 (Race)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Speed (km/h)')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


# Asynchronous function for printing speed data
async def print_speeds():
    await asyncio.sleep(0.1)
    print(f"Verstappen's Max Speed: {max_speed_ver:.2f} km/h")
    print(f"Verstappen's Min Speed: {min_speed_ver:.2f} km/h")
    print(f"Piastri's Max Speed: {max_speed_pia:.2f} km/h")
    print(f"Piastri's Min Speed: {min_speed_pia:.2f} km/h")


# Main function to run asynchronous tasks
async def main():
    await asyncio.gather(print_speeds(), plot_speeds())


# Run the program
asyncio.run(main())
