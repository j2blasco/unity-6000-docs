* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html

# MenuItem
class in UnityEditor
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
### Description
The `MenuItem` attribute allows you to add menu items to the main menu and Inspector window context menus.
The `MenuItem` attribute turns any static function into a menu command. Only static functions can use the `MenuItem` attribute.  
  
To create a hotkey, use the following special characters: 
  * **%** : Represents **Ctrl** on Windows and Linux. **Cmd** on macOS.
  * **^** : Represents **Ctrl** on Windows, Linux, and macOS.
  * **#** : Represents **Shift**.
  * **&** : Represents **Alt**.


If no special modifier key combinations are required, the key can be given after an underscore. For example, to create a menu with the hotkeys **Shift+Alt+G** , use `"MyMenu/Do Something #&g"`. To create a menu with hotkey **G** with no required key modifiers to press, use `"MyMenu/Do Something _g"`.   
  
A space character must precede hotkey text. For example, `"MyMenu/Do_g"` isn't interpreted as a hotkey, but `"MyMenu/Do _g"` is.  
  
Some special keyboard keys are supported as hotkeys. For example, "#LEFT" would map to Shift-Left. The keys supported like this are: LEFT, RIGHT, UP, DOWN, F1 .. F12, HOME, END, PGUP, PGDN, INS, DEL, BACKSPACE, TAB, and SPACE.  
  
When adding menu items to the "GameObject/" menu to create custom GameObjects, be sure to call [GameObjectUtility.SetParentAndAlign](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetParentAndAlign.html) to ensure that the new GameObject is reparented correctly in the case of a context click (see example below). Your function should also call [Undo.RegisterCreatedObjectUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html) to make the creation undoable and set [Selection.activeObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) to the newly created object. Also note that in order for a menu item in "GameObject/" to be propagated to the hierarchy Create dropdown and hierarchy context menu, it must be grouped with the other GameObject creation menu items. This can be achieved by setting its priority to 10 (see example below). Note that for legacy purposes MenuItems in "GameObject/Create Other" with no explicit priority set will receive a priority of 10 instead of the default 1000 - we encourage using a more descriptive category name than "Create Other" and explicitly setting the priority to 10.  
  
You can use `MenuItem` to add menu items to the right-click context menu in the Project window. The context menu in the Project window uses the same menu items as the Assets menu. When you add a menu item to the Assets menu, that menu item is also added to the context menu in the Project window. For example, `"Assets/Do something"` adds the `Do something` menu item to the context menu in the Project window. 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class MenuTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Add a menu item named "Do Something" to MyMenu in the menu bar.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Do Something")]
    static void DoSomething()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Doing Something...");
    }  
  
    // Add a menu item named "Log Selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Name" to MyMenu in the menu bar.
    // We want this to be validated menu item: an item that is only enabled if specific conditions are met.
    // To achieve this, we use a second function below to validate the menu item.
    // so it will only be enabled if we have a transform selected.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Log Selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Name")]
    static void LogSelectedTransformName()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) is on " + Selection.activeTransform.gameObject.name + ".");
    }  
  
    // Validate the menu item defined by the function above.
    // The "Log Selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Name" menu item is disabled if this function returns false.
    // We tell the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) that this is a validation function by decorating it with a MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html) attribute
    // and passing true as the second parameter.
    // This invokes the MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)(string itemName, bool isValidateFunction) attribute constructor
    // resulting in the function being treated as the validator for "Log Selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Name" menu item.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Log Selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Name", true)]
    static bool ValidateLogSelectedTransformName()
    {
        // Return false if no transform is selected.
        return Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html) != null;
    }  
  
    // Add a menu item named "Do Something with a Shortcut Key" to MyMenu in the menu bar
    // and give it a shortcut (ctrl-g on Windows, cmd-g on macOS).
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Do Something with a Shortcut Key %g")]
    static void DoSomethingWithAShortcutKey()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Doing something with a Shortcut Key...");
    }  
  
    // Add a menu item called "Double Mass" to a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)'s context menu.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CONTEXT/Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)/Double Mass")]
    static void DoubleMass(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) command)
    {
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) body = (Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html))command.context;
        body.mass = body.mass * 2;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Doubled Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)'s Mass to " + body.mass + " from Context Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html).");
    }  
  
    // Add a menu item to create custom GameObjects.
    // Priority[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.html) 10 ensures it is grouped with the other menu items of the same kind
    // and propagated to the hierarchy dropdown and hierarchy context menus.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/MyCategory/Custom Game Object", false, 10)]
    static void CreateCustomGameObject(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) menuCommand)
    {
        // Create a custom game object
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Custom Game Object");
        // Ensure it gets reparented if this was a context click (otherwise does nothing)
        GameObjectUtility.SetParentAndAlign[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetParentAndAlign.html)(go, menuCommand.context as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html));
        // Register the creation in the undo system
        Undo.RegisterCreatedObjectUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html)(go, "Create " + go.name);
        Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = go;
    }  
  
    // Add a menu item called "Test" to the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view context menu when the
    // EditorToolContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) "TestToolContext" is engaged.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CONTEXT/TestToolContext/Test")]
    static void TestToolContextItem()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Testing Test Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) Context Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)");
    }  
  
    // Add a menu item called "Test" to the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view context menu when the
    // EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) "TestTool" is engaged.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CONTEXT/TestTool/Test")]
    static void TestToolItem()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Testing Test Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)");
    }
}
```

### Constructors
Constructor | Description  
---|---  
[MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem-ctor.html) | Creates a menu item and invokes the static function that follows it when the menu item is selected.  
* * *
