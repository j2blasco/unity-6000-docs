* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.IgnoredByDeepProfilerAttribute.html

# IgnoredByDeepProfilerAttribute
class in Unity.Profiling
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
IgnoredByDeepProfilerAttribute prevents Unity Profiler from capturing method calls.
When you capture data with Unity Profiler in Deep Profiler mode, Unity registers entrance and exit to each function. In some cases, you want some code to be ignored. This can happen for instance if it is some kind of wrapper or method or class that adds too much clatter to the Profiler Time Line view. You can apply the [IgnoredByDeepProfiler] attribute to classes, structures, and methods. [IgnoredByDeepProfiler] works for both the Mono and IL2CPP scripting backends. 
```
using UnityEngine;
using Unity.Profiling;  
  
[IgnoredByDeepProfiler]
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
    }
}

```

* * *
