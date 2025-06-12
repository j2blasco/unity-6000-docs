* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerId.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetMarkerId
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
public int GetMarkerId(string markerName); 
### Parameters
Parameter | Description  
---|---  
markerName | Marker name.  
### Returns
**int** Returns marker identifier as integer. Returns _invalidMarkerId_ if there is no such marker in the capture. 
### Description
Get Profiler marker identifier for a specific name.
Use marker identifier to avoid string allocations when traversing Profiler data.  
  
The Profiler uses a unique identifier for each marker it creates during a profiling session. The markers can generate many samples which [HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html) and [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html) can access.  
All samples that the same marker generates have the same integer marker identifier and the same name.  
  
Marker identifiers are persistent for the entire profiling session.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Collections;
using UnityEditor.Profiling;
using UnityEditorInternal;
using UnityEngine;
using UnityEngine.Profiling;  
  
public class Example
{
    public static long GetGCAllocs(int frameIndex)
    {
        long totalGcAllocSize = 0;  
  
        int gcAllocMarkerId = FrameDataView.invalidMarkerId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidMarkerId.html);  
  
        for (int threadIndex = 0;; ++threadIndex)
        {
            using (RawFrameDataView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html) frameData = ProfilerDriver.GetRawFrameDataView(frameIndex, threadIndex))
            {
                if (!frameData.valid)
                    break;  
  
                if (gcAllocMarkerId == FrameDataView.invalidMarkerId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidMarkerId.html))
                {
                    gcAllocMarkerId = frameData.GetMarkerId("GC.Alloc");
                    if (gcAllocMarkerId == FrameDataView.invalidMarkerId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidMarkerId.html))
                        break;
                }  
  
                int sampleCount = frameData.sampleCount;
                for (int i = 0; i < sampleCount; ++i)
                {
                    if (gcAllocMarkerId != frameData.GetSampleMarkerId(i))
                        continue;  
  
                    long gcAllocSize = frameData.GetSampleMetadataAsLong(i, 0);
                    totalGcAllocSize += gcAllocSize;
                }
            }
        }  
  
        return totalGcAllocSize;
    }
}

```

Additional resources: [GetMarkerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerName.html), [HierarchyFrameDataView.GetItemMarkerID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMarkerID.html), [RawFrameDataView.GetSampleMarkerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleMarkerId.html).
* * *
