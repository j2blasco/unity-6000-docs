* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html

# Sampler
class in UnityEngine.Profiling
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
Provides control over a CPU Profiler label.
Sampler is a counter which produces timings information you can see in [CPU Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html). Use this class to get information about built-in or custom Profiler label.  
  
Additional resources: [Sampler.Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html), [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html), [CPU Usage Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html).
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
