* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.AddMenuItemsForType.html

#  [ContextMenuUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.html).AddMenuItemsForType
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
public static void AddMenuItemsForType([UIElements.DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) menu, IEnumerable<T> targets); 
## Declaration
public static void AddMenuItemsForType([UIElements.DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) menu, Type type, IEnumerable<Object> targets, string submenu); 
### Parameters
Parameter | Description  
---|---  
menu | The context menu to add all [MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html) for a specific type to.  
targets | The target objects for the menu items.  
type | The object type to search for when collecting context menu items.  
submenu | Optional name of the submenu category to filter results by.  
### Description
Adds all [MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html) of a specific type to the Scene view context menu.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Actions;
using UnityEditor.Overlays;
using UnityEngine;
using UnityEngine.UIElements;

[Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)(typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)), "Context Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) Example", defaultDisplay = true)]
class ContextMenuExample : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CONTEXT/Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)/Print Selected")]
    static void Init(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) cmd)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Selected transforms: {cmd.context}");
    }

    static void PopulateMenuItems(ContextualMenuPopulateEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuPopulateEvent.html) evt)
    {
        ContextMenuUtility.AddMenuItemsForType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.AddMenuItemsForType.html)(evt.menu, typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)), Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html));
    }

    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent()
    {
        var root = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
        ContextualMenuManipulator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html) manipulator = new ContextualMenuManipulator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html)(PopulateMenuItems);
        manipulator.target = root;
        const string text = "Context click here to show the context menu items for the selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) components.";
        root.Add(new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)(text));
        root.style.width = 256;
        root.style.height = 128;
        return root;
    }
}


```

* * *
