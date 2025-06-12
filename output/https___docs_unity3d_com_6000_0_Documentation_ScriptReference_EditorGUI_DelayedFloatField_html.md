* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedFloatField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).DelayedFloatField
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
public static float DelayedFloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static float DelayedFloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static float DelayedFloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the float field.  
label | Optional label to display in front of the float field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**float** The value entered by the user. Note that the return value will not change until the user has pressed enter or focus is moved away from the float field. 
### Description
Makes a delayed text field for entering floats.
Similar to [EditorGUI.FloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html) but will not return the new value until the user has pressed enter or focus is moved away from the float field.
* * *
## Declaration
public static void DelayedFloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label = null); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the float field.  
property | The float property to edit.  
label | Optional label to display in front of the float field. Pass [GUIContent.none](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html) to hide label.  
### Description
Makes a delayed text field for entering floats.
Similar to [EditorGUI.FloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html) but will not return the new value until the user has pressed enter or focus is moved away from the float field.
* * *
