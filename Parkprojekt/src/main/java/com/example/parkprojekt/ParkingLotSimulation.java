package com.example.parkprojekt;

import javafx.animation.TranslateTransition;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.util.Duration;

public class ParkingLotSimulation extends Application {

    private static final int PARKING_SPOT_WIDTH = 60;
    private static final int PARKING_SPOT_HEIGHT = 100;
    private static final int CAR_WIDTH = 50;
    private static final int CAR_HEIGHT = 80;
    private static final int PARKING_SPOT_X = 250;
    private static final int PARKING_SPOT_Y = 50;
    private static final int CAR_START_X = 50;
    private static final int CAR_START_Y = 50;
    private static final int CAR_END_X = 250;
    private static final int CAR_END_Y = 50;

    @Override
    public void start(Stage primaryStage) {
        // create a parking spot rectangle
        Rectangle parkingSpot = new Rectangle(PARKING_SPOT_X, PARKING_SPOT_Y, PARKING_SPOT_WIDTH, PARKING_SPOT_HEIGHT);
        parkingSpot.setFill(Color.LIGHTGRAY);
        parkingSpot.setStroke(Color.BLACK);

        // create a car rectangle
        Rectangle car = new Rectangle(CAR_START_X, CAR_START_Y, CAR_WIDTH, CAR_HEIGHT);
        car.setFill(Color.BLUE);
        car.setStroke(Color.BLACK);

        // create a translate transition to move the car to the parking spot
        TranslateTransition tt = new TranslateTransition(Duration.seconds(3), car);
        tt.setByX(PARKING_SPOT_X - CAR_START_X);
        tt.setByY(PARKING_SPOT_Y - CAR_START_Y);

        // create a root pane and add the parking spot and car to it
        StackPane root = new StackPane();
        root.getChildren().addAll(parkingSpot, car);

        // create a scene and set it on the stage
        Scene scene = new Scene(root, 400, 200);
        primaryStage.setScene(scene);

        // start the animation when the scene is shown
        primaryStage.setOnShown(event -> {
            tt.play();
        });

        // show the stage
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}