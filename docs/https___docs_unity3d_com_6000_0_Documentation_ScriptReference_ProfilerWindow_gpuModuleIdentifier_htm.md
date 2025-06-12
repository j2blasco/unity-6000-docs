* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-gpuModuleIdentifier.html

#  [ProfilerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html).gpuModuleIdentifier
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
gpuModuleIdentifier; 
### Description
The identifier of the [GPU Usage Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html).
Compare this constant to [ProfilerWindow.selectedModuleIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-selectedModuleIdentifier.html) to check if the currently selected [Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow#modules.html) is the [CPU Usage Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Profiling;
using UnityEngine;  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html) m_Profiler = null;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Analysis/Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Extension")]
    public static void ShowExampleWindow()
    {
        var window = GetWindow<Example>();
        window.m_Profiler = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html)>();
    }  
  
    void OnGUI()
    {
        // First make sure there is an open Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Window
        if (m_Profiler == null)
            m_Profiler = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html)>();
        // If the currently selected Module is not the GPU Usage module, setting the selection will not be visible to the user immediately
        if (m_Profiler.selectedModuleIdentifier == ProfilerWindow.gpuModuleIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-gpuModuleIdentifier.html))
        {
            // Get the GPU Usage Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) module's selection controller interface to interact with the selection
            var gpuSampleSelectionController = m_Profiler.GetFrameTimeViewSampleSelectionController(ProfilerWindow.gpuModuleIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-gpuModuleIdentifier.html));
            // If the current selection object is null, there is no selection to print out.
            using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(gpuSampleSelectionController.selection != null))
            {
                if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Print current Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html)"))
                {
                    // Get the currently shown selection and log out some of its details
                    var selection = gpuSampleSelectionController.selection;
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"The sample currently selected in the GPU Usage Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) module is {selection.sampleDisplayName} at a depth of {selection.markerPathDepth}.");
                }
            }
        }
    }
}

```

* * *
