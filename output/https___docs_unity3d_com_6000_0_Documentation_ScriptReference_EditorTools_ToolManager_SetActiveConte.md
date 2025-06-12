* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveContext.html

#  [ToolManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html).SetActiveContext
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
public static void SetActiveContext(Type context); 
## Declaration
public static void SetActiveContext(); 
### Parameters
Parameter | Description  
---|---  
context | The [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) type to be set as the active tool.  
### Description
Sets the active [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html).
To restore the manipulation tools to their default behavior, pass [GameObjectToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html) or null to the [context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager-context.html) argument.
* * *
