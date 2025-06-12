* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendor.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).graphicsDeviceVendor
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
graphicsDeviceVendor; 
### Description
The vendor of the graphics device (Read Only).
This is the vendor of user's graphics card, as reported by the graphics driver.  
  
Additional resources: [SystemInfo.graphicsDeviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceName.html), [SystemInfo.graphicsDeviceVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVersion.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints using the following format - "ATI Technologies Inc." on MacBook Pro running Mac OS X 10.4.8
        print(SystemInfo.graphicsDeviceVendor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendor.html));
    }
}

```

* * *
