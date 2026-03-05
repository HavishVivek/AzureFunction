# Soil Moisture Monitoring System

## What This Is

An automated soil moisture monitoring and irrigation control system built on Azure IoT Hub and Azure Functions. The system monitors soil moisture levels from IoT devices and automatically controls irrigation relays based on real-time sensor readings.

## What It Does

This system provides automated irrigation management:

- **Receives Soil Moisture Data**: Collects real-time moisture readings from soil sensors connected to IoT devices via Azure IoT Hub
- **Analyzes Moisture Levels**: Evaluates sensor readings against a configured threshold to determine irrigation needs
- **Controls Irrigation**: Automatically sends relay commands to devices to turn irrigation on or off based on soil conditions
- **Logs Activity**: Records all sensor data, decisions, and relay commands for monitoring and analysis

## What's In This Repository

### soil-moisture-trigger/
An Azure Function that monitors soil moisture and controls irrigation relays. Contains:
- **function_app.py** - Main function that processes Event Hub messages from IoT Hub, reads soil moisture values, evaluates threshold conditions (450), and sends direct method commands to turn relays on or off
- **requirements.txt** - Python dependencies including azure-functions and azure-iot-hub libraries
- **host.json** - Azure Functions runtime configuration with logging and extension bundle settings
- **local.settings.json** - Local development settings for connection strings and environment variables
- **.vscode/extensions.json** - Recommended VS Code extensions for Azure Functions development
- **.gitignore** - Files to exclude from version control

### azurite/
Local Azure Storage emulator data for development and testing. Contains:
- Database files for blob, queue, and table storage emulation
- Configuration files for the Azurite emulator
- Local storage data used during function testing

## How It Works

IoT devices equipped with soil moisture sensors continuously send telemetry data to Azure IoT Hub. The Azure Function subscribes to the Event Hub-compatible endpoint and receives these messages in real-time. When a message arrives, the function:

1. Decodes and parses the incoming JSON message
2. Extracts the device ID from IoT Hub metadata
3. Reads the soil moisture value from the message payload
4. Compares the moisture level against a threshold (450)
5. Determines whether irrigation is needed (moisture > 450 triggers relay on, otherwise relay off)
6. Sends a direct method command back to the IoT device to control the relay
7. Logs the decision and action taken

This creates an event-driven, automated irrigation system that responds to changing soil conditions in real-time without manual intervention.

## Use Case

This solution is designed for automated irrigation management in:
- Home gardens and landscaping
- Small-scale agriculture or greenhouses
- Plant monitoring systems
- Water conservation applications
- Smart farming projects

The system helps optimize water usage, prevent over or under-watering, and automate irrigation tasks based on actual soil conditions rather than fixed schedules.
