* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.OnGUI.html

#  [MaterialPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.html).OnGUI
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
public void OnGUI([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) prop, string label, [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html) editor); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the property GUI.  
prop | The [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) to make the custom GUI for.  
label | The label of this property.  
editor | Current material editor.  
### Description
Override this method to make your own GUI for the property.
* * *
