import random
from datetime import datetime
from media import MediaPlayer

class KITT:
    def __init__(self, name="KITT"):
        self.name = name
        self.engine_on = False
        self.prepared = False
        self.systems = {"scanner": True, "engine": True, "AI": True}
        self.media = MediaPlayer()
        self.drift_scores = []
        self.fuel = 100.0

    # Diğer tüm metodlar buraya eklenir (start_engine, start_drive vs.)

class DriftCar(KITT):
    def perform_drift(self):
        print("DriftCar özel drift yeteneği aktif...")
        score = super().perform_drift()
        if score >= 8:
            print("Harika drift!")
        elif score <= 3:
            print("Daha çok pratik yapmalisin.")
        return score