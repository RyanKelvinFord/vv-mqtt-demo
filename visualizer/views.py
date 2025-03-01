from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random
import csv
from datetime import datetime

# Global data storage for accumulated data
data_storage = []

def generate_mock_data():
    """Generate a single mock data entry."""
    return {
        "timestamp": datetime.now().isoformat(),
        "country_code": "DE",
        "value": round(random.uniform(0, 10), 2)
    }

# API to fetch the accumulated data
def get_mock_data(request):
    # Generate new data and add it to the storage
    new_data = generate_mock_data()
    data_storage.append(new_data)

    # Return the full data storage as JSON
    return JsonResponse(data_storage, safe=False)

# Dashboard view
def dashboard(request):
    # Reset data storage on page load
    global data_storage
    data_storage = []  # Clear previous data
    return render(request, "visualizer/dashboard.html")

# CSV download view
def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'

    writer = csv.writer(response)
    writer.writerow(["Timestamp", "Country Code", "Value"])  # Header row

    for entry in data_storage:
        writer.writerow([entry["timestamp"], entry["country_code"], entry["value"]])

    return response