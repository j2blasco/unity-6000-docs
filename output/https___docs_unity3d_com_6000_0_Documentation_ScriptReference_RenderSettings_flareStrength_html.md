* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-flareStrength.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).flareStrength
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
flareStrength; 
### Description
The intensity of all flares in the Scene.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void  Start()
    {
        RenderSettings.flareStrength[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-flareStrength.html) = 0.2f;
    }
}

```

Additional resources: [LensFlare component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html).
* * *
