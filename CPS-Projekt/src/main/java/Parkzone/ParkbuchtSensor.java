package Parkzone;

import Utils.Utils;

import java.util.ArrayList;
import java.util.List;

public class ParkbuchtSensor {

    private List<Boolean> parkbuctSensor;
    private int laengeParkbucht;
    private Utils utils;

    public ParkbuchtSensor() {
        utils = new Utils();
        //Länge als Random eingeben
        laengeParkbucht = utils.getLaengeParkbucht();
        parkbuctSensor = new ArrayList();
    }

    public List<Boolean> getParkbuctSensor() {
        return parkbuctSensor;
    }

    public void setParkbuctSensor(int index, boolean aktuellSensor) {
        if (!(index < 0 || index > parkbuctSensor.size())) {
            parkbuctSensor.set(index, aktuellSensor);
        }
    }
}

