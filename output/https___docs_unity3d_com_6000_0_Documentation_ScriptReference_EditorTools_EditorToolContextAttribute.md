* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContextAttribute-ctor.html

# EditorToolContextAttribute Constructor
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
public EditorToolContextAttribute(string displayName, Type targetType); 
### Parameters
Parameter | Description  
---|---  
displayName | The name to display in menus.  
targetType | Set to the type that this tool can edit. Set to null if the tool is not a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tool.  
### Description
Registers an [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) as either a global tool context or a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tool context.
* * *
