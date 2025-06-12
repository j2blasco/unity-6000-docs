* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveTool.html

#  [ToolManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html).SetActiveTool
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
public static void SetActiveTool(); 
## Declaration
public static void SetActiveTool(Type type); 
## Declaration
public static void SetActiveTool([EditorTools.EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) tool); 
### Parameters
Parameter | Description  
---|---  
type | The [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) type to set as the active tool.  
tool | The [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) instance to set as the active tool.  
### Description
Sets the active [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html).
To set a built-in tool, such as Move, Rotate, or Scale, to active, use [Tools.current](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools-current.html) instead.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEngine;

class ToolToSetActive : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)/Set Active Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) Type")]
    static void SetActiveToolExample()
    {
        ToolManager.SetActiveTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveTool.html)<ToolToSetActive>();
    }

    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Position;

    public override void OnToolGUI(EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window)
    {
        m_Position = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(m_Position, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(m_Position);
    }
}

```

* * *
