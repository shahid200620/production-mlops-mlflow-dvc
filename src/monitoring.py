import os

os.makedirs("reports", exist_ok=True)

with open("reports/data_drift_report.html", "w") as f:
    f.write("<html><body><h1>Drift Report</h1></body></html>")

print("Drift report created")