* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemorySnapshotMetadata.Description.html

#  [MemorySnapshotMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemorySnapshotMetadata.html).Description
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
Description; 
### Description
User defined metadata that provides a description for the memory snapshot.
This propery provides a free form text input method to extend the memory snapshot with extra information such as the context in which the snapshot was taken.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using Unity.Profiling.Memory;  
  
public class MemoryProfilerExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string levelName = "Default Level Name";  
  
    void Start()
    {
        MemoryProfiler.CreatingMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) += CreateMetadata;
    }  
  
    void CreateMetadata(MemorySnapshotMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemorySnapshotMetadata.html) metadata)
    {
        metadata.Description = $"This Memory Snapshot capture started at {DateTime.Now} in level {levelName}.";
    }  
  
    void OnDestroy()
    {
        MemoryProfiler.CreatingMetadata[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) -= CreateMetadata;
    }
}

```

* * *
