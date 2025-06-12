* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.GetSample.html

#  [ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html).GetSample
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
public [Unity.Profiling.ProfilerRecorderSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderSample.html) GetSample(int index); 
### Description
Gets sample data.
Use to obtain sample data.
```
using Unity.Profiling;
using UnityEngine;  
  
public class FrameTimeScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) frameTimeRecorder;  
  
    void OnEnable()
    {
        frameTimeRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Internal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 30);
    }  
  
    void OnDisable()
    {
        frameTimeRecorder.Dispose();
    }  
  
    double CalculateAverageFromSampleValuesPerFrame(ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) r)
    {
        int count = r.Count;
        double acc = 0;
        for (var i = 0; i < count; ++i)
        {
            acc += r.GetSample(i).Value;
        }
        return count > 0 ? acc / count : 0;
    }  
  
    void OnGUI()
    {
        GUI.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 350, 20), $"Frame time: {CalculateAverageFromSampleValuesPerFrame(frameTimeRecorder) * 1e-6:0.00}ms");
    }
}

```

* * *
