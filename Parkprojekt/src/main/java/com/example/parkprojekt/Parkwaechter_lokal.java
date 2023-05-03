package com.example.parkprojekt;

import org.eclipse.paho.client.mqttv3.MqttException;

import java.util.Arrays;

public class Parkwaechter_lokal extends Parkmanager {


    enum ParkplatzStatusSensor {FREI, BELEGT};


    ParkplatzStatusSensor []parkbuchtsensoren;

    static ParkplatzStatusSensor []parksensoren;

    mqtt_client client;
    int endIndex;
    boolean istVoll;
    int autoAnzahl;
    double rabattCm;
    double preisStunde;


    public Parkwaechter_lokal(String Parkbucht_id, String broker_id ) throws MqttException {
        parkbuchtsensoren = new ParkplatzStatusSensor[400];
        client = new mqtt_client(Parkbucht_id , broker_id);
        endIndex = 0;
        istVoll = false;
        autoAnzahl = 0;
    }

    public ParkplatzStatusSensor[] getParkbuchtsensoren() {
        return parkbuchtsensoren;
    }

    public int get_freierPlatz() {
        int freier_platz = 0;
        for (int i = 0; i <= parkbuchtsensoren.length; i++) {
            if (parkbuchtsensoren[i] == ParkplatzStatusSensor.FREI) {
                freier_platz ++;
            }
        }
        return freier_platz;
    }

    public int get_belegterPlatz() {
        int belegter_platz = 0;
        for (int i = 0; i <= parkbuchtsensoren.length; i++) {
            if (parkbuchtsensoren[i] == ParkplatzStatusSensor.BELEGT) {
                belegter_platz++;
            }
            if (belegter_platz > 380) {
                istVoll = true;
            }
        }
        return belegter_platz;
    }

    public String get_freierPlatz_segmente(){
        char[] freierPlatz = new char[parkbuchtsensoren.length];
            for(int i = 0; i < parkbuchtsensoren.length; i++) {
                if (parkbuchtsensoren[i] == ParkplatzStatusSensor.FREI) {
                    freierPlatz[i] = '_';
                }
                else {
                    freierPlatz[i] = 'X';
                }
            }
        return Arrays.toString(freierPlatz);
    }

    public boolean genugPlatzFuerAutoIngesamt(double autolaenge) {
        int freierPlatz = 0;

        for (int i = 0; i < parkbuchtsensoren.length; i++ ) {
            if (parkbuchtsensoren[i] == ParkplatzStatusSensor.FREI) {
                freierPlatz++;
                if (freierPlatz > (int) (autolaenge + 1.5)) {
                    return true;
                }
            }
        }

        return false;
    }

    public boolean genugPlatzFuerAuto(double autoLaenge) {
        int freierPlatz = 0;
        int maxLaenge = 0;
        for (int i = 0; i < parkbuchtsensoren.length; i++) {
            if (parkbuchtsensoren[i] == ParkplatzStatusSensor.FREI) {
                freierPlatz++;
                maxLaenge = Math.max(maxLaenge, freierPlatz);
                if (maxLaenge > (int) autoLaenge + 1.5) {
                    endIndex = i;
                    return true;
                }
            } else {
                freierPlatz = 0;
            }
        }
        return false;
    }

    public int getEndIndex() {
        return endIndex;
    }

    public boolean IstVoll() {
        return istVoll;
    }

    public void belegeParkplatz(double autolaenge) {
        int index = endIndex;
        int i = 0;
        while (i < ((int)autolaenge +1.5) ) {
            parkbuchtsensoren[index] = ParkplatzStatusSensor.BELEGT;
            index--;
            i++;
        }
        autoAnzahl++;
    }

}
