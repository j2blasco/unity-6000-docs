* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.AppendAction.html

#  [DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html).AppendAction(string,Action<DropdownMenuAction>,Func<DropdownMenuAction,DropdownMenuAction.Status>,object)
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
actionName | The name of the item. This name is displayed in the dropdown menu.  
action | The callback to execute when the user selects this item in the menu.  
actionStatusCallback | The callback to execute to determine the status of this item.  
userData | The object to store in the <b>userData</b> property of the <see cref="DropdownMenuAction" /> item.  
### Description
Adds an item that executes an action in the dropdown menu. 
The item is added to the end of the current item list.   
  

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
            e.menu.AppendAction("Submenu/My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1", a => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) 1 Works"), action =>
            {
                action.tooltip = "Status[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.html) dependent tooltip";
                return DropdownMenuAction.Status.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.Status.Normal.html);
            }, null);
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
actionName | The name of the item. This name is displayed in the dropdown menu.  
action | The callback to execute when the user selects this item in the menu.  
status | The status of the item.  
### Description
Adds an item that executes an action in the dropdown menu. 
The item is added to the end of the current item list.   
  

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
        }));  
  
        rootVisualElement.Add(contextMenuContainer);
    }
}

```

* * *
