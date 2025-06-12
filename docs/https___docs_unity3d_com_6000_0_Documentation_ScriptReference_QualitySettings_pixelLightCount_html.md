* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-pixelLightCount.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).pixelLightCount
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
pixelLightCount; 
### Description
The maximum number of pixel lights that should affect any object.
If there are more lights illuminating an object, the dimmest ones will be rendered as vertex lights.  
  
Use this from scripting if you want to have finer control than offered by quality settings levels.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Use at most one pixel light for every object
        QualitySettings.pixelLightCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-pixelLightCount.html) = 1;
    }
}

```

Additional resources: [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
* * *
