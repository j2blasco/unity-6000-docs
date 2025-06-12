* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetAreaEnabled.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).GetAreaEnabled
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
public static bool GetAreaEnabled([Profiling.ProfilerArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerArea.html) area); 
### Parameters
Parameter | Description  
---|---  
area | Which area you want to check the state of.  
### Returns
**bool** Returns whether or not a given [ProfilerArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerArea.html) is currently enabled. 
### Description
Returns whether or not a given [ProfilerArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerArea.html) is currently enabled.
Enabled areas emit stats and samples. Each enabled area adds to the profiler overhead. To disable an area, either close the corresponding chart in the [ProfilerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html) or call [Profiler.SetAreaEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.SetAreaEnabled.html).
* * *
