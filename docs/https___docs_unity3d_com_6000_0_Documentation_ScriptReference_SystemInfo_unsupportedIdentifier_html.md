* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-unsupportedIdentifier.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).unsupportedIdentifier
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
unsupportedIdentifier; 
### Description
Value returned by SystemInfo string properties which are not supported on the current platform.
```
using UnityEngine;
using System.Collections;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (SystemInfo.unsupportedIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-unsupportedIdentifier.html) != SystemInfo.deviceUniqueIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html))
        {
            // use SystemInfo.deviceUniqueIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html)
        }
    }
}

```

* * *
