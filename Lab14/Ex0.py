import importlib

packages = ["scipy", "statsmodels", "matplotlib"]

print("--- Package Installation Report ---")
for package in packages:
    try:
        importlib.import_module(package)
        print(f"[OK] {package} is installed.")
    except ImportError:
        print(f"[ERROR] {package} is NOT installed.")