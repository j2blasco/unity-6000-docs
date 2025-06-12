* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.CreatePropertyGUI.html

#  [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html).CreatePropertyGUI
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
public [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePropertyGUI([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
property | The SerializedProperty to make the custom GUI for.  
### Returns
**VisualElement** The element containing the custom GUI. 
### Description
Creates custom GUI with UI Toolkit for the property.
See [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) for an example of making a custom property drawer that uses CreatePropertyGUI.
* * *
