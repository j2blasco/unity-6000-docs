* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.InsertSeparator.html

#  [DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html).InsertSeparator
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
public void InsertSeparator(string subMenuPath, int atIndex); 
### Parameters
Parameter | Description  
---|---  
subMenuPath | The submenu path to add the separator to. Path components are delimited by forward slashes ('/').  
atIndex | The index to insert the separator at.  
### Description
Adds a separator line in the menu. 
The separator is added at the end of the specified index in the list.   
  

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
            e.menu.AppendAction("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 1
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 3 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 2
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 4", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 4 Works"), DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html));  // 3  
  
            e.menu.InsertSeparator("/", 1);     // Indices from 1 to 3 are shifted up index by 1. In result 'My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 2' now has an index of 2.
            e.menu.InsertSeparator("Submenu/", 4);  // If we want to insert a separator between submenu items, we have to use shifted indices
        }));  
  
        rootVisualElement.Add(contextMenuContainer);
    }
}

```

* * *
