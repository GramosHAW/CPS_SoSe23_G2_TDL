package com.example.parkprojekt;

import org.eclipse.paho.client.mqttv3.MqttException;

public class Auto {

    double autoLeange;
    Parkwaechter_lokal pw;
    int []benoetigterPlatz;

    public Auto () throws MqttException {
        autoLeange = 4.9;
        pw = new Parkwaechter_lokal("1","2");
        benoetigterPlatz = new int[(int) (autoLeange + 1.5)];
    }

    public void belegeParkplatz() {
        if (pw.genugPlatzFuerAuto(autoLeange)) {

        }
    }
}
