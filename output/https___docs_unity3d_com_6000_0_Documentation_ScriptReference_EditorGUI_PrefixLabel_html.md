* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).PrefixLabel
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
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) PrefixLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) PrefixLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) PrefixLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, int id, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) PrefixLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, int id, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
totalPosition | Rectangle on the screen to use in total for both the label and the control.  
id | The unique ID of the control. If none specified, the ID of the following control is used.  
label | Label to show in front of the control.  
style | Style to use for the label.  
### Returns
**Rect** Rectangle on the screen to use just for the control itself. 
### Description
Makes a label in front of some control.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIPrefixLabel.png)   
_Prefix Label in an Editor Window._  
  
Note that most editor controls already have built-in optional labels that can be specified as one of the parameters. PrefixLabel can be used when there is no such built-in label available, or when you're creating your own editor control from scratch.  
  
PrefixLabel takes a rect that's the rect for the entire control, including the label, and returns a rect that's for just the control itself, without the label.  
  
PrefixLabel also ensures that when the label is clicked, the linked control will get keyboard focus (if the control supports keyboard focus). The ID of the linked control can optionally be specified, or if no ID is given, the label is automatically linked to the following control coming after it.
* * *
