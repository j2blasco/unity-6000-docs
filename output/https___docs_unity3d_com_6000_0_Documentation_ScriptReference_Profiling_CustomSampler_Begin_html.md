* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Begin.html

#  [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html).Begin
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
## Declaration
public void Begin(); 
## Declaration
public void Begin([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject); 
### Description
Begin profiling a piece of code with a custom label defined by this instance of [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html).
This will show up in the Profiler hierarchy.
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    CustomSampler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) sampler;
    void Start()
    {
        sampler = CustomSampler.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Create.html)("MyCustomSampler");
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        sampler.Begin();
        // do something that takes a lot of time
        sampler.End();
    }
}

```

Profiler.BeginSample is conditionally compiled away using ConditionalAttribute. Thus it will have zero overhead, when it is deployed in non-Development Build.  
  
Additional resources: [CustomSampler.End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.End.html), [CustomSampler.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Create.html), [ProfilerCPU](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html).
* * *
