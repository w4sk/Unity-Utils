using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using M2MqttUnity;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

public class mqttReceiver : M2MqttUnityClient
{
    [Header("MQTT topics")]
    [Tooltip("Topic to subscribe to subscribe. !!!ATTENTION!!! multi-level wildcard # subscribes to all topics")]
    [SerializeField] private string topicSubscribe = "python/mqtt"; // topic to subscribe !!! The multi-level wildcard # is used to subscribe to all the topics. Attention i if #, subscribe to all topics. if MQTT is on data plan

    //using C# Propertiy Get/Set and event listener to reduce Update overhead in the controlled objects
    private string m_msg;

    public string msg
    {
        get { return m_msg; }
        set
        {
            if (m_msg == value) return;
            m_msg = value;
            if (OnMessegeArrived != null) OnMessegeArrived(m_msg);
        }
    }

    public event OnMessageArrivedDelegate OnMessegeArrived;
    public delegate void OnMessageArrivedDelegate(string newMsg);

    // using C# Property Get/Set and evernt Listner to expose the connection status
    private bool m_isConnected;

    public bool isConnected
    {
        get {return m_isConnected;}

        set
        {
            if (m_isConnected == value) return;
            m_isConnected = value;
            if (OnConnectionSucceeded != null) OnConnectionSucceeded(isConnected);
        }
    }

    public event OnConnectionSucceededDelegate OnConnectionSucceeded;
    public delegate void OnConnectionSucceededDelegate(bool isConnected);

    // a list to store the messages
    private List<string> eventMessages = new List<string>();

    void SetEncrypted(bool isEncrypted)
    {
        this.isEncrypted = isEncrypted;
    }

    // Remove 'public' to from the following method
    void StoreMessage(string eventMsg)
    {
        if (eventMessages.Count > 50)
        {
            eventMessages.RemoveAt(0);
        }
        eventMessages.Add(eventMsg);
    }

    protected override void OnConnecting()
    {
        base.OnConnecting();
        Debug.Log("Connecting to broker");
    }

    protected override void OnConnected()
    {
        base.OnConnected();
        Debug.Log("Connected to broker");
        isConnected = true;
    }

    protected override void OnConnectionFailed(string errorMessage)
    {
        Debug.Log("CONNECTION FAILED! " + errorMessage);
    }

    protected override void OnDisconnected()
    {
        Debug.Log("Disconnected from broker");
        isConnected = false;
    }

    protected override void OnConnectionLost()
    {
        Debug.Log("CONNECTION LOST!");
    }

    protected override void SubscribeTopics()
    {
        client.Subscribe(new string[] { topicSubscribe }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
    }

    protected override void UnsubscribeTopics()
    {
        client.Unsubscribe(new string[] { topicSubscribe });
    }

    protected override void Start()
    {
        base.Start();
    }

    protected override void DecodeMessage(string topic, byte[] message)
    {
        // The message is decoded
        msg = System.Text.Encoding.UTF8.GetString(message);
        Debug.Log("Received: " + msg);
        Debug.Log("from topic: " + m_msg);

        StoreMessage(msg);
    }

    protected override void Update()
    {
        base.Update();
    }

    private void OnDestory()
    {
        Disconnect();
    }
}
