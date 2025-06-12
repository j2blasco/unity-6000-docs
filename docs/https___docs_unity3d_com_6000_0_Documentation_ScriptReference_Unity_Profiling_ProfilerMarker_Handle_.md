* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Handle.html

#  [ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html).Handle
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
Handle; 
### Description
Gets native handle of the [ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.ProfilerMarker.html).
Use _Handle_ to obtain a native marker handle and extend funtionality of [ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.ProfilerMarker.html).
```
using System.Diagnostics;
using System.Runtime.CompilerServices;
using Unity.Collections.LowLevel.Unsafe;
using Unity.Profiling;
using Unity.Profiling.LowLevel;
using Unity.Profiling.LowLevel.Unsafe;  
  
public static class ProfilerMarkerExtension
{
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, int metadata)
    {
        var data = new ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)();
        data.Type = (byte)ProfilerMarkerDataType.Int32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.Int32.html);
        data.Size = (uint)UnsafeUtility.SizeOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<int>();
        data.Ptr = UnsafeUtility.AddressOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
        ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, &data);
    }  
  
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, uint metadata)
    {
        var data = new ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)();
        data.Type = (byte)ProfilerMarkerDataType.UInt32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.UInt32.html);
        data.Size = (uint)UnsafeUtility.SizeOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<uint>();
        data.Ptr = UnsafeUtility.AddressOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
        ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, &data);
    }  
  
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, long metadata)
    {
        var data = stackalloc ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
        data[0].Type = (byte)ProfilerMarkerDataType.Int64[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.Int64.html);
        data[0].Size = (uint)UnsafeUtility.SizeOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<long>();
        data[0].Ptr = UnsafeUtility.AddressOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
        ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
    }  
  
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, ulong metadata)
    {
        var data = stackalloc ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
        data[0].Type = (byte)ProfilerMarkerDataType.UInt64[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.UInt64.html);
        data[0].Size = (uint)UnsafeUtility.SizeOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<ulong>();
        data[0].Ptr = UnsafeUtility.AddressOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
        ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
    }  
  
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, float metadata)
    {
        var data = stackalloc ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
        data[0].Type = (byte)ProfilerMarkerDataType.Float[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.Float.html);
        data[0].Size = (uint)UnsafeUtility.SizeOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<float>();
        data[0].Ptr = UnsafeUtility.AddressOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
        ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
    }  
  
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, double metadata)
    {
        var data = stackalloc ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
        data[0].Type = (byte)ProfilerMarkerDataType.Double[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.Double.html);
        data[0].Size = (uint)UnsafeUtility.SizeOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<double>();
        data[0].Ptr = UnsafeUtility.AddressOf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
        ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
    }  
  
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    [Conditional("ENABLE_PROFILER")]
    public static unsafe void Begin(this ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) marker, string metadata)
    {
        var data = stackalloc ProfilerMarkerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
        data[0].Type = (byte)ProfilerMarkerDataType.String16[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.String16.html);
        fixed(char* c = metadata)
        {
            data[0].Size = ((uint)metadata.Length + 1) * 2;
            data[0].Ptr = c;
            ProfilerUnsafeUtility.BeginSampleWithMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
        }
    }
}

```

Additional resources: [ProfilerUnsafeUtility.CreateMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html), [ProfilerUnsafeUtility.BeginSampleWithMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html).
* * *
