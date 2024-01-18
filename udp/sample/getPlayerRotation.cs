using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class getPlayerRotation : MonoBehaviour
{
    [SerializeField] private UDPClient _udpClient;
    [SerializeField] private GameObject _playerHead;
    // Update is called once per frame
    void Update()
    {
        float _playerRotationYaw = _playerHead.transform.localEulerAngles.y > 180 ? (_playerHead.transform.localEulerAngles.y - 360) : _playerHead.transform.localEulerAngles.y;
        float _clampedPlayerRotationYaw = Mathf.Clamp(_playerRotationYaw, -90, 90);
        _udpClient.MessageToSend = _clampedPlayerRotationYaw.ToString() + ",0,0";
    }
}
