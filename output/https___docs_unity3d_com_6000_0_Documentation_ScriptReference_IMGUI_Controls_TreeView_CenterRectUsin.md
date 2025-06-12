* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CenterRectUsingSingleLineHeight.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).CenterRectUsingSingleLineHeight
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
protected void CenterRectUsingSingleLineHeight(ref [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect); 
### Parameters
Parameter | Description  
---|---  
rect | Rect to be modified and centered.  
### Description
Modifies the input rect so it is centered and have a height equal to [EditorGUIUtility.singleLineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html).
This method can be used in [RowGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUI.html) for centering and adjusting the row rect using [EditorGUIUtility.singleLineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html). In general it is a good idea to use a rect with [EditorGUIUtility.singleLineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html) for labels and controls if working with row heights larger than the default row height.  
  
Additional resources: ::RowGUI.
* * *
