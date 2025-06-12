* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html

# ToolManager
class in UnityEditor.EditorTools
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
This class manipulates editor tools in the Scene view.
### Static Properties
Property | Description  
---|---  
[activeContextType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-activeContextType.html) | Gets the type of EditorToolContext that is currently active. The default value is GameObjectToolContext.  
[activeToolType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-activeToolType.html) | Gets the type of the EditorTool that is currently active.  
### Static Methods
Method | Description  
---|---  
[IsActiveContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.IsActiveContext.html) | Test if an EditorToolContext is currently the active tool context.  
[IsActiveTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.IsActiveTool.html) | Test if an EditorTool is currently the active tool.  
[RefreshAvailableTools](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.RefreshAvailableTools.html) | Call RefreshAvailableTools to rebuild the contents of the Scene View Tools Overlay.  
[RestorePreviousPersistentTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.RestorePreviousPersistentTool.html) | Sets the last-used global EditorTool as the active tool.  
[RestorePreviousTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.RestorePreviousTool.html) | Sets the last-used EditorTool as the active tool.  
[SetActiveContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveContext.html) | Sets the active EditorToolContext.  
[SetActiveTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveTool.html) | Sets the active EditorTool.  
### Events
Event | Description  
---|---  
[activeContextChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-activeContextChanged.html) | Defines an event handler for when the active EditorToolContext changes.  
[activeContextChanging](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-activeContextChanging.html) | Defines an event handler for when the active EditorToolContext will change.  
[activeToolChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-activeToolChanged.html) | Defines an event handler for when the active tool changes.  
[activeToolChanging](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-activeToolChanging.html) | Defines an event handler for when the active tool changes.  
* * *
