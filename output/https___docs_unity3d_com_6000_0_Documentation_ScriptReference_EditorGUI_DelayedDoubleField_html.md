* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedDoubleField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).DelayedDoubleField
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
public static double DelayedDoubleField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, double value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static double DelayedDoubleField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, double value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static double DelayedDoubleField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, double value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the double field.  
label | Optional label to display in front of the double field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**double** The value entered by the user. Note that the return value will not change until the user has pressed enter or focus is moved away from the double field. 
### Description
Makes a delayed text field for entering doubles.
Similar to [EditorGUI.DoubleField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DoubleField.html) but will not return the new value until the user has pressed enter or focus is moved away from the double field.
* * *
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the double field.  
property | The double property to edit.  
label | Optional label to display in front of the double field. Pass [GUIContent.none](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html) to hide label.  
### Description
Makes a delayed text field for entering doubles.
Similar to [EditorGUI.DoubleField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DoubleField.html) but will not return the new value until the user has pressed enter or focus is moved away from the double field.
* * *
