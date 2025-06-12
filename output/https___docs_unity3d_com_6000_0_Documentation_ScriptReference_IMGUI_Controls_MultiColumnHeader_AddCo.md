* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.AddColumnHeaderContextMenuItems.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).AddColumnHeaderContextMenuItems
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
protected void AddColumnHeaderContextMenuItems([GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu); 
### Parameters
Parameter | Description  
---|---  
menu | Context menu shown.  
### Description
Override this method to extend the default context menu items shown when context clicking the header area.
Call base.AddColumnHeaderContextMenuItems to add the default items. You can use currentColumnIndex to know which column was activated to open the contextual menu.
* * *
