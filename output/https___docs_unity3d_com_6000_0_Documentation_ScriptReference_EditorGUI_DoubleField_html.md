* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DoubleField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).DoubleField
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
public static double DoubleField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, double value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static double DoubleField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, double value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static double DoubleField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, double value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the double field.  
label | Optional label to display in front of the double field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**double** The value entered by the user. 
### Description
Makes a text field for entering doubles.
Additional resources: [FloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html), [IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntField.html), [LongField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LongField.html).
* * *
