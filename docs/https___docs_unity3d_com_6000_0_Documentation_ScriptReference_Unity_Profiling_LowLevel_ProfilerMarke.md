* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.String16.html

#  [ProfilerMarkerDataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.html).String16
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
Indicates that [ProfilerMarkerData.Ptr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.Ptr.html) points to a **char***.
Use [String16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.String16.html) to pass string data to the [ProfilerUnsafeUtility.BeginSampleWithMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html).  
  
**Note:** The size of the string must be set in bytes including the null terminator.
```
using System.Diagnostics;
using System.Runtime.CompilerServices;
using Unity.Profiling;
using Unity.Profiling.LowLevel;
using Unity.Profiling.LowLevel.Unsafe;  
  
public static class ProfilerMarkerExtension
{
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, string metadata)
    {
        var data = new ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)();
        data.Type = (byte)ProfilerMarkerDataType.String16[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.String16.html);
        fixed(char* c = metadata)
        {
            data.Size = ((uint)metadata.Length + 1) * 2;
            data.Ptr = c;
            ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, &data);
        }
    }
}

```

* * *
