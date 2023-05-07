import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Car extends Frame {
    private int speed;
    private int numberOfWheels;
    private int x, y;
    private BufferedImage carImage;

    public Car(int numberOfWheels, int speed) {
        super("Car Simulation");
        this.numberOfWheels = numberOfWheels;
        this.speed = speed;
        x = 0;
        y = 100;
        try {
            carImage = ImageIO.read(new File("src\\main\\java\\Utils\\Bilder\\klein.jpeg"));

        } catch (IOException e) {
            e.printStackTrace();
        }
        setSize(1000, 900);
        setVisible(true);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                System.exit(0);
            }
        });
    }

    public void paint(Graphics g) {
        g.drawImage(carImage, x, y, 100, 50, null); // Hier wird das Auto-Bild gezeichnet
        g.drawString("Das Auto fährt mit " + numberOfWheels + " Rädern und einer Geschwindigkeit von " + speed + " km/h.", 50, 200);
    }

    public void move() {
        x += speed;
        if (x > getWidth()) {
            x = -100;
        }
        repaint();
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getSpeed() {
        return speed;
    }

    public static void main(String[] args) {
        Car car = new Car(4, 5);
        while (true) {
            car.move();
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
