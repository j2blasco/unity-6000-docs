* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.SelectedFrameIndexChanged.html

#  [ProfilerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html).SelectedFrameIndexChanged
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
### Parameters
Parameter | Description  
---|---  
value | The zero-based index of the frame currently selected in the Profiler Window. A long.  
### Description
Calls the methods in its invocation list when the Profiler window’s selected frame index changes.
The Profiler window’s selected frame index may change for a variety of reasons, such as a new frame being captured, the user selecting a new frame, or a new capture being loaded.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html) m_Profiler;
    long m_SelectedFrameIndex;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Analysis/Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Extension")]
    public static void ShowExampleWindow()
    {
        GetWindow<Example>();
    }  
  
    void OnEnable()
    {
        // Make sure there is an open Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Window.
        if (m_Profiler == null)
            m_Profiler = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html)>();  
  
        // Subscribe to the Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) window's SelectedFrameIndexChanged event.
        m_Profiler.SelectedFrameIndexChanged += OnProfilerSelectedFrameIndexChanged;
    }  
  
    private void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)($"The selected frame in the Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) window is {m_SelectedFrameIndex}.");
    }  
  
    private void OnDisable()
    {
        // Unsubscribe from the Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) window's SelectedFrameIndexChanged event.
        m_Profiler.SelectedFrameIndexChanged -= OnProfilerSelectedFrameIndexChanged;
    }  
  
    void OnProfilerSelectedFrameIndexChanged(long selectedFrameIndex)
    {
        // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) with the selected Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) frame.
        m_SelectedFrameIndex = selectedFrameIndex;
        Repaint();
    }
}

```

Additional resources: [ProfilerWindow.selectedFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-selectedFrameIndex.html).
* * *
