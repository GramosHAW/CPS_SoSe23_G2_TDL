package App;
import Broker.Broker;
import java.util.Arrays;
import java.util.List;

public class App extends Broker {

    private List<String> topics;
    private Thread thread1;
    private Thread thread2;
    public App( ) {
        super( "App");
        topics = Arrays.asList("app/bereitZumParken", "app/steuerungFreigeben");
        thread1 =  new Thread(this::subscribenAuto);
        thread1.start();
        //publischenAuto();

    }

    public void subscribenAuto(){
        try {
            subscriben("appSub_client","app/steuerungFreigeben");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void publischenAuto(){
        try {
            pubischen("appPub_client",getTopics().get(0), "AutoSubscribe geschlossen");
            pubischen("appPub_client",getTopics().get(1), "AutoSubscribe geschlossen");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public List<String> getTopics() {
        return topics;
    }
}
