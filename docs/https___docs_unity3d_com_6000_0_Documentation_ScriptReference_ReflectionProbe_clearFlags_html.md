* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-clearFlags.html

#  [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).clearFlags
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html "Go to ReflectionProbe Component in the Manual")
[Rendering.ReflectionProbeClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.html) clearFlags; 
### Description
How the reflection probe clears the background.
Can be [ReflectionProbeClearFlags.Skybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.Skybox.html) or [ReflectionProbeClearFlags.SolidColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.SolidColor.html).
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
Additional resources: [ReflectionProbeClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.html).
* * *
