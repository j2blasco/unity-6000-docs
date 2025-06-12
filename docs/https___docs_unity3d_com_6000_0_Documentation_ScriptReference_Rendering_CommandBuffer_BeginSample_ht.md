* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BeginSample.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).BeginSample
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
public void BeginSample(string name); 
## Declaration
public void BeginSample([Profiling.CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) sampler); 
## Declaration
public void BeginSample([Unity.Profiling.ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker); 
### Parameters
Parameter | Description  
---|---  
name | Name of the profile information used for sampling.  
sampler | The CustomSampler that the CommandBuffer uses for sampling.  
marker | The ProfilerMarker that the CommandBuffer uses for sampling.  
### Description
Adds a command to begin profile sampling.
Schedules a performance profiling sample to begin when the Command Buffer reaches this point. This is useful for measuring CPU and GPU time spent by one or more commands in the Command Buffer.  
  
A profiling sample that starts with BeginSample must always end with a call to [CommandBuffer.EndSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EndSample.html) with the same argument.
* * *
