# Soil Moisture Monitoring and Irrigation Control System

An automated soil moisture monitoring and irrigation control system built on Azure IoT Hub and Azure Functions. This system monitors real-time soil moisture levels from IoT devices and automatically controls irrigation relays based on sensor readings.

## What This System Does

This is an event-driven automation system that provides intelligent irrigation management:

- **Real-Time Monitoring**: Receives continuous soil moisture data from IoT devices equipped with moisture sensors via Azure IoT Hub
- **Intelligent Analysis**: Evaluates sensor readings against configurable thresholds to determine irrigation needs
- **Automated Control**: Sends direct method commands to IoT devices to turn irrigation relays on or off based on soil conditions
- **Activity Logging**: Records all sensor data, decisions, and relay commands for monitoring and troubleshooting

## How It Works

The system creates an automated feedback loop between soil sensors and irrigation controls:

1. IoT devices with soil moisture sensors continuously send telemetry data to Azure IoT Hub
2. The Azure Function subscribes to the Event Hub-compatible endpoint and receives messages in real-time
3. When a message arrives, the function decodes the payload and extracts the soil moisture value
4. The moisture level is compared against a threshold to determine if irrigation is needed
5. A direct method command is sent back to the IoT device to control the relay
6. All actions and decisions are logged for monitoring

This creates a fully automated irrigation system that responds to changing soil conditions without manual intervention, optimizing water usage and preventing over or under-watering.

## Repository Structure

### SoilData/

The main project directory containing the Azure Function and development tools:

#### soil-moisture-trigger/
The Azure Function that processes IoT Hub messages and controls irrigation. This is the core logic that:
- Receives Event Hub messages from IoT Hub
- Parses soil moisture sensor readings
- Evaluates threshold conditions
- Sends relay control commands to devices
- Logs all activities

#### azurite/
Local Azure Storage emulator data for development and testing. Contains database files for blob, queue, and table storage emulation used during local function development.

## Use Cases

This solution is designed for automated irrigation management in:

- **Home Gardens & Landscaping**: Maintain optimal soil moisture for lawns, flower beds, and vegetable gardens
- **Small-Scale Agriculture**: Automate irrigation for small farms or greenhouses
- **Plant Monitoring Systems**: Track and respond to plant hydration needs in real-time
- **Water Conservation**: Reduce water waste by irrigating only when soil conditions require it
- **Smart Farming Projects**: Build IoT-enabled agricultural automation systems

## Technology Stack

- **Azure IoT Hub**: Device-to-cloud messaging and device management
- **Azure Functions**: Serverless event-driven compute for processing messages
- **Python**: Function runtime and logic implementation
- **Azurite**: Local Azure Storage emulator for development
- **Event Hub**: Event streaming integration with IoT Hub

## Key Features

- **Event-Driven Architecture**: Responds immediately to sensor readings without polling
- **Serverless Deployment**: Runs on Azure Functions for automatic scaling and minimal maintenance
- **Bidirectional Communication**: Receives telemetry and sends commands to devices
- **Real-Time Decision Making**: Evaluates soil conditions and controls irrigation instantly
- **Local Development Support**: Includes Azurite for testing without cloud resources
- **Extensible Design**: Can be adapted for different sensor types, thresholds, and control mechanisms

## Benefits

- **Water Conservation**: Irrigates only when soil actually needs water, reducing waste
- **Automation**: Eliminates need for manual watering schedules or intervention
- **Optimal Plant Health**: Maintains ideal soil moisture levels for plant growth
- **Real-Time Response**: Reacts immediately to changing soil conditions
- **Cost Efficient**: Serverless architecture means you only pay for actual usage
- **Scalable**: Can manage multiple devices and sensors from a single function

## Development and Testing

The repository includes everything needed for local development:

- Azure Function project with all necessary configuration files
- Azurite local storage emulator for testing without Azure resources
- VS Code workspace configuration for Azure Functions development
- Dependency management through requirements files

The system can be developed and tested entirely locally before deploying to Azure.