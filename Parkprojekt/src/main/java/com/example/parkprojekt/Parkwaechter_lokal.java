package com.example.parkprojekt;

import java.util.Arrays;

public class Parkwaechter_lokal extends Parkwaechter_zentral {


    enum ParkplatzStatusSensor {FREI, BELEGT, RESERVIERT};

    ParkplatzStatusSensor []parkbuchtsensoren;
    mqtt_client client;
    int endIndex;


    public Parkwaechter_lokal(String Parkbucht_id, String broker_id ) {
        parkbuchtsensoren = new ParkplatzStatusSensor[400];
        client = new mqtt_client(Parkbucht_id, String broker_id);
        endIndex = 0;

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

    public void belegeParkplatz(double autolaenge) {
        int i = 0;
        while (i < ((int)autolaenge +1.5) ) {
            parkbuchtsensoren[endIndex] = ParkplatzStatusSensor.BELEGT;
            endIndex--;
            i++;
        }
    }

}
