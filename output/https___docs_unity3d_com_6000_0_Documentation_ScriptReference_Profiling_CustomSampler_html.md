* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html

# CustomSampler
class in UnityEngine.Profiling
/
Inherits from:[Profiling.Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html)
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
Custom CPU Profiler label used for profiling arbitrary code blocks.
Use CustomSampler to measure execution time of script code blocks. Produced information is displayed in the [CPU Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) and can be captured with [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).  
Using CustomSampler is more efficient than using [Profiler.BeginSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginSample.html) to profile your code. This is because CustomSamplers that have been created in advance have very low [Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Begin.html) call overhead compared to [Profiler.BeginSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginSample.html).
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
CustomSampler.Begin is conditionally compiled away using ConditionalAttribute. Thus it will have zero overhead, when it is deployed in non-Development Build.  
  
Additional resources: [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html), [CustomSampler.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Create.html), [CustomSampler.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Begin.html).
### Public Methods
Method | Description  
---|---  
[Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Begin.html) | Begin profiling a piece of code with a custom label defined by this instance of CustomSampler.  
[End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.End.html) | End profiling a piece of code with a custom label.  
### Static Methods
Method | Description  
---|---  
[Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Create.html) | Creates a new CustomSampler for profiling parts of your code.  
### Inherited Members
### Properties
Property | Description  
---|---  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-isValid.html) | Returns true if Sampler is valid. (Read Only)  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-name.html) | Sampler name. (Read Only)  
### Public Methods
Method | Description  
---|---  
[GetRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.GetRecorder.html) | Returns Recorder associated with the Sampler.  
### Static Methods
Method | Description  
---|---  
[Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html) | Returns Sampler object for the specific CPU Profiler label.  
[GetNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.GetNames.html) | Returns number and names of all registered Profiler labels.  
* * *
