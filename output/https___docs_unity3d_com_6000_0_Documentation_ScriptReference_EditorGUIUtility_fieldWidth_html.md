* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-fieldWidth.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).fieldWidth
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
fieldWidth; 
### Description
The minimum width in pixels reserved for the fields of Editor GUI controls.
Most Editor GUI controls consist of a label as well as the control field itself. The minimum width of the field is controlled by the fieldWidth value. Fields often appear wider than the minimum width, since Editor GUI controls are usually set to occupy a [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) that expands to fill the available horizontal space. Within this Rect, the field will take up all the space not used by the [EditorGUIUtility.labelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-labelWidth.html).  
  
The fieldWidth also controls the width of the text field in [EditorGUI.Slider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html) controls.
* * *
