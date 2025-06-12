* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool-toolbarIcon.html

#  [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html).toolbarIcon
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
[GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) toolbarIcon; 
### Description
The icon and tooltip for this custom editor tool. If this function is not implemented, the toolbar displays the Inspector icon for the target type. If no target type is defined, the toolbar displays the Tool Mode icon.
This property is accessed frequently, so load the icon's [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) in [MonoBehaviour.OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnEnable.html).
```
using UnityEditor.EditorTools;
using UnityEngine;

public class ToolbarIconSample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {}

[EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Toolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toolbar.html) Icon Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)", typeof(ToolbarIconSample))]
class ToolbarIconSampleTool : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)
{
    GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) m_Icon;

    public override GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) toolbarIcon => m_Icon;

    private void OnEnable()
    {
        m_Icon = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Text Icon", "Toolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toolbar.html) Icon Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) tooltip.");
    }

    private void OnDisable()
    {
        m_Icon = null;
    }
}

```

* * *
