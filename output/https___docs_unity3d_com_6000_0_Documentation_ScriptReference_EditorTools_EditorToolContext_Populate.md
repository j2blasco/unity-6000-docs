* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.PopulateMenu.html

#  [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html).PopulateMenu
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
public void PopulateMenu([UIElements.DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) menu); 
### Parameters
Parameter | Description  
---|---  
menu | The Scene view context menu to add menu items to.  
### Description
Adds menu items to the Scene view context menu.
Refer to MenuUtility for utility functions that add menu items to the Scene view context menu.
```
public override void PopulateMenu(DropdownMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) menu)
{
    // Add all clipboard operations to the context menu (Cut, Copy, Paste, Delete, and Duplicate).
    ContextMenuUtility.AddClipboardEntriesTo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.AddClipboardEntriesTo.html)(menu);

    // Add an item to the context menu using a delegate or an EditorAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html).
    menu.AppendAction("Parent Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)/Child Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)", (item) => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Executed Child Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)."));

    // Add an item to the context menu using a predefined MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html).
    ContextMenuUtility.AddMenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.AddMenuItem.html)(menu, "GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Move To View");
}

```

* * *
