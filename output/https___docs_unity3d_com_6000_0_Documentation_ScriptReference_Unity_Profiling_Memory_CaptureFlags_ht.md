* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.html

# CaptureFlags
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
Flags that specify what kind of data to capture in a snapshot.
These flags provide control for what broad data categories should be included in the snapshot. For general purpose captures it is recommended to capture with all flags, or at least with [CaptureFlags.ManagedObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html), [CaptureFlags.NativeObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeObjects.html) and [CaptureFlags.NativeAllocations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html).  
  
For more focused investigations where the size of the snapshot and the speed at which it is taken are important, you can use a narrower set of [CaptureFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.html). For example, if the only goal is to check native object sizes, then not setting the [CaptureFlags.ManagedObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html) flag can greately reduce capture time and size. If detailed NativeAllocations, such as those used by native collections, and the graphics sizes of native objects is not important, the [CaptureFlags.NativeAllocations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html) can be left off as well.  
  
**Note:** [CaptureFlags.NativeAllocations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html) and [CaptureFlags.NativeAllocationSites](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html) won't add extra data to the snapshot unless the build supports the collection of native call stack information, which currently requires source code access.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.IO;
using Unity.Profiling.Memory;
using UnityEngine;  
  
public static class MemoryProfilerExample
{
    public static IEnumerator TakeSnapshot()
    {
        var snapshotFileName = "SnapshotName.tmpsnap";
        // Make sure the file does not exist, e.g. as a left over of a failed previous attempt to take a snapshot.
        if (File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(snapshotFileName))
            File.Delete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Delete.html)(snapshotFileName);  
  
        bool snapshotFinished = false;
        string resultingSnapshotPath = null;
        MemoryProfiler.TakeSnapshot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html)(snapshotFileName, (filePath, success) =>
        {
            snapshotFinished = true;
            if (success)
            {
                resultingSnapshotPath = Path.GetFullPath(filePath);
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Snapshot captured and stored at {resultingSnapshotPath}.");
            }
            else
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Failed to take a snapshot.");
            }
        },
            CaptureFlags.ManagedObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html) | CaptureFlags.NativeObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeObjects.html) | CaptureFlags.NativeAllocations[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html));  
  
        while (!snapshotFinished)
        {
            yield return null;
        }  
  
        if (resultingSnapshotPath != null && File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(resultingSnapshotPath))
        {
            var finalPath = resultingSnapshotPath.Replace(".tmpsnap", ".snap");
            // Remove any pre-existing file first.
            if (File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(finalPath))
                File.Delete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Delete.html)(finalPath);  
  
            // Now that writing to the file has succesfully completed, rename the file to the .snap extension to denote that the Memory Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) can open it.
            File.Move(resultingSnapshotPath, finalPath);  
  
            // If you don't have access to the Player's file system you could also upload the file to an end-point that is accessible to you here.
        }
    }
}

```

Additional resources: [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/), [MemoryProfiler.TakeSnapshot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html).
### Properties
Property | Description  
---|---  
[ManagedObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html) | Specifies that the entire managed heap and all the data needed to parse it should be captured as part of the Memory Snapshot.   
[NativeObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeObjects.html) | Specifies that information about Native Objects should be collected.  
[NativeAllocations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html) | Specifies that the Native Memory used by any Native Allocation made by Unity should be captured.  
[NativeAllocationSites](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html) | Specifies the location that each native allocation was allocated at.  
[NativeStackTraces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeStackTraces.html) | Specifies that Call-Stack Symbols for the Native Call-stack of each Allocation should be collected.  
* * *
