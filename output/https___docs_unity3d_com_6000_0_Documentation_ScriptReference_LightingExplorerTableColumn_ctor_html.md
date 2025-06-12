* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn-ctor.html

# LightingExplorerTableColumn Constructor
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
public LightingExplorerTableColumn([LightingExplorerTableColumn.DataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.DataType.html) type, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) headerContent, string propertyName, int width, [LightingExplorerTableColumn.OnGUIDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.OnGUIDelegate.html) onGUIDelegate, [LightingExplorerTableColumn.ComparePropertiesDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.ComparePropertiesDelegate.html) compareDelegate, [LightingExplorerTableColumn.CopyPropertiesDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.CopyPropertiesDelegate.html) copyDelegate, int[] dependencyIndices); 
### Parameters
Parameter | Description  
---|---  
type | Depending on what LightingExplorer.DataType we use, built-in compare and draw methods will be used. If you want to fully overload this, use LightingExplorer.DataType.Custom.  
headerContent | Title for the column header.  
propertyName | Name of the property on the object you wish to use. If you use LightingExplorer.DataType.Name, choose ‘null’.  
width | Width of the column. The minimum width is this value divided by 2. The default value is 100.  
onGUIDelegate | If you want to draw a property differently than the default, provide this delegate. If you use LightingExprlorer.DataType.Custom, you must override this.  
compareDelegate | If you want to sort properties differently than the default way, provide this delegate. If you use LightingExplorer.DataType.Custom, you must override this.  
copyDelegate | If you want to copy properties differently than the default way, provide this delegate.   
dependencyIndices | If you depend on another Serialized property than the one in your column, use this field to specify which indices to include. The first column is index 0.  
### Description
Constructor.
* * *
