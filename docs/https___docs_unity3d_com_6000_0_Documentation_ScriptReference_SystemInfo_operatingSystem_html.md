* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystem.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).operatingSystem
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
operatingSystem; 
### Description
Operating system name with version (Read Only).
Returns detailed information about the operating system of the device, including the version. For a simple platform detection, properties like [Application.platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html) or [deviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html) might be more appropriate.  
  
**Note:** On Microsoft Store Apps, it's not easy to identify if you're running 32-bit or 64-bit version of Windows. However, you can query the CPU architecture to find this information. If the CPU is 64-bit, [SystemInfo.operatingSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystem.html) returns **Windows <version> 64 bit**, and if the CPU is 32-bit - **Windows <version>**.
```
using UnityEngine;  
  
public class ExampleClass: MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints "Windows 11 (10.0.22621) 64bit" on 64 bit Windows 11
        // Prints "Mac OS X 13.4" on Mac OS Ventura
        // Prints "iPhone OS" with iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) 15.3.1
        // Prints "iPad OS" on iPad with iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) 16
        // Prints "Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Android.html) OS 13 / API-33 (TQ2A.230305.008.C1/9619669)"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(SystemInfo.operatingSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystem.html));
    }
}

```

Additional resources: [Application.platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html), [deviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html).
* * *
