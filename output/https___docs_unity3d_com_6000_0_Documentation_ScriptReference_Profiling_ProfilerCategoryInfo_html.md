* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo.html

# ProfilerCategoryInfo
struct in UnityEditor.Profiling
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
Category information descriptor structure.
Contains the full information about a Profiler category such as its name, color, id, and flags. Use with [FrameDataView.GetAllCategories](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetAllCategories.html) and [FrameDataView.GetCategoryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCategoryInfo.html) to get information on the available Profiler categories.
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
### Properties
Property | Description  
---|---  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo-color.html) | The color of the Profiler category, as a Color32.  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo-flags.html) | Flags for showing if the Category is user defined or built into Unity.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo-id.html) | Id used by Unity for tracking the Category.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo-name.html) | The name used by Unity for the Category.  
* * *
