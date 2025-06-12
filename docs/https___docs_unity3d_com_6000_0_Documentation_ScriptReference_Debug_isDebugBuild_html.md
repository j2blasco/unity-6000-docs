* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-isDebugBuild.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).isDebugBuild
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
isDebugBuild; 
### Description
In the Build Settings dialog there is a check box called "Development Build".
If it is checked isDebugBuild will be true. In the editor `isDebugBuild` always returns true. It is recommended to remove all calls to [Debug.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) when deploying a game, this way you can easily deploy beta builds with debug prints and final builds without.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Log some debug information only if this is a debug build
        if (Debug.isDebugBuild[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-isDebugBuild.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This is a debug build!");
        }
    }
}

```

* * *
