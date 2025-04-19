#### Simulation von Daten durch die Entwicklung einer API ####



import random
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

def add_noise(value, noise_min, noise_max):
    return round(value + random.uniform(noise_min, noise_max), 2)

@app.route('/sensordata')
def get_sensor_data():
    timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    #### 
    oil_temperature_base = random.uniform(75.0, 90.0)
    oil_pressure_base = random.uniform(2.0, 3.0)
    engine_power_base = random.uniform(150.0, 350.0)
    engine_speed_base = random.uniform(1450, 1550)
    engine_vibrations_base = random.uniform(0.3, 0.7)

    # Adding slight noise
    oil_temperature = add_noise(oil_temperature_base, -2, 2)
    oil_pressure = add_noise(oil_pressure_base, -0.2, 0.2)
    engine_power = add_noise(engine_power_base, -10, 10)
    engine_speed = round(add_noise(engine_speed_base, -30, 30), 0)
    engine_vibrations = add_noise(engine_vibrations_base, -0.1, 0.1)

    response = {
        "timestamp": timestamp,
        "oil_temperature": oil_temperature,
        "oil_pressure": oil_pressure,
        "engine_power": engine_power,
        "engine_speed": engine_speed,
        "engine_vibrations": engine_vibrations,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)

