* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LongField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).LongField
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
public static long LongField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, long value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static long LongField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, long value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the long field.  
label | Optional label to display in front of the long field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**long** The value entered by the user. 
### Description
Makes a text field for entering long integers.
Additional resources: [IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntField.html), [FloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html), [DoubleField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DoubleField.html).
* * *
