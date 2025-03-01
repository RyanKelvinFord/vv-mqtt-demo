from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random
import csv
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json

# ==============================================
#  Existing Simulator Code (Unchanged)
# ==============================================

# Global data storage for accumulated data (existing simulator data)
data_storage = []

def generate_mock_data():
    """Generate a single mock data entry for the existing simulator."""
    return {
        "timestamp": datetime.now().isoformat(),
        "country_code": "DE",
        "value": round(random.uniform(0, 10), 2)
    }

def get_mock_data(request):
    """API to fetch the accumulated simulator data."""
    new_data = generate_mock_data()
    data_storage.append(new_data)
    return JsonResponse(data_storage, safe=False)

def dashboard(request):
    """Render the existing simulator dashboard."""
    global data_storage
    data_storage = []  # Clear previous data each time user visits
    return render(request, "visualizer/dashboard.html")

def download_csv(request):
    """Allows CSV download of the existing simulator data."""
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'

    writer = csv.writer(response)
    writer.writerow(["Timestamp", "Country Code", "Value"])  # Header row

    for entry in data_storage:
        writer.writerow([entry["timestamp"], entry["country_code"], entry["value"]])

    return response

# ==============================================
#  New "Motor" Dashboard and API Code
# ==============================================

# A separate storage for the new motor-related data
motor_data_storage = []

def generate_motor_data():
    """
    Generate a single mock data entry for the motor dashboard.
    - Motor running time in hours:minutes
    - Water level height: 0–150 cm
    - Motor activation switch: Open/Close
    """
    hours = random.randint(0, 24)
    minutes = random.randint(0, 59)
    water_level = random.randint(0, 150)
    motor_status = random.choice(["Open", "Close"])  # Randomly pick status

    return {
        "timestamp": datetime.now().isoformat(),
        "motor_time": f"{hours}h {minutes}m",
        "water_level": water_level,
        "motor_status": motor_status
    }

def get_motor_data(request):
    """API endpoint to fetch motor-related data."""
    new_data = generate_motor_data()
    motor_data_storage.append(new_data)
    return JsonResponse(motor_data_storage, safe=False)

def motor_dashboard(request):
    """
    Renders a new dashboard page that displays:
      - motor run time,
      - water level,
      - motor switch status
    """
    global motor_data_storage
    motor_data_storage = []  # Reset data each new load
    return render(request, "visualizer/motor_dashboard.html")

def download_motor_csv(request):
    """Allows CSV download of the motor dashboard data."""
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        f'attachment; filename="motor_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
    )
    writer = csv.writer(response)
    writer.writerow(["Timestamp", "Motor Running Time", "Water Level (cm)", "Motor Status"])

    for entry in motor_data_storage:
        writer.writerow([
            entry["timestamp"],
            entry["motor_time"],
            entry["water_level"],
            entry["motor_status"],
        ])

    return response

# ==============================================
#  MQTT Data Transfer Testing + Visualization
# ==============================================

# In-memory storage for MQTT data
mqtt_data_storage = []

@csrf_exempt
def mqtt_data_endpoint(request):
    """
    Simple endpoint to demonstrate how you might receive/send MQTT-related data.
    In a real IoT scenario, you'd likely use paho-mqtt or similar.
      - GET returns a simple JSON message
      - POST expects JSON payload and returns a success message
    """
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            # Store the payload and a timestamp
            stored_entry = {
                "timestamp": datetime.now().isoformat(),
                "payload": payload,
                # If there's a 'value' in payload, store it so we can chart it
                "value": payload.get("value"),
            }
            mqtt_data_storage.append(stored_entry)
            return JsonResponse({"status": "success", "stored_entry": stored_entry})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({
            "message": "MQTT endpoint is running. Send POST to simulate data reception."
        })

def get_mqtt_data(request):
    """
    Returns all MQTT data stored so far. The MQTT dashboard can call this endpoint
    to fetch and visualize the data.
    """
    return JsonResponse(mqtt_data_storage, safe=False)

def mqtt_dashboard(request):
    """
    Renders a new dashboard page to visualize posted MQTT data in a table & chart.
    """
    return render(request, "visualizer/mqtt_dashboard.html")