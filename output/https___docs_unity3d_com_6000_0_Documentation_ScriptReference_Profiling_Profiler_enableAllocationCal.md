* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableAllocationCallstacks.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).enableAllocationCallstacks
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
enableAllocationCallstacks; 
### Description
Enables the recording of callstacks for managed allocations.
When enabled, the Unity player saves callstack for each managed allocation sample which is known as _GC.Alloc_. You can see the callstacks in the Timeline View or in the Object Details pane of the Hierarchy View when selecting the _GC.Alloc_ sample.  
  
You must also set [Profiler.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) to `true` in order to start the capture.
```
using UnityEngine;
using System.Collections;
using UnityEngine.Profiling;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Profiler.logFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-logFile.html) = "mylog"; //Also supports passing "myLog.raw"
        Profiler.enableBinaryLog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableBinaryLog.html) = true;
        Profiler.enableAllocationCallstacks[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableAllocationCallstacks.html) = true;
        Profiler.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) = true;  
  
        // Optional, if more memory is needed for the buffer
        Profiler.maxUsedMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-maxUsedMemory.html) = 256 * 1024 * 1024;
    }
}

```

**Note:** Callstacks capture adds noticable performance overhead to the profiling for every managed allocation.
* * *
