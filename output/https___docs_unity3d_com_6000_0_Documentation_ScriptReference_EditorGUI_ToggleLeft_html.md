* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ToggleLeft.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).ToggleLeft
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
public static bool ToggleLeft([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelStyle = EditorStyles.label); 
## Declaration
public static bool ToggleLeft([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelStyle = EditorStyles.label); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the toggle.  
label | Label to display next to the toggle.  
value | The value to edit.  
labelStyle | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the label.  
### Returns
**bool** The value set by the user. 
### Description
Makes a toggle field where the toggle is to the left and the label immediately to the right of it.
[EditorGUI.ToggleLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ToggleLeft.html) is similar to [GUI.Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html) but respects the [EditorGUI.showMixedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-showMixedValue.html) property and handles keyboard focus consistent with other Editor controls.
* * *
