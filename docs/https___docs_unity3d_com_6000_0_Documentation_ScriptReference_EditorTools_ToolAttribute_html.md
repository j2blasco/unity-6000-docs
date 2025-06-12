* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute.html

# ToolAttribute
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
Base class from which [EditorToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html) and [EditorToolContextAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContextAttribute.html) inherit.
### Static Properties
Property | Description  
---|---  
[defaultPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-defaultPriority.html) | The default value for ToolAttribute.toolPriority and ToolAttribute.variantPriority. Specify a priority lower than this value to display a tool before the default entries, or specify a higher value to display it after the default entries.  
### Properties
Property | Description  
---|---  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-displayName.html) | The name that displays in menus.  
[targetContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-targetContext.html) | If provided, the EditorTool will only be made available when the ToolManager.activeContextType is equal to targetContext.  
[targetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-targetType.html) | Set to the type that this EditorTool or EditorToolContext can edit. Set to null if the tool is not specific to a Component and should be available at any time.  
[toolPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-toolPriority.html) | Tool priority defines the order that tools are displayed in within the Tools Overlay.  
[variantGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantGroup.html) | Tool variants are used to group logically similar tools into a single button in the Tools Overlay.  
[variantPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantPriority.html) | The variant priority defines the order that tools are displayed in when they are displayed in a ToolAttribute.variantGroup dropdown.  
* * *
