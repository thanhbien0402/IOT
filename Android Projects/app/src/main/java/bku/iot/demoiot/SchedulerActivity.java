package bku.iot.demoiot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;
public class SchedulerActivity extends MainActivity{

    MQTTHelper mqttHelper;
    LabeledSwitch btnSched1,btnSched2,btnSched3;

    TextView notification;
    ImageButton temperature;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scheduler);

        btnSched1 = findViewById(R.id.btnScheduler1);
        btnSched2 = findViewById(R.id.btnScheduler2);
        btnSched3 = findViewById(R.id.btnScheduler3);
        notification = findViewById(R.id.txtNotification);
        temperature = findViewById(R.id.temperature_button);

        temperature.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SchedulerActivity.this, MainActivity.class);
                startActivity(intent);
                finish();
            }
        });
        btnSched1.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn == true){
                    sendDataMQTT("HCrystalH/feeds/nutnhan1","1");
                }else{
                    sendDataMQTT("HCrystalH/feeds/nutnhan1","0");
                }
            }
        });
        btnSched2.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("HCrystalH/feeds/nutnhan2", "1");
                }else {
                    sendDataMQTT("HCrystalH/feeds/nutnhan2", "0");
                }
            }
        });
        btnSched3.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("HCrystalH/feeds/nutnhan3", "1");
                }else {
                    sendDataMQTT("HCrystalH/feeds/nutnhan3", "0");
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
                Log.d("TEST", topic + "***"+ message.toString());
                 if(topic.contains("nutnhan1")){
                    if(message.toString().equals("1")){
                        btnSched1.setOn(true);
                    }else {
                        btnSched1.setOn(false);
                    }
                }else if(topic.contains("nutnhan2")){
                    if(message.toString().equals("1")){
                        btnSched2.setOn(true);
                    }else {
                        btnSched2.setOn(false);
                    }
                }else if(topic.contains("nutnhan3")){
                     if(message.toString().equals("1")){
                         btnSched3.setOn(true);
                     }else {
                         btnSched3.setOn(false);
                     }
                }else if(topic.contains("notification")){
                     notification.setText(message.toString());
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}
