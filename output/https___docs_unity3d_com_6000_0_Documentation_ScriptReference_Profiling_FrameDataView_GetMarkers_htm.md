* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkers.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetMarkers
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
public void GetMarkers(List<MarkerInfo> markerInfoList); 
### Parameters
Parameter | Description  
---|---  
markerInfoList | List filled with marker descriptors.  
### Description
Gets all available markers for the current profiling session.
Use to retrieve all marker identifiers together with names and other information such as category, flags and metadata parameters.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor.Profiling;
using Unity.Profiling.LowLevel;  
  
public class Example
{
    public static void GetAllWarningMarkers(FrameDataView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html) frameData, List<int> warningMarkerIds)
    {
        warningMarkerIds.Clear();
        var markers = new List<FrameDataView.MarkerInfo>();
        frameData.GetMarkers(markers);
        foreach (var marker in markers)
        {
            if (marker.flags.HasFlag(MarkerFlags.Warning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.Warning.html)))
                warningMarkerIds.Add(marker.id);
        }
    }
}

```

Additional resources: [MarkerInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.MarkerInfo.html).
* * *
