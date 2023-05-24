package Auto;
import Broker.Broker;
import java.util.Arrays;
import java.util.List;

public class Auto extends Broker {
    private List<String> topics;
    private Thread thread1;
    public Auto( ) {
        super( "Auto");
        topics = Arrays.asList("auto/autoStatus", "auto/sensorWert");
        thread1 =  new Thread(this::subscribenAuto);
        thread1.start();
        publischenAuto();
    }

    public void subscribenAuto(){
        try {
            subscriben("autoSub_client", "chaossensor/1/data");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void publischenAuto(){
        while (true)try {
            pubischen("autoPub_client", getTopics().get(0), "co2: 20, länge: 1m, 2342");
            pubischen("autoPub_client", getTopics().get(1), "co2: 23, länge: 2m, 2343");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public List<String> getTopics() {
        return topics;
    }
}
