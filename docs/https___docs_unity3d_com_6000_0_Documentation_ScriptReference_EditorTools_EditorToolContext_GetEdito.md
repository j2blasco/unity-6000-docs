* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.GetEditorToolType.html

#  [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html).GetEditorToolType
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
protected Type GetEditorToolType([Tool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) tool); 
### Parameters
Parameter | Description  
---|---  
tool | The [Tool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) that needs to be resolved to an [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) type.  
### Returns
**Type** An [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) type for the requested [Tool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html). 
### Description
Defines the [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) type for a given [Tool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html).
This function resolves the correct [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) type for the active context. Unity only invokes it for manipulation tools, such as [Tool.Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Move.html), [Tool.Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Rotate.html), [Tool.Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Scale.html), [Tool.Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Rect.html), and [Tool.Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Transform.html).
* * *
