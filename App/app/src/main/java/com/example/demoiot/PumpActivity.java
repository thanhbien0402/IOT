package com.example.demoiot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.content.Intent;
import android.widget.Button;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import java.nio.charset.Charset;

public class PumpActivity extends AppCompatActivity {
    MQTTHelper mqttHelper;
    TextView txtNotification;

    LabeledSwitch btn1;
    ImageButton home,scheduler,temperature,lamp,pump;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pump);

        txtNotification = findViewById(R.id.txtNotification);
        home = findViewById(R.id.home_button);
        temperature = findViewById(R.id.temperature_button);
        lamp = findViewById(R.id.lamp_button);
        pump = findViewById(R.id.pump_button);
        scheduler = findViewById(R.id.scheduler_button);
        home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(PumpActivity.this, MainActivity.class);
                startActivity(intent);
                finish();
            }
        });
        temperature.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(PumpActivity.this, TemperatureActivity.class);
                startActivity(intent);
                finish();
            }
        });
        pump.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(PumpActivity.this, PumpActivity.class);
                startActivity(intent);
                finish();
            }
        });
        lamp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(PumpActivity.this, LampActivity.class);
                startActivity(intent);
                finish();
            }
        });
//        scheduler.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent intent = new Intent(PumpActivity.this, SchedulerActivity.class);
//                startActivity(intent);
//                finish();
//            }
//        });
        btn1.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("bcthanh/feeds/nutnhan1", "1");
                }
                else {
                    sendDataMQTT("bcthanh/feeds/nutnhan1", "0");
                }
            }
        });
        startMQTT();
    }
    public void sendDataMQTT(String topic, String value){
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){
        }
    }
    public void startMQTT(){
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                if (topic.contains("nutnhan1")){
                    if (message.toString().equals("1")){
                        btn1.setOn(true);
                    }
                    else btn1.setOn(false);
                }
            }
            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {
            }
        });
    }
}