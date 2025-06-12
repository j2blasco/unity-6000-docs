* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetGfxResourceInfo.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetGfxResourceInfo
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
public bool GetGfxResourceInfo(ulong gfxResourceId, out [Profiling.FrameDataView.GfxResourceInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GfxResourceInfo.html) info); 
### Parameters
Parameter | Description  
---|---  
gfxResourceId | Graphics resource identifier.  
info | Graphics resource information output struct with instance ID and other attributes.  
### Returns
**bool** Returns true if resource exists in the frame and the information is available. 
### Description
Gets information for a given graphics resource identifier.
Use this function to retrieve information about related Unity Objects for the graphics resource in the Profiler capture. On the Render Thread, the Profiler capture can be associated with a graphics resource representing a Texture, RenderTexture, Mesh Asset, or other graphics resource. This information is included as part of the sample metadata; you can use the [RawFrameDataView.GetSampleMetadataAsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleMetadataAsInt.html) or [HierarchyFrameDataView.GetItemInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemInstanceID.html) functions to retrieve this metadata.
```
using UnityEditorInternal;
using UnityEditor.Profiling;  
  
public class Example
{
    public static string GetGfxResourceName(int frame, ulong gfxResourceId)
    {
        using (var frameData = ProfilerDriver.GetRawFrameDataView(frame, 0))
        {
            if (frameData.GetGfxResourceInfo(gfxResourceId, out var info))
            {
                if (frameData.GetUnityObjectInfo(info.relatedInstanceId, out var objectInfo))
                    return objectInfo.name;
            }
            return "N/A";
        }
    }
}

```

* * *
