* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-currentResolution.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).currentResolution
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
[Resolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html) currentResolution; 
### Description
The current screen resolution (Read Only).
Returns the current screen resolution (read only). If the player is running in windowed mode, this returns the current resolution of the desktop. If you are working with VR devices, use [XRSettings.eyeTextureWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-eyeTextureWidth.html) and [XRSettings.eyeTextureHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-eyeTextureHeight.html) instead.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        print(Screen.currentResolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-currentResolution.html));
    }
}

```

* * *
