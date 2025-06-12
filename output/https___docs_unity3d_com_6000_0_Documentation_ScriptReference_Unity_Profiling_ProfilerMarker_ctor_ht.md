* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker-ctor.html

# ProfilerMarker Constructor
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
public ProfilerMarker(string name); 
## Declaration
public ProfilerMarker([Unity.Profiling.ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) category, string name); 
## Declaration
public ProfilerMarker([Unity.Profiling.ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) category, char* name, int nameLen); 
## Declaration
public ProfilerMarker([Unity.Profiling.ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) category, string name, [Unity.Profiling.LowLevel.MarkerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.html) flags); 
## Declaration
public ProfilerMarker([Unity.Profiling.ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) category, char* name, int nameLen, [Unity.Profiling.LowLevel.MarkerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.html) flags); 
## Declaration
public ProfilerMarker(char* name, int nameLen); 
### Parameters
Parameter | Description  
---|---  
name | Marker name.  
category | Profiler category.  
nameLen | Marker name length.  
flags | The marker flags.  
### Description
Constructs a new performance marker for code instrumentation.
Use _ProfilerMarker_ to markup a piece of code for the Profiler and [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).
```
using Unity.Profiling;  
  
public class MySystemClass
{
    static readonly ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) s_PreparePerfMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)("MySystem.Prepare");
    static readonly ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) s_SimulatePerfMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)(ProfilerCategory.Ai[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Ai.html), "MySystem.Simulate");  
  
    public void UpdateLogic()
    {
        s_PreparePerfMarker.Begin();
        // ...
        s_PreparePerfMarker.End();  
  
        using (s_SimulatePerfMarker.Auto())
        {
            // ...
        }
    }
}

```

* * *
