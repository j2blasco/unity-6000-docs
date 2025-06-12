* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html

#  [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html).generation
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
[iOS.DeviceGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration.html) generation; 
### Description
The generation of the device. (Read Only)
For information on the possible values, see [DeviceGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration.html).
```
using UnityEngine;
using UnityEngine.iOS;  
  
public class DeviceGenerationExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string m_DeviceGeneration = "Undefined";  
  
    void Start()
    {
        // Check if the device running this is an "iPhone 14 Pro Max"
        if (Device.generation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) == DeviceGeneration.iPhone14ProMax[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration-iPhone14ProMax.html))
        {
            m_DeviceGeneration = "iPhone 14 Pro Max";
        }
        
        // Check if the device running this is an 'iPad Mini (6th generation)"
        if (Device.generation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) == DeviceGeneration.iPadMini6Gen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration-iPadMini6Gen.html))
        {
            m_DeviceGeneration = "iPad Mini (6th generation)";
        }
        
        // Check if the device running this is an "iPod Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) (7th generation)"
        if (Device.generation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) == DeviceGeneration.iPodTouch7Gen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration-iPodTouch7Gen.html))
        {
            m_DeviceGeneration = "iPod Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) (7th generation)";
        }  
  
        // Check if the device running this is an unknown iPhone
        if (Device.generation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) == DeviceGeneration.iPhoneUnknown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration-iPhoneUnknown.html))
        {
            m_DeviceGeneration = "Unknown iPhone";
        }
        
        // Check if the device running this is an unknown iPad
        if (Device.generation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) == DeviceGeneration.iPadUnknown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration-iPadUnknown.html))
        {
            m_DeviceGeneration = "Unknown iPad";
        }
        
        // Check if the device running this is an unknown iPod Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html)
        if (Device.generation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) == DeviceGeneration.iPodTouchUnknown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration-iPodTouchUnknown.html))
        {
            m_DeviceGeneration = "Unknown iPod Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html)";
        }
        
        // Output the device generation to the console/device log
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Device[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html) generation: " + m_DeviceGeneration);
    }
}

```

* * *
