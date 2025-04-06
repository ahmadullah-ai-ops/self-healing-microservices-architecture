import random

def autonomous_decision(service_metrics):
    # Simulate a simple decision-making process
    if service_metrics['cpu_usage'] > 80 or service_metrics['error_rate'] > 0.05:
        print("Decision: Scale up service or restart.")
        return "scale_up"
    print("Decision: Service is healthy.")
    return "healthy"

# Example usage
service_metrics = {
    'cpu_usage': random.randint(60, 90),
    'error_rate': random.random()
}
decision = autonomous_decision(service_metrics)
print(f"Autonomous Decision: {decision}")

