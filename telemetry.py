import fastf1 as f1
import matplotlib.pyplot as plt
import asyncio
import numpy as np

# Загрузка сессии гонки в Монако 2024 года
session = f1.get_session(2024, 'Monaco', 'R')
session.load()

# Извлечение данных по лучшему кругу для гонщика Verstappen
ver_laps = session.laps.pick_driver('VER').pick_fastest()

# Извлечение телеметрии для лучшего круга Verstappen
ver_telemetry = ver_laps.get_telemetry()

# Извлечение передачи, скорости, дистанции, педали газа (Throttle) и тормоза (Brake)
gear_data = ver_telemetry['nGear']  # Передача
speed_data = ver_telemetry['Speed']  # Скорость
distance_data = ver_telemetry['Distance']  # Дистанция
throttle_data = ver_telemetry['Throttle']  # Педаль газа

# Преобразуем данные тормоза: любые значения тормоза > 0 отображаются как 100%, 0 остается 0
brake_data = np.where(ver_telemetry['Brake'] > 0, 100, 0)  # Масштабируем торможение

# Асинхронная функция для построения четырёх графиков в одном окне
async def plot_verstappen_telemetry():
    await asyncio.sleep(0.1)  # Небольшая задержка для асинхронности

    # Создаем фигуру с четырьмя подграфиками (4 строки, 1 столбец)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 12), sharex=True)

    # Первый график: Скорость
    ax1.set_ylabel('Speed (km/h)', color='blue')
    ax1.plot(distance_data, speed_data, label='Speed', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_title('Verstappen Speed, Throttle, Brake and Gear Over Distance - Monaco GP 2024')
    ax1.grid(True)

    # Второй график: Throttle
    ax2.set_ylabel('Throttle (%)', color='green')
    ax2.plot(distance_data, throttle_data, label='Throttle', color='green')
    ax2.tick_params(axis='y', labelcolor='green')
    ax2.grid(True)

    # Третий график: Масштабированный Brake
    ax3.set_ylabel('Brake (Scaled)', color='red')
    ax3.plot(distance_data, brake_data, label='Brake', color='red', linestyle='-', linewidth=2)
    ax3.tick_params(axis='y', labelcolor='red')
    ax3.grid(True)

    # Четвертый график: Gear
    ax4.set_xlabel('Distance (m)')
    ax4.set_ylabel('Gear', color='orange')
    ax4.plot(distance_data, gear_data, label='Gear', color='orange', linestyle='-.')
    ax4.tick_params(axis='y', labelcolor='orange')
    ax4.grid(True)

    # Настройки компоновки графиков
    plt.tight_layout()

    # Отображаем графики
    plt.show()

# Основная асинхронная функция
async def main():
    await plot_verstappen_telemetry()

# Запуск программы
asyncio.run(main())
