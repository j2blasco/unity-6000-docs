* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.SolidColor.html

#  [ReflectionProbeClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.html).SolidColor
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
Clear with a background color.
Additional resources: [ReflectionProbe.clearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-clearFlags.html) property.
```
using UnityEngine;
using System.Collections;  
  

public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) probe = GetComponent<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)>();  
  
        // Clear with background color (ignore any skyboxes)
        probe.clearFlags = UnityEngine.Rendering.ReflectionProbeClearFlags.SolidColor;
    }
}

```

* * *
