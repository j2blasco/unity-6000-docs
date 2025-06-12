* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetAllCategories.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetAllCategories
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
public void GetAllCategories(List<ProfilerCategoryInfo> categoryInfoList); 
### Parameters
Parameter | Description  
---|---  
categoryInfoList | List filled with ProfilerCategoryInfo.  
### Description
Gets all the available Profiler Categories for the current profiling session.
Use to retrieve all the Profiler category information for the current Profiling session.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor.Profiling;
using Unity.Profiling;  
  
public class Example
{
    public static void GetAllBuiltinProfilerCategories(FrameDataView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html) frameDataView, List<ProfilerCategoryInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo.html)> unityProfilerCategories)
    {
        unityProfilerCategories.Clear();
        var infos = new List<ProfilerCategoryInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo.html)>();
        frameDataView.GetAllCategories(infos);
        foreach (var info in infos)
        {
            if (info.flags.HasFlag(ProfilerCategoryFlags.Builtin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategoryFlags.Builtin.html)))
            {
                unityProfilerCategories.Add(info);
            }
        }
    }
}

```

* * *
