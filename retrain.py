import os

if os.path.exists("drift_detected.flag"):
    print("Retraining triggered")
else:
    print("No drift detected")