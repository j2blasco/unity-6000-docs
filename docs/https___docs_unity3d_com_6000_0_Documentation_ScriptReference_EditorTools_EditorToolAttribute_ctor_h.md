* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute-ctor.html

# EditorToolAttribute Constructor
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
public EditorToolAttribute(string displayName, Type componentToolTarget, Type editorToolContext); 
## Declaration
public EditorToolAttribute(string displayName, Type componentToolTarget); 
## Declaration
public EditorToolAttribute(string displayName, Type componentToolTarget, Type editorToolContext, Type variantGroup); 
## Declaration
public EditorToolAttribute(string displayName, Type componentToolTarget, Type editorToolContext, int toolPriority, Type variantGroup); 
## Declaration
public EditorToolAttribute(string displayName, Type componentToolTarget, Type editorToolContext, int toolPriority, Type variantGroup, int variantPriority); 
### Parameters
Parameter | Description  
---|---  
displayName | The name to display in menus.  
componentToolTarget | The type this tool can edit. Set to null if the tool is not a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tool.  
editorToolContext | The [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) type that this tool relates to. When an [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) defines an `editorToolContext` scope, the tool is not shown in menus and must be activated by the [EditorToolContext.ResolveTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.ResolveTool.html) method.  
toolPriority | The order to display tools in the Tools overlay in. Refer to [ToolAttribute.toolPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-toolPriority.html).  
variantGroup | The tool variant group to assign the tool to in the Tools overlay. Tool variants are used to group similar tools into a single button in the Tools overlay. Refer to [ToolAttribute.variantGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantGroup.html).  
variantPriority | The variant priority defines the order that tools are displayed in when they are displayed in a [ToolAttribute.variantGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantGroup.html) dropdown.  
### Description
Registers an [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) as either a Global tool or a [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) tool.
A Global tool is always available in the toolbar menu. A [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) tool is only available when the current selection contains a matching target type.
* * *
