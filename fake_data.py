import random
import time

# base location (example: Bengaluru)
BASE_LAT = 12.9716
BASE_LON = 77.5946

def fake_can_frame():
    speed = random.uniform(0, 60)                     
    engine_temp = random.uniform(40, 95)              
    fuel_level = random.uniform(10, 100)              
    lat = BASE_LAT + random.uniform(-0.0005, 0.0005)
    lon = BASE_LON + random.uniform(-0.0005, 0.0005)

    speed_int = int(speed * 10)
    temp_int = int(engine_temp)
    fuel_int = int(fuel_level)
    lat_int = int((lat - BASE_LAT) * 1e6)
    lon_int = int((lon - BASE_LON) * 1e6)

    data_bytes = [
        (speed_int >> 8) & 0xFF, speed_int & 0xFF,
        temp_int & 0xFF,
        fuel_int & 0xFF,
        lat_int & 0xFF,
        lon_int & 0xFF,
        0, 0
    ]

    print(
        "ID: 0x120  DATA:",
        " ".join(f"{b:02X}" for b in data_bytes),
        f" | speed={speed:.1f} km/h",
        f"temp={engine_temp:.1f}°C",
        f"fuel={fuel_level:.1f}%",
        f"lat={lat:.6f}",
        f"lon={lon:.6f}"
    )

while True:
    fake_can_frame()
    time.sleep(1)