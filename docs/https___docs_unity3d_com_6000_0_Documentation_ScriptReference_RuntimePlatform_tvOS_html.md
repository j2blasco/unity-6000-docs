* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.tvOS.html

#  [RuntimePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.html).tvOS
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
In the player on the Apple's tvOS.
Additional resources: [RuntimePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.html), [Platform dependent Compilation.](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Application.platform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html) == RuntimePlatform.tvOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.tvOS.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Do something special here!");
        }
    }
}

```

* * *
