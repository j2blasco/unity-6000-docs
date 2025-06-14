* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.html

# MarkerFlags
enumeration
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
Profiler marker usage flags.
Use to specify marker usage or availability information.
```
using System.Collections.Generic;
using Unity.Profiling.LowLevel;
using Unity.Profiling.LowLevel.Unsafe;  
  
public class Example
{
    public static unsafe void WriteAllNonDevelopmentStatsToFile(string filePath)
    {
        using (var writer = new System.IO.StreamWriter(filePath))
        {
            var availableStatHandles = new List<ProfilerRecorderHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html)>();
            ProfilerRecorderHandle.GetAvailable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html)(availableStatHandles);
            foreach (var h in availableStatHandles)
            {
                var statDesc = ProfilerRecorderHandle.GetDescription[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetDescription.html)(h);
                if (!statDesc.Flags.HasFlag(MarkerFlags.AvailabilityNonDevelopment[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.AvailabilityNonDevelopment.html)))
                    continue;  
  
                var name = System.Text.Encoding.UTF8.GetString(statDesc.NameUtf8, statDesc.NameUtf8Len);
                writer.WriteLine($"{name};{statDesc.Flags}");
            }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.Default.html) | Default value for markers created in native code.  
[Script](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.Script.html) | Marker is created by scripting code.  
[ScriptInvoke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.ScriptInvoke.html) | Specifies that marker is generated by invocation of scripting method from native code.  
[ScriptDeepProfiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.ScriptDeepProfiler.html) | Specifies that marker is generated by deep profiling.  
[AvailabilityEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.AvailabilityEditor.html) | Specifies that marker is present only in the Editor.  
[AvailabilityNonDevelopment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.AvailabilityNonDevelopment.html) | Specifies that marker is present in non-development Players.  
[Warning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.Warning.html) | Specifies that marker highlights performance suboptimal behavior.  
[Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.Counter.html) | Marker represents a counter.  
[SampleGPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.SampleGPU.html) | Specifies that marker is capable of capturing GPU timings.  
* * *
