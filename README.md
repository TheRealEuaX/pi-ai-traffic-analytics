# Overview
Edge Traffic Analytics is a lightweight computer vision system designed to run entirely on-device using a Raspberry Pi 4 and camera module.
The system detects passing vehicles, classifies their brand, logs structured metadata, and exposes real-time analytics through a local dashboard without cloud dependency.

# System architecture
Camera -> Motion trigger -> Vehicle detection -> Region crop -> Brand classification -> Logging -> Dashboard

Stage 1 – Vehicle Detection
Model: YOLOv8 (nano variant)
Detects vehicle bounding boxes
Optimized for low-latency edge inference

Stage 2 – Brand Classification
Lightweight CNN (MobileNet-based)
Runs only on detected vehicle crops
Outputs brand + confidence score

Data Layer
SQLite database
Timestamped records
Image storage with metadata

Dashboard
Flask-based web interface
Real-time vehicle count
Brand distribution analytics
Recent detections preview

# Hardware 
Raspberry Pi 4 (4GB)
Raspberry Pi Camera Module
