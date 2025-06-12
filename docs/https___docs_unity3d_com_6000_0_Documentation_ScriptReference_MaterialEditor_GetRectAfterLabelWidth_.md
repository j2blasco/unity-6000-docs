* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetRectAfterLabelWidth.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).GetRectAfterLabelWidth
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
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) GetRectAfterLabelWidth([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r); 
### Parameters
Parameter | Description  
---|---  
r | Line Rect.  
### Returns
**Rect** A sub rect of the input Rect. 
### Description
Utility method for GUI layouting ShaderGUI. This is the rect after the label which can be used for multiple properties. The input rect can be fetched by calling: EditorGUILayout.GetControlRect.
* * *
