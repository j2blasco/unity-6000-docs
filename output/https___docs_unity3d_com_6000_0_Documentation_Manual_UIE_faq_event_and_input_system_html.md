* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * [Configure runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-render-runtime-ui.html)
  * FAQ for input and event systems with UI Toolkit


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)
Runtime UI event system and input handling
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
Performance consideration for runtime UI
# FAQ for input and event systems with UI Toolkit
This page includes frequently asked questions for using the **event system** A way of sending events to objects in the application based on input, be it keyboard, mouse, touch, or custom input. The Event System consists of a few components that work together to send events. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#EventSystem) and the input system with UI Toolkit.
  1. [How do I know if the mouse is over a visual element from a runtime panel?](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html#mouse-over)
  2. [How can I remap basic UI actions?](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html#remap)
  3. [How can I change what element is focused next when using directional navigation?](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html#directional-nav)
  4. [Is it possible to get rid of WASD inputs for directional navigation or space bar for the submit action?](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html#wasd)
  5. [How can I start entering keyboard input without ever clicking anywhere with the mouse?](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html#enter-keyboard)


## How do I know if the mouse is over a visual element from a runtime panel?
You can do this by two methods:
**First method**
  1. Add an Event System component in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) the same way as you create GameObject-based UI content from the [`com.unity.uGUI`](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ugui.html) package.
  2. Use the [`EventSystem.current.IsPointerOverGameObject`](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.EventSystem.html?q=eventsystem#UnityEngine_EventSystems_EventSystem_IsPointerOverGameObject) method, which returns `true` if the pointer is over UI content from either uGUI or from UI Toolkit.
  3. Use the [`EventSystem.current.RaycastAll`](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.EventSystem.html?q=eventsystem#UnityEngine_EventSystems_EventSystem_RaycastAll_UnityEngine_EventSystems_PointerEventData_System_Collections_Generic_List_UnityEngine_EventSystems_RaycastResult__) method to see what **visual element** is under the mouse.
  4. Intersected UI Toolkit Panels are represented in the Event System’s environment through a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject):
     * The GameObject’s name matches the corresponding PanelSettings.
     * The GameObject’s parent is the GameObject that holds the current Event System component.
     * The GameObject has two components, `PanelRaycaster` and `PanelEventHandler`. Both components have a `panel` property that returns the `IPanel` it targets.


After you find the panel under the pointer, call the [`panel.Pick`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.Pick.html) method to find what visual element lies at the pointer’s position.
You must use the [`RuntimePanelUtils.ScreenToPanel`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.ScreenToPanel.html) method to transform the pointer’s screen coordinates into panel coordinates.
uGUI’s screen coordinate system uses a bottom-left origin whereas UI Toolkit screen coordinates are expressed from the top-left. Conversion between the two systems requires that you mirror the Y coordinate with `yTopLeft = Screen.height - yBottomLeft`, and vice versa.
**Second method**
  1. Use the `UIDocument.rootVisualElement` property from one UIDocument per distinct PanelSettings used to get the list of all the runtime panels that could be under the pointer, which you can gather
  2. Go through the panels manually in order of depth and call [`panel.Pick`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.Pick.html) on each of them successively until you find one that returns a visual element.


## How can I remap basic UI actions?
To remap basic UI actions:
  1. Add an Event System component in your scene the same way as you create GameObject-based UI content from the [`com.unity.uGUI`](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ugui.html) package.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, configure the **Stand alone Input Module** or **Input System UI Input Module** fields to control what input maps to each action.


**Note** : The actions mapped to Tab and Shift+Tab inputs can’t be remapped because they’re not exposed through the Event System input modules.
## How can I change what element is focused next when using directional navigation?
You can configure directional navigation to have other targets other than the default ones.
The following code example allows element A to navigate to elements U, D, L, R when navigating up, down, left, and right respectively:
```
A.RegisterCallback <NavigationMoveEvent>(e =>
{
    switch(e.direction)
    {
        case NavigationMoveEvent.Direction.Up: U.Focus(); break;
        case NavigationMoveEvent.Direction.Down: D.Focus(); break;
        case NavigationMoveEvent.Direction.Left: L.Focus(); break;
        case NavigationMoveEvent.Direction.Right: R.Focus(); break;
    }
    e.PreventDefault();
});

```

## Is it possible to get rid of WASD inputs for directional navigation or space bar for the submit action?
Yes. You can use the EventSystem’s **StandaloneInputModule** or **InputSystemUIInputModule** fields in the Inspector window to control what input maps to each action. However, since these actions are shared with uGUI input, this also changes the uGUI controls.
To remap UI Toolkit inputs without affecting uGUI controls, disable UI Toolkit’s runtime event handling and send all events manually to panels. To do so, call `EventSystem.SetUITookitEventSystemOverride(null, true, false);` before the start method of your current EventSystem kicks in, such as the `Awake` method of the component of your scene. For more information about this uGUI method, see [SetUITookitEventSystemOverride](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.EventSystem.html?q=eventsystem#UnityEngine_EventSystems_EventSystem_SetSelectedGameObject_UnityEngine_GameObject_).
## How can I start entering keyboard input without ever clicking anywhere with the mouse?
It’s possible that no element or panel is in focus at a given time, such as when loading your game scene for the first time. In this case, keyboard navigation doesn’t start from a predictable first element. This can be a problem for a game that plays entirely without a mouse.
You add C# script to allow a predictable navigation behavior from the start, and attach your script to the same GameObject as the UIDocument responsible for the element that you choose to get the initial focus.
Assume your script is named `FirstFocus` and your initial focused element is named as `first-focused`. In your script’s `Start()` method, add a line to focus that element as the following:
```
public class FirstFocus : MonoBehaviour
{
    void Start()
    {
        FocusFirstElement();
    }

    public void FocusFirstElement()
    {
        GetComponent<UIDocument>().rootVisualElement.
            Q<VisualElement>("first-focused").Focus();
    }
}

```

**Note** : If you disable the UIDocument’s GameObject, all its underlying hierarchy is recreated from scratch. Therefore, you must run your custom `FocusFirstElement()` method again after you re-enable the GameObject.
## Additional resources
  * [Get started with runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-runtime-ui.html)
  * [Render UI in the Game view](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-render-runtime-ui.html)
  * [The Panel Settings asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
  * [Runtime event system](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)
  * [Control behavior with Events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * [Handle events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)
Runtime UI event system and input handling
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
Performance consideration for runtime UI
