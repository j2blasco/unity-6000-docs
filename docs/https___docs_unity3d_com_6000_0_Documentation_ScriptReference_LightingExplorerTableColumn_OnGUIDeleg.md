* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.OnGUIDelegate.html

#  [LightingExplorerTableColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.html).OnGUIDelegate
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
public delegate void OnGUIDelegate([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) prop, SerializedProperty[] dependencies); 
### Parameters
Parameter | Description  
---|---  
r | The current rect for where it will be drawn in the TableView.  
prop | The property that is specified using ‘propertyName’ in the constructor.  
dependencies | An array of properties specified by using ‘dependencyIndicies’ in the constructor.  
### Description
A delegate for how to draw the property.
* * *
