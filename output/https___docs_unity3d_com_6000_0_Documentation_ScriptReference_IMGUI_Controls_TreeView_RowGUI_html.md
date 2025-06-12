* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUI.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).RowGUI
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
protected void RowGUI([IMGUI.Controls.TreeView.RowGUIArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.html) args); 
### Parameters
Parameter | Description  
---|---  
args | Row data.  
### Description
Override this method to add custom GUI content for the rows in the TreeView.
This method is called once per visible row. The _See Also_ section below links to methods and properties that can be used to tweak where the default icon, text and foldout arrow are rendered and other useful information when doing custom row content.  
  
If the TreeView is used in combination with a [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html) then use the methods of RowGUIArgs to access information for the columns. See the manual for examples.  
  
Additional resources: [GetContentIndent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetContentIndent.html), [GetFoldoutIndent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetFoldoutIndent.html).
* * *
