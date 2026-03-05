# IoT Sensor Monitoring & Device Control System

## What This Is

This is a comprehensive IoT monitoring and automation platform built on Azure IoT Hub and Azure Functions. The system monitors multiple types of sensors and intelligently controls connected devices based on real-time sensor data and custom business logic.

## What It Does

This platform provides automated monitoring and control across various sensor types and device outputs:

- **Receives Sensor Data**: Collects real-time readings from multiple sensors across connected IoT devices via Azure IoT Hub
- **Processes Multiple Data Streams**: Each Azure Function is dedicated to a specific sensor type or monitoring task
- **Analyzes Conditions**: Evaluates sensor readings against configured thresholds and business rules
- **Controls Device Outputs**: Automatically sends commands to devices to trigger appropriate outputs and actions
- **Monitors Performance**: Logs all sensor data, decisions, and actions for tracking and analysis

## What's In This Repository

- **Multiple Azure Functions**: Each function monitors a specific sensor type or handles a particular automation task
  - **soil-moisture-trigger/**: Monitors soil moisture levels and controls irrigation relays
  - Additional functions can be added for temperature, humidity, light, pressure, motion, and other sensors
- **azurite/**: Local Azure Storage emulator data for development and testing

## Sensor Types & Use Cases

This system is designed to handle various monitoring and automation scenarios:

### Environmental Monitoring
- **Soil Moisture**: Automatic irrigation control based on moisture levels
- **Temperature & Humidity**: Climate control for greenhouses or indoor environments
- **Light Levels**: Automated lighting systems based on ambient conditions
- **Air Quality**: Ventilation control based on CO2 or particulate levels

### Industrial & Agricultural Applications
- **Pressure Sensors**: Monitor and control water systems or pneumatic equipment
- **Flow Sensors**: Track liquid or gas flow and trigger alerts or adjustments
- **Motion Sensors**: Security monitoring and automated access control
- **Level Sensors**: Tank or reservoir monitoring with automatic refill triggers

### Custom Automation
- Each Azure Function can implement unique logic for its specific sensor type
- Devices receive commands and execute outputs like activating relays, motors, valves, alarms, or displays
- Multi-sensor coordination for complex automation workflows

## What It's Used For

This solution is ideal for scenarios requiring:

- Real-time monitoring of environmental or industrial conditions
- Automated responses to changing sensor readings
- Remote control and management of distributed IoT devices
- Scalable monitoring across multiple locations or zones
- Data-driven decision making for resource optimization
- Reduced manual intervention in monitoring and control tasks

The platform helps improve efficiency, reduce waste, automate repetitive tasks, and maintain optimal conditions across various applications including agriculture, smart buildings, industrial automation, and environmental monitoring.

## How It Works

IoT devices equipped with various sensors continuously send telemetry data to Azure IoT Hub. Multiple Azure Functions subscribe to these data streams, with each function specialized for specific sensor types. When sensor data arrives, the appropriate function processes the information, applies business logic and thresholds, then sends direct method commands back to the devices to control outputs such as relays, motors, actuators, or other connected hardware. This creates a fully automated, event-driven monitoring and control system that operates in real-time.
