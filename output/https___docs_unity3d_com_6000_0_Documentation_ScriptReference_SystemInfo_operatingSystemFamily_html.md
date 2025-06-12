* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystemFamily.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).operatingSystemFamily
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
[OperatingSystemFamily](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OperatingSystemFamily.html) operatingSystemFamily; 
### Description
Returns the operating system family the game is running on (Read Only).
This API is used by UI code to distinguish between desktop OS families with different UI conventions. For all non-desktop platforms it will currently return [OperatingSystemFamily.Other](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OperatingSystemFamily.Other.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (SystemInfo.operatingSystemFamily[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystemFamily.html) == OperatingSystemFamily.MacOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OperatingSystemFamily.MacOSX.html))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Do something special here");
    }
}

```

Additional resources: [OperatingSystemFamily](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OperatingSystemFamily.html) enum, [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html) class.
* * *
