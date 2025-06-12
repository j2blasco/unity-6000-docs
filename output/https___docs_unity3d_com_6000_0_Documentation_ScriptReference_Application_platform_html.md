* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).platform
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
[RuntimePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.html) platform; 
### Description
Returns the platform the game is running on (Read Only).
Use this property if you need to do some platform dependent work.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Application.platform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html) == RuntimePlatform.WindowsPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WindowsPlayer.html))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Do something special here");
    }
}

```

Additional resources: [RuntimePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.html) enum, [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html) class.
* * *
