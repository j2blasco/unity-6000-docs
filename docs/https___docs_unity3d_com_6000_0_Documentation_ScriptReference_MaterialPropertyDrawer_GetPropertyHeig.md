* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.GetPropertyHeight.html

#  [MaterialPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.html).GetPropertyHeight
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
public float GetPropertyHeight([MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) prop, string label, [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html) editor); 
### Parameters
Parameter | Description  
---|---  
prop | The [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) to make the custom GUI for.  
label | The label of this property.  
editor | Current material editor.  
### Description
Override this method to specify how tall the GUI for this property is in pixels.
The default is one line high.
* * *
