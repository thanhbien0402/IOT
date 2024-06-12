package com.example.demoiot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

public class MainActivity extends AppCompatActivity {
    MQTTHelper mqttHelper;
    TextView txtTemp, txtHumid, txtLight;
    LabeledSwitch btn1, btn2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        txtTemp = findViewById(R.id.txtTemperature);
//        txtHumid = findViewById(R.id.txtHumidity);
//        txtLight = findViewById(R.id.txtLight);
//        btn1 = findViewById(R.id.btn1);
//        btn2 = findViewById(R.id.btn2);

//        btn1.setOnToggledListener(new OnToggledListener() {
//            @Override
//            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
//                if (isOn == true){
//                    sendDataMQTT("bcthanh/feeds/nutnhan1", "1");
//                }
//                else {
//                    sendDataMQTT("bcthanh/feeds/nutnhan1", "0");
//                }
//            }
//        });
        btn2.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("bcthanh/feeds/nutnhan2", "1");
                }
                else {
                    sendDataMQTT("bcthanh/feeds/nutnhan2", "0");
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
                Log.d("TEST", topic + "***" + message.toString());
                if (topic.contains("cambien1")){
                    txtTemp.setText(message.toString() + "℃");
                }
                else if (topic.contains("cambien2")){
                    txtHumid.setText(message.toString() + "%");
                }
                else if (topic.contains("cambien3")){
                    txtLight.setText(message.toString() + " lux");
                }
                else if (topic.contains("nutnhan1")){
                    if (message.toString().equals("1")){
                        btn1.setOn(true);
                    }
                    else btn1.setOn(false);
                }
                else if (topic.contains("nutnhan2")){
                    if (message.toString().equals("1")){
                        btn2.setOn(true);
                    }
                    else btn2.setOn(false);
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}