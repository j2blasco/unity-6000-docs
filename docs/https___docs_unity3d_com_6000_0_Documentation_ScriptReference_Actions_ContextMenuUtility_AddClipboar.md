* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.AddClipboardEntriesTo.html

#  [ContextMenuUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.html).AddClipboardEntriesTo
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
public static void AddClipboardEntriesTo([UIElements.DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) menu); 
## Declaration
public static void AddClipboardEntriesTo([UIElements.DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) menu, bool cutEnabled, bool copyEnabled, bool pasteEnabled, bool duplicateEnabled, bool deleteEnabled); 
### Parameters
Parameter | Description  
---|---  
menu | The Scene view context menu to add a clipboard operations to.  
cutEnabled | Whether to enable the Cut operation in the Scene view context menu. When Cut is disabled, it is greyed out in the Scene view context menu.  
copyEnabled | Whether to enable the Copy operation in the Scene view context menu. If Copy is disabled, it is greyed out in the Scene view context menu.  
pasteEnabled | Whether to enable the Paste operation in the Scene view context menu. If Paste is disabled, it is greyed out in the Scene view context menu.  
duplicateEnabled | Whether to enable the Duplicate operation in the Scene view context menu. If Duplicate is disabled, it is greyed out in the Scene view context menu.  
deleteEnabled | Whether to enable the Delete operation in the Scene view context menu. If Delete is disabled, it is greyed out in the Scene view context menu.  
### Description
Adds clipboard operations to the Scene view context menu.
By default, the Cut, Copy, Duplicate, and Delete operations are greyed out in the Scene view context menu if you do not have a GameObject selected in the Scene. The Paste operation is greyed out if the clipboard is empty. The method overload provides additional control over whether these operations are greyed out.
* * *
