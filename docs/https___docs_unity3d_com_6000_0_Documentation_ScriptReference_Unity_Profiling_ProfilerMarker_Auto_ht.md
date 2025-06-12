* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Auto.html

#  [ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html).Auto
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
public [Unity.Profiling.ProfilerMarker.AutoScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.AutoScope.html) Auto(); 
### Returns
**AutoScope** IDisposable struct which calls [Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Begin.html) and [End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.End.html) automatically. 
### Description
Creates a helper struct for the scoped **using** blocks.
[Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Begin.html) is called in the constructor and [End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.End.html) in the _Dispose_ method.  
  
**Note:** [Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Auto.html) is thread safe and can be used in jobified code.
```
using Unity.Profiling;  
  
public class MySystemClass
{
    static ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) s_SimulatePerfMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)("MySystem.Simulate");  
  
    public void UpdateLogic()
    {
        using (s_SimulatePerfMarker.Auto())
        {
            // ...
        }
    }
}

```

* * *
