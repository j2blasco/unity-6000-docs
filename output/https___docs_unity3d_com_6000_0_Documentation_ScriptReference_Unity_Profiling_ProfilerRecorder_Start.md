* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html

#  [ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html).StartNew
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
public static [Unity.Profiling.ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) StartNew([Unity.Profiling.ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) category, string statName, int capacity, [Unity.Profiling.ProfilerRecorderOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
category | Profiler category.  
statName | Profiler marker or counter name.  
capacity | Maximum amount of samples to be collect. Must be greater than 0.  
options | ProfilerRecorder options.  
### Returns
**ProfilerRecorder** Returns new enabled recorder instance. 
### Description
Initialize a new instance of ProfilerRecorder and start data collection.
For a list of built-in Profiler markers available, see the User Manual documentation on [Common Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html).  
  
**Note:** _capacity_ paramether must be greater than 0, otherwise StartNew throws an exception.
```
using Unity.Profiling;
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) systemMemoryRecorder;
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) gcMemoryRecorder;
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) mainThreadTimeRecorder;  
  
    void OnEnable()
    {
        systemMemoryRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Memory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html), "System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) Used Memory");
        gcMemoryRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Memory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html), "GC Reserved Memory");
        mainThreadTimeRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Internal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 15);
    }  
  
    void OnDisable()
    {
        systemMemoryRecorder.Dispose();
        gcMemoryRecorder.Dispose();
        mainThreadTimeRecorder.Dispose();
    }
}

```

Additional resources: [ctor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder-ctor.html).
* * *
## Declaration
public static [Unity.Profiling.ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) StartNew([Unity.Profiling.ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, int capacity, [Unity.Profiling.ProfilerRecorderOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
capacity | Maximum amount of samples to be collected. Must be greater than 0.  
options | Profiler recorder options.  
marker | Profiler marker instance.  
### Returns
**ProfilerRecorder** Returns new enabled recorder instance. 
### Description
Initialize a new instance of ProfilerRecorder for ProfilerMarker and start data collection.
Additional resources:: [ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html).
* * *
