from kitt import KITT, DriftCar
from utils import summarize_scores

# Aracı başlat
car = DriftCar()
car.start_engine()
car.prepare_to_drive()
car.start_drive()
car.scan_surroundings()
car.perform_drift()
car.save_drift_scores()

# Drift analiz
summarize_scores(car.drift_scores)