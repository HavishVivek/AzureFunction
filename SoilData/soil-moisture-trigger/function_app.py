import os
import json
import logging
import azure.functions as func
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod

app = func.FunctionApp()

@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="iothub-ehub-pi3b-hub-58039924-a115b11e53",  # Replace with your IoT Hub Event Hub-compatible name
    connection="IOT_HUB_CONNECTION_STRING"
)
def iot_hub_trigger(event: func.EventHubEvent):
    try:
        # Decode the incoming Event Hub message
        message_body = event.get_body().decode("utf-8")
        logging.info(f"Python EventHub trigger received event: {message_body}")

        # Parse JSON payload
        body = json.loads(message_body)

        # Get device ID from IoT Hub metadata
        device_id = event.iothub_metadata.get("connection-device-id", "unknown")
        logging.info(f"Received message from device {device_id}: {body}")

        # Read soil moisture value
        soil_moisture = body.get("soil_moisture", 0)

        # Determine relay command
        if soil_moisture > 450:
            direct_method = CloudToDeviceMethod(method_name="relay_on", payload={})
        else:
            direct_method = CloudToDeviceMethod(method_name="relay_off", payload={})

        logging.info(f"Sending direct method '{direct_method.method_name}' to device {device_id}")

        # Initialize IoTHubRegistryManager
        registry_manager_connection_string = os.environ["REGISTRY_MANAGER_CONNECTION_STRING"]
        registry_manager = IoTHubRegistryManager(registry_manager_connection_string)

        # Invoke direct method
        registry_manager.invoke_device_method(device_id, direct_method)

        logging.info("Direct method request sent successfully!")

    except json.JSONDecodeError:
        logging.error(f"Received invalid JSON: {message_body}")
    except Exception as e:
        logging.error(f"Error processing IoT Hub message: {e}")