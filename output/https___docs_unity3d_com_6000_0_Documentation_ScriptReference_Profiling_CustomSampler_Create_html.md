* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Create.html

#  [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html).Create
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
public static [Profiling.CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) Create(string name, bool collectGpuData); 
### Parameters
Parameter | Description  
---|---  
name | Name of the Sampler.  
collectGpuData | Specifies whether this Sampler records GPU timings. If you want the Sampler to record GPU timings, set this to true.  
### Returns
**CustomSampler** [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) object or _null_ if a built-in Sampler with the same name exists. 
### Description
Creates a new CustomSampler for profiling parts of your code.
Multiple calls with the same _name_ parameter return different [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) objects which refer to the same native representation. CustomSampler represents scripting profiler label.  
  
Method throws **ArgumentNullException** when used with _null_ string.
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
Additional resources: [CustomSampler.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Begin.html), [Sampler.Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html).
* * *
