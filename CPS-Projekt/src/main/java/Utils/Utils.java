package Utils;

import java.util.Random;

public class Utils {
    private final int ABSTAND_SENSOR = 5;
    private int laengeParkbucht;

    public void setLaengeParkbucht(int laengeParkbucht) {
        this.laengeParkbucht = laengeParkbucht;
    }

    public Utils(){
        Random random = new Random();
        laengeParkbucht = random.nextInt(100 - 90 + 1 ) +90;
    }

    public int getABSTAND_SENSOR() {
        return ABSTAND_SENSOR;
    }

    public int getLaengeParkbucht() {
        return laengeParkbucht;
    }

}
