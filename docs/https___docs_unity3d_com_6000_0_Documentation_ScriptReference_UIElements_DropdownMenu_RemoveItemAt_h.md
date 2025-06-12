* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.RemoveItemAt.html

#  [DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html).RemoveItemAt
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
public void RemoveItemAt(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the item to remove.  
### Description
Removes the menu item at index. 
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
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  
  
            e.menu.RemoveItemAt(0); // Remove My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1
            e.menu.RemoveItemAt(1); // Remove My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3 (item indices have shifted after first removal)
        }));  
  
        rootVisualElement.Add(contextMenuContainer);
    }
}

```

* * *
