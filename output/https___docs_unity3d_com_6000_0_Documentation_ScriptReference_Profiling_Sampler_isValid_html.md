* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-isValid.html

#  [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html).isValid
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
isValid; 
### Description
Returns true if Sampler is valid. (Read Only)
Invalid Sampler represents non-existing Profiler label.  
  
**Note:** At the moment all built-in counters are available only in the Editor and Development Players. [Sampler.Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html) in non-Development Players returns invalid Sampler.
```
using UnityEngine;
using UnityEngine.Profiling;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var sampler = Sampler.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html)("BehaviourUpdate");
        if (sampler.isValid)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Retrieved a Sampler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html) for BehaviourUpdate!");  
  
        sampler = Sampler.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html)("TerrainRenderer");
        if (!sampler.isValid)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) label TerrainRenderer does not exist!");
    }
}

```

* * *
