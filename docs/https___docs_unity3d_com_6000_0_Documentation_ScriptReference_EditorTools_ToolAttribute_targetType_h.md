* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-targetType.html

#  [ToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute.html).targetType
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
targetType; 
### Description
Set to the type that this [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) or [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) can edit. Set to null if the tool is not specific to a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) and should be available at any time.
A Global tool or tool context is always available in the toolbar menu. A [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tool is only available when the current selection contains a matching target type.
* * *
