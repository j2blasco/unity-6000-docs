* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.html

# DeviceType
enumeration
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Enumeration for [SystemInfo.deviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html), denotes a coarse grouping of kinds of devices.
**Universal Windows Platform** : tablets are treated as desktop machines, thus [DeviceType.Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Handheld.html) will only be returned for Windows Phones and IoT family devices.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script checks what device type the Application[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) is running on and outputs this to the console  
  
using UnityEngine;  
  
public class DeviceTypeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //This is the Text for the Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) at the top of the screen
    string m_DeviceType;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
//Output the device type to the console window
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Device[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.Device.html) type : " + m_DeviceType);  
  
        //Check if the device running this is a console
        if (SystemInfo.deviceType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html) == DeviceType.Console[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Console.html))
        {
            //Change the text of the label
            m_DeviceType = "Console";
        }  
  
        //Check if the device running this is a desktop
        if (SystemInfo.deviceType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html) == DeviceType.Desktop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Desktop.html))
        {
            m_DeviceType = "Desktop";
        }  
  
        //Check if the device running this is a handheld
        if (SystemInfo.deviceType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html) == DeviceType.Handheld[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Handheld.html))
        {
            m_DeviceType = "Handheld[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html)";
        }  
  
        //Check if the device running this is unknown
        if (SystemInfo.deviceType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html) == DeviceType.Unknown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Unknown.html))
        {
            m_DeviceType = "Unknown";
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Unknown.html) | Device type is unknown. You should never see this in practice.  
[Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Handheld.html) | A handheld device like mobile phone or a tablet.  
[Console](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Console.html) | A stationary gaming console.  
[Desktop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.Desktop.html) | Desktop or laptop computer.  
* * *
