* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-flareFadeSpeed.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).flareFadeSpeed
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
flareFadeSpeed; 
### Description
The fade speed of all flares in the Scene.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void  Start()
    {
        RenderSettings.flareFadeSpeed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-flareFadeSpeed.html) = 0.5f;
    }
}

```

Additional resources: [The Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html), [LensFlare component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html).
* * *
