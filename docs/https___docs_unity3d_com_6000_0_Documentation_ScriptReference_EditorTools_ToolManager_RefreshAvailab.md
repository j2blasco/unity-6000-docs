* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.RefreshAvailableTools.html

#  [ToolManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html).RefreshAvailableTools
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
public static void RefreshAvailableTools(); 
### Description
Call RefreshAvailableTools to rebuild the contents of the Scene View Tools Overlay.
This method is useful when a tool can change the value of [EditorTool.IsAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.IsAvailable.html) outside of selection and tool change events.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEngine;  
  
// An example of a tool that may be made available or unavailable in situations other than selection changes.
[EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Conditional Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)", typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)))]
class ConditionallyAvailable : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)
{
    bool m_IsAvailable;
    void OnEnable() => EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) += UpdateAvailable;
    void OnDisable() => EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) -= UpdateAvailable;  
  
    // This tool is enabled and disabled in 10 second intervals.
    void UpdateAvailable()
    {
        var time = DateTime.Now;  
  
        if (m_IsAvailable != ((time.Second / 10) % 2 == 0))
        {
            m_IsAvailable = !m_IsAvailable;
            // Because the tool is changing availability arbitrarily, it is necessary to manually refresh the UI.
            ToolManager.RefreshAvailableTools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.RefreshAvailableTools.html)();
        }
    }  
  
    // When a tool is available, it is shown in the Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html) Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html). If not available, it is hidden.
    public override bool IsAvailable() => m_IsAvailable;
}

```

* * *
