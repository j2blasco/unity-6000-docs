* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html

#  [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html).Get
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
public static [Profiling.Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html) Get(string name); 
### Parameters
Parameter | Description  
---|---  
name | Profiler Sampler name.  
### Returns
**Sampler** [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html) object which represents specific profiler label. 
### Description
Returns [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html) object for the specific CPU Profiler label.
You can use this function to get a Sampler associated with a built-in or custom label. The _name_ parameter is the same you can see in Hierarchy view of the [Profiler Window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html). If label with the specified _name_ parameter does not exist or not available in the Player, an invalid Sampler object will be returned. You can use [Sampler.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-isValid.html) to verify if Sampler is valid.
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Sampler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html) sampler;
    void Start()
    {
        sampler = Sampler.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html)("BehaviourUpdate");
    }
}

```

**Get** can be used to obtain any existing Sampler including custom Sampler. Return value is always Sampler type and can not be casted to CustomSampler.  
  
**Note:** At the moment all built-in counters are available only in the Editor and Development Players. **Get** in non-Development Players returns invalid Sampler.  
  
Additional resources: [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html), [Sampler.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-isValid.html), [CPU Usage Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html).
* * *
