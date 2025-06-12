* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.HandlePrefixLabel.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).HandlePrefixLabel
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
public static void HandlePrefixLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) labelPosition, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int id = 0, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.label); 
### Parameters
Parameter | Description  
---|---  
totalPosition | Rectangle on the screen to use in total for both the label and the control.  
labelPosition | Rectangle on the screen to use for the label.  
label | Label to show for the control.  
id | The unique ID of the control. If none specified, the ID of the following control is used.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the label.  
### Description
Makes a label for some control.
HandlePrefixLabel is like PrefixLabel but allows custom control over the label position by supplying its [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) explicitly. PrefixLabel or HandlePrefixLabel should be used when creating a control with a connected label. It ensures that when the label is clicked, the control will get keyboard focus. For this reason it is important that the same ID is supplied to PrefixLabel or HandlePrefixLabel as to the control itself. It is also possible to not supply a Control ID, in which case the one from the immediately following control is automatically used.
* * *
