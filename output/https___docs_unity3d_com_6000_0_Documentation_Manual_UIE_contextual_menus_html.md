* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-contextual-menus.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * [Event reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)
  * Contextual menu events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transition-Events.html)
Transition events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-IMGUI-Events.html)
IMGUI events
# Contextual menu events
Use the contextual menu events, [`ContextualMenuManipulator`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html) and [`ContextualMenuPopulateEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuPopulateEvent.html), to display a set of choices when a user performs certain actions, such as when a user right-clicks a label. 
## Enable contextual menus
To enable contextual menus, attach the [`ContextualMenuManipulator`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html) to a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). This manipulator displays a contextual menu after either a right button mouse up event or a menu key up event. The `ContextualMenuManipulator` manipulator also adds a callback that responds to a [`ContextualMenuPopulateEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuPopulateEvent.html). 
The following code example adds a contextual menu to a visual element. The menu has only one item.
```
void InstallManipulator(VisualElement element)
{
    ContextualMenuManipulator m = new ContextualMenuManipulator(MyDelegate);
    m.target = element;
}

void MyDelegate(ContextualMenuPopulateEvent evt)
{
    // Modify evt.menu
    evt.menu.AppendAction("My action", DisplayProperties, DropdownMenuMenuAction.AlwaysEnabled);
}

void DisplayProperties(DropdownMenu.MenuAction menuItem)
{
    // ...
}

```

The callback given to the `ContextualMenuManipulator` constructor is invoked last so child elements can populate the menu.
The manipulator sends a `ContextualMenuPopulateEvent` event propagated to the target element hierarchy. The event moves along the propagation path: from the root of the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree) to the event target, and then back up the visual tree to the root. Along the propagation path, the elements with a callback for the `ContextualMenuPopulateEvent` event can add, remove, or update items in the contextual menu.
## Respond to the user selection
When an element receives a `ContextualMenuPopulateEvent`, it calls either [`DropdownMenu.InsertAction()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.InsertAction.html) or [`DropdownMenu.AppendAction()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.AppendAction.html) to add menu items to the contextual menu. [`DropdownMenu.InsertAction()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.InsertAction.html) and [`DropdownMenu.AppendAction()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.AppendAction.html) take two callbacks as parameters. The first callback executes when the user selects the item in the menu. The second callback executes before it displays the menu and also checks whether the menu item is enabled.
Both callbacks receive a `MenuAction` as a parameter. The `MenuAction` represents the menu item and has the following properties:
  * `MenuAction.userData` includes a reference to user data used with `AppendAction()` or `InsertAction()`.
  * `MenuAction.eventInfo` includes information about the event that displays the contextual menu. Use `MenuAction.eventInfo` in the action that responds to the event. For example, you can use the mouse position to create and place an object based on the selected contextual menu item.


## Examples
The following example creates a custom Editor window with two labels and adds contextual menus for each label. The example demonstrates how to add, remove, and update a contextual menu.
  1. Create a Unity project with any template.
  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `Editor`.
  3. In the `Editor` window, create a C# script named `ContextualMenuDemo` and replace its contents with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;

public class ContextualMenuDemo : EditorWindow
{
    [MenuItem("Window/ContextualMenuDemo")]
    public static void ShowExample()
    {
        ContextualMenuDemo wnd = GetWindow<ContextualMenuDemo>();
        wnd.titleContent = new GUIContent("ContextualMenuDemo");
    }

    public void CreateGUI()
    {
        VisualElement root = rootVisualElement;
        VisualElement label = new Label("Right click me!");
        root.Add(label);

        AddANewContextMenu(label);
        InsertIntoAnExistingMenu(label);

        VisualElement second = new Label("Click me also!");
        root.Add(second);

        AddANewContextMenu(second);
        InsertIntoAnExistingMenu(second);

        // Override the default behavior by clearing the menu.
        ReplaceContextMenu(second);
    }

    void AddANewContextMenu(VisualElement element)
    {
        // The manipulator handles the right click and sends a ContextualMenuPopulateEvent to the target element.
        // The callback argument passed to the constructor is automatically registered on the target element.
        element.AddManipulator(new ContextualMenuManipulator((evt) =>
        {
            evt.menu.AppendAction("First menu item", (x) => Debug.Log("First!!!!"), DropdownMenuAction.AlwaysEnabled);
            evt.menu.AppendAction("Second menu item", (x) => Debug.Log("Second!!!!"), DropdownMenuAction.AlwaysEnabled);
        }));
    }

    void InsertIntoAnExistingMenu(VisualElement element)
    {
        element.RegisterCallback<ContextualMenuPopulateEvent>((evt) =>
        {
            evt.menu.AppendSeparator();
            evt.menu.AppendAction("Another action", (x) => Debug.Log("Another Action!!!!"), DropdownMenuAction.AlwaysEnabled);
        });
    }

    void ReplaceContextMenu(VisualElement element)
    {
        element.RegisterCallback<ContextualMenuPopulateEvent>((evt) =>
        {
            evt.menu.ClearItems();
            evt.menu.AppendAction("The only action", (x) => Debug.Log("The only action!"), DropdownMenuAction.AlwaysEnabled);
        });
    }

}

```

  4. To see the example live, from the menu, select **Window** > **UI Toolkit** > **ContextualMenuDemo**. 


## Additional resources
  * [UXML element reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transition-Events.html)
Transition events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-IMGUI-Events.html)
IMGUI events
