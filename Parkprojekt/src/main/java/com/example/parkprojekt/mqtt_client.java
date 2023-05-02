package com.example.parkprojekt;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class mqtt_client {

    String brokerUrl = "tcp://localhost:1883";
    String clientId = "my-client-id";
    MqttClient mqttClient = new MqttClient(brokerUrl, clientId);

    public mqtt_client(String client, String broker) throws MqttException {

    }


    public void publish(String topic, String payload) throws MqttException {
        String topic_ = topic;
        String payload_ = payload;
        MqttMessage message = new MqttMessage(payload.getBytes());
        mqttClient.publish(topic, message);
    }

    public void subscribe(String topic) throws MqttException {
        String topic_ = topic;
        mqttClient.subscribe(topic_, (_topic, message) -> {
            String payload = new String(message.getPayload());
            System.out.println("Received message on topic " + topic + ": " + payload);
        });
    }



}
