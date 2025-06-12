* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.InsertAction.html

#  [DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html).InsertAction(int,string,Action<DropdownMenuAction>,Func<DropdownMenuAction,DropdownMenuAction.Status>,object)
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
### Parameters
Parameter | Description  
---|---  
atIndex | The index to insert the item at.  
actionName | The name of the item. This name is displayed in the dropdown menu.  
action | Callback to execute when the user selects this item in the menu.  
actionStatusCallback | The callback to execute to determine the status of the item.  
userData | The object to store in the <b>userData</b> property of the <see cref="DropdownMenuAction" /> item. This object is accessible through the action callback.  
### Description
Adds an item that executes an action in the dropdown menu. 
The item is added to the end of the specified index in the list.   
  

```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;  
  
public class ContextMenuWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("My/Context Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) Window")]
    static void ShowMe() => GetWindow<ContextMenuWindow>();  
  
    void CreateGUI()
    {
        var contextMenuContainer = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
        contextMenuContainer.style.flexGrow = 1;
        contextMenuContainer.AddManipulator(new ContextualMenuManipulator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html)(e =>
        {
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 0
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 1
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 4", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 4 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 2
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 6", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 6 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 3  
  
            // Indices from 1 to 3 are shifted up index by 1. In result 'My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2' now has an index of 2.
            e.menu.InsertAction(1, "My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2 Works"), DropdownMenuAction.AlwaysEnabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.AlwaysEnabled.html));  
  
            // If we want to insert an between submenu items, we have to use shifted indices
            e.menu.InsertAction(4, "Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 5", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 5 Works"), DropdownMenuAction.AlwaysDisabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.AlwaysDisabled.html));
        }));  
  
        rootVisualElement.Add(contextMenuContainer);
    }
}

```

* * *
### Parameters
Parameter | Description  
---|---  
atIndex | The index to insert the item at.  
actionName | The name of the item. This name is displayed in the dropdown menu.  
action | The callback to execute when the user selects this item in the menu.  
status | The status of the item.  
### Description
Adds an item that executes an action in the dropdown menu. 
The item is added to the end of the specified index in the list.   
  

```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;  
  
public class ContextMenuWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("My/Context Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) Window")]
    static void ShowMe() => GetWindow<ContextMenuWindow>();  
  
    void CreateGUI()
    {
        var contextMenuContainer = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
        contextMenuContainer.style.flexGrow = 1;
        contextMenuContainer.AddManipulator(new ContextualMenuManipulator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html)(e =>
        {
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 0
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 1
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 4", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 4 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 2
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 6", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 6 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 3  
  
            // Indices from 1 to 3 are shifted up index by 1. In result 'My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2' now has an index of 2.
            e.menu.InsertAction(1, "My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  
  
            // If we want to insert an between submenu items, we have to use shifted indices
            e.menu.InsertAction(4, "Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 5", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 5 Works"), DropdownMenuAction.Status.Disabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Disabled.html));
        }));  
  
        rootVisualElement.Add(contextMenuContainer);
    }
}

```

* * *
