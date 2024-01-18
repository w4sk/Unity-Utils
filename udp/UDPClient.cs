using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class UDPClient : MonoBehaviour
{
    [SerializeField] private string IPAdress = "172.16.10.102";
    [SerializeField] private int port = 12345;

    private UDPClientWrapper udpClient;

    void Start()
    {
        udpClient = new UDPClientWrapper(IPAdress, port);
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            string message = "Send Message";
            byte[] data = Encoding.UTF8.GetBytes(message);
            udpClient.Send(data, data.Length);
        }
    }

    private void OnDestroy()
    {
        udpClient.Close();
    }
}