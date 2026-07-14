"""
Pydantic schemas for serialization and validation.
"""
from pydantic import BaseModel, Field
from datetime import datetime

class SensorRecord(BaseModel):
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., description="Relative Humidity percentage")
    air_quality: float = Field(..., description="CO2 levels in ppm")
    light_intensity: float = Field(..., description="Light intensity in Lux")
    soil_moisture: float = Field(..., description="Soil Moisture percentage")
    soil_ph: float = Field(..., description="Soil pH level")
    electrical_conductivity: float = Field(..., description="EC in dS/m")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    sensor_id: str
    device_id: str
    zone_id: str
    crop_type: str
