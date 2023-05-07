package Broker;
import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class Broker {
    private String broker = "tcp://localhost:1883";
    private static final int qos = 2;
    private String klasse;

    public Broker(String klasse){
        this.klasse = klasse;
    }
    public void pubischen(String clientid, String topic, String content) throws MqttException {
        MqttClient client = new MqttClient(broker, clientid, new MemoryPersistence());
        MqttConnectOptions options = new MqttConnectOptions();
        options.setConnectionTimeout(60);
        options.setKeepAliveInterval(60);
        // connect
        client.connect(options);
        // create message and setup QoS
        MqttMessage message = new MqttMessage(content.getBytes());
        message.setQos(qos);
        // publish message
        client.publish(topic, message);
        System.out.println("Klasse " + klasse + " Published" + " topic: " + topic);
        System.out.println("Klasse " + klasse + " message content: " + content);
        System.out.println();
        // disconnect
        client.disconnect();
        // close client
        client.close();
    }

    public void subscriben(String clientid, String topic) throws Exception{
        MqttClient client = new MqttClient(broker, clientid, new MemoryPersistence());
        // connect options
        MqttConnectOptions options = new MqttConnectOptions();
        options.setConnectionTimeout(60);
        options.setKeepAliveInterval(60);
        // setup callback
        client.setCallback(new MqttCallback() {

            public void connectionLost(Throwable cause) {
                System.out.println("Klasse " + klasse + " connectionLost: " + cause.getMessage());
            }

            public void messageArrived(String topic, MqttMessage message) {
                System.out.println("Klasse " + klasse + " Subscriber" + " topic: " + topic);
                //System.out.println("Klasse " + klasse + " Qos: " + message.getQos());
                System.out.println("Klasse " + klasse + " message content: " + new String(message.getPayload()));
                System.out.println();
            }

            public void deliveryComplete(IMqttDeliveryToken token) {
                System.out.println("deliveryComplete---------" + token.isComplete());
            }

        });
        client.connect(options);
        client.subscribe(topic, qos);

    }

}
