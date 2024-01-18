using UnityEngine;

public class UDPClient : MonoBehaviour
{
    [SerializeField] private string IPAdress = "172.16.10.102";
    [SerializeField] private int port = 12345;

    private UDPClientWrapper udpClient;
    private string messageToSend = "";

    // プロパティを導入
    public string MessageToSend
    {
        get { return messageToSend; }
        set { messageToSend = value; }
    }

    void Start()
    {
        udpClient = new UDPClientWrapper(IPAdress, port);
    }

    void FixedUpdate()
    {
        if (!string.IsNullOrEmpty(messageToSend))
        {
            udpClient.Send(messageToSend);
        }
    }

    private void OnDestroy()
    {
        udpClient.Close();
    }
}