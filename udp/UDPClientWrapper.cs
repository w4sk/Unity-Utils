using UnityEngine;
using System.Net.Sockets;
using System.Text;

public class UDPClientWrapper: MonoBehaviour
{
    private UdpClient client;
    private string host;
    private int port;

    public UDPClientWrapper(string host, int port)
    {
        this.host = host;
        this.port = port;
        client = new UdpClient();
        client.Connect(host, port);
    }

    public void Send(string message)
    {
        byte[] data = Encoding.UTF8.GetBytes(message);
        client.Send(data, data.Length);
    }

    public void Close()
    {
        client.Close();
    }
}