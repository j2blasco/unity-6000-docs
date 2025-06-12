* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogDensity.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).fogDensity
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
fogDensity; 
### Description
The density of the exponential fog.
Fog density is used by [Exponential](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FogMode.Exponential.html) and [ExponentialSquared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FogMode.ExponentialSquared.html) modes.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        // Set the fog density
        RenderSettings.fogDensity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogDensity.html) = 0.1f;  
  
        // And enable fog
        RenderSettings.fog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fog.html) = true;
    }
}

```

Additional resources: [RenderSettings.fogMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogMode.html).
* * *
