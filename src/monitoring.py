import requests
import time

def monitor_service(service_url):
    try:
        response = requests.get(service_url)
        if response.status_code != 200:
            print(f"Service failed: {service_url}")
            return False
        print(f"Service healthy: {service_url}")
        return True
    except Exception as e:
        print(f"Error accessing {service_url}: {str(e)}")
        return False

def monitor_system():
    services = ["http://localhost:5000", "http://localhost:5001"]
    while True:
        for service in services:
            healthy = monitor_service(service)
            if not healthy:
                print(f"Triggering recovery for {service}")
                trigger_recovery(service)
        time.sleep(10)

def trigger_recovery(service_url):
    print(f"Restarting {service_url}... (simulated recovery action)")
    # You can add logic to trigger Kubernetes auto-restarts or Docker commands here

if __name__ == "__main__":
    monitor_system()

