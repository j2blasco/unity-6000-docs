* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetJoystickNames.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetJoystickNames
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
## Declaration
public static string[] GetJoystickNames(); 
### Returns
**string[]** Returns an array of joystick and gamepad device names. 
### Description
Retrieves a list of input device names corresponding to the index of an Axis configured within Input Manager.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
The strings returned are taken from the connected device's "friendly name" as reported by the operating system. That is, the names are not fixed and will likely vary between devices, drivers, and the OS itself.  
  
These strings are intended for use within input configuration screens - this way, instead of showing labels like "Joystick 1", you can show more meaningful names like "Logitech WingMan". To read values from different joysticks, you need to assign respective axes for the number of joysticks you want to support in the Input Manager.  
  
The position of a joystick in this array corresponds to the joystick number, i.e. the name in position 0 of this array is for the joystick that feeds data into 'Joystick 1' in the Input Manager, the name in position 1 corresponds to 'Joystick 2', and so on. Note that some entries in the array may be blank if no device is connected for that joystick number.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints a joystick name if movement is detected.  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // requires you to set up axes "Joy0X" - "Joy3X" and "Joy0Y" - "Joy3Y" in the Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) Manager
        for (int i = 0; i < 4; i++)
        {
            if (Mathf.Abs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html)(Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Joy" + i + "X")) > 0.2 ||
                Mathf.Abs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html)(Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Joy" + i + "Y")) > 0.2)
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Input.GetJoystickNames[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetJoystickNames.html)()[i] + " is moved");
            }
        }
    }
}

```

* * *
