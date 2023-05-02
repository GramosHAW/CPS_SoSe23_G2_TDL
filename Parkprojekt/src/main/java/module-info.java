module com.example.parkprojekt {
    requires javafx.controls;
    requires javafx.fxml;
    requires org.eclipse.paho.client.mqttv3;



    opens com.example.parkprojekt to javafx.fxml;
    exports com.example.parkprojekt;
}