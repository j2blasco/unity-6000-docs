* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MultiIntField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).MultiIntField
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
public static void MultiIntField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, GUIContent[] subLabels, int[] values); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the integer field.  
subLabels | Array with small labels to show in front of each int field. There is room for one letter per field only.  
values | Array with the values to edit.  
### Description
Makes a multi-control with text fields for entering multiple integers in the same line.
The height of the multi-control depends on the total width of its editor window. The control is drawn within the specified rectangle (position). If the control does not fit, it is drawn outside the rectangle. Additional resources: [EditorGUIUtility.wideMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-wideMode.html).
* * *
