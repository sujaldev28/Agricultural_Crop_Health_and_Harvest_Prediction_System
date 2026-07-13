"""
Synthetic ESP32 sensor stream generator.
"""
import random
import time
from typing import Dict, Any

class SensorStreamSimulator:
    """Simulates continuous MQTT/HTTP sensor messages."""
    
    def generate_reading(self) -> Dict[str, Any]:
        """Returns simulated crop sensor packet."""
        return {
            "temperature": random.uniform(15, 30),
            "humidity": random.uniform(50, 90),
            "air_quality": random.uniform(400, 1200),
            "light_intensity": random.uniform(1000, 20000),
            "soil_moisture": random.uniform(40, 80),
            "soil_ph": random.uniform(5.5, 7.5),
            "electrical_conductivity": random.uniform(1.0, 3.0),
            "timestamp": time.time(),
            "sensor_id": "esp32_01",
            "device_id": "device_zone_A",
            "zone_id": "zone_0",
            "crop_type": "tomato"
        }
