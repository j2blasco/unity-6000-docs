* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.OnToolbarGUI.html

#  [SearchField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.html).OnToolbarGUI
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
public string OnToolbarGUI(string text, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
text | Text string to display in the search field.  
options | An optional list of layout options that specify extra layout properties.   
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**string** The text entered in the search field. The original input string is returned instead if the search field text was not changed. 
### Description
This function displays the search field with the toolbar UI style and uses the GUILayout class to automatically calculate the position and size of the Rect it is rendered to. Pass an optional list to specify extra layout properties.
* * *
## Declaration
public string OnToolbarGUI([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, string text); 
### Parameters
Parameter | Description  
---|---  
rect | Rectangle to use for the search field.  
text | Text string to display in the search field.  
### Returns
**string** The text entered in the search field. The original input string is returned instead if the search field text was not changed. 
### Description
This function displays the search field with a toolbar style in the given Rect.
* * *
