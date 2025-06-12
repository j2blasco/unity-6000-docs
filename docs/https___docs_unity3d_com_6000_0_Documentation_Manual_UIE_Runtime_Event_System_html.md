* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * [Configure runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-render-runtime-ui.html)
  * Runtime UI event system and input handling


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-ui-document-component.html)
UI Document component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html)
FAQ for input and event systems with UI Toolkit
# Runtime UI event system and input handling
UI Toolkit uses an **event system** to handle input and send events to all active panels. This system processes input events and sends them to the appropriate elements in the UI.
## Use UI Toolkit with different input systems
Unity provides two input handling systems: the legacy [Input Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)Settings where you can define all the different input axes, buttons and controls for your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#InputManager) and the new [Input System package](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/index.html). The Input Manager is part of the core Unity platform and serves as the default system unless you install the Input System package. The new Input System package provides greater flexibility and broader devices and platforms support.
The UI Toolkit’s event system can receive events from both systems. The system automatically detects the active input handling system and processes events accordingly.
### Set the active input handling system
To set the active input handling system in your project:
  1. Select **Edit** > **Project Settings** > **Player**.
  2. In the **Player** window, under **Other Settings** > **Configuration** , set **Active Input Handling** to one of the following options:
     * **Input Manager (Old)** : Use the legacy Input Manager.
     * **Input System Package (New)** : Use the Input System package.
     * **Both** : Use the Input System package if available, otherwise fall back to the legacy Input Manager.


If the Input System package is active in your project, UI Toolkit automatically derives its events from actions defined in the input system. To [configure those actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/ActionsEditor.html), go to **Edit** > **Project Settings** > **Input System Package**.
### Set up input handling with the Input Manager
To set up input handling with Input Manager, go to **Edit** > **Project Settings** > **Input Manager**.
![Input Manager settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/input-manager-nav.png) Input Manager settings
You can configure the **Horizontal** and **Vertical** axes to influence how [`NavigationMoveEvents`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html) are generated in UI Toolkit. You can also modify the **Submit** and **Cancel** actions to generate [`NavigationSubmitEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationSubmitEvent.html) and [`NavigationCancelEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationCancelEvent.html) in UI Toolkit.
### Set up input handling with the Input System package
To set up input handling with the Input System package, go to **Edit** > **Project Settings** > **Input System Package**.
![Input System settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/input-system-nav.png) Input System settings
The Input System package offers enhanced configurability compared to Input Manager. You can use the project-wide actions asset to set up how `NavigationMoveEvents`, [`PointerMoveEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html) (“UI / Point” action), [`PointerDownEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html), [`PointerUpEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerUpEvent.html) (“UI / Click”), [`WheelEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.WheelEvent.html) (“UI / ScrollWheel”), `NavigationSubmitEvent`, and `NavigationCancelEvent` are generated for UI Toolkit.
## Use UI Toolkit and uGUI with different input systems
You can use UI Toolkit’s UI Documents and uGUI components at the same time. When you use UI Toolkit (and uGUI) with different input systems, you need to choose appropriate input modules.
The following table outlines the required components and settings for each input system usage:
**Usage** | **Required components** | **Active Input Handling**  
---|---|---  
**UI Toolkit elements with legacy Input Manager** | Default event system (No Scene component required) | **Input Manager (Old)**  
**UI Toolkit elements with Input System package** | Default event system (No Scene component required) |  **Input System Package (New)** or **Both**  
**UI Toolkit elements and uGUI components with legacy Input Manager** | A **Standalone Input Module** and an **EventSystem** component |  **Input Manager (Old)** or **Both**  
**UI Toolkit elements and uGUI components with Input System package** | An **Input System UI Input Module** and an **EventSystem** component |  **Input System Package (New)** or **Both**  
When you add your first uGUI element to the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), an [**EventSystem**](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/manual/script-EventSystem.html) and a [**Standalone Input Module**](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/manual/script-StandaloneInputModule.html) are automatically added to the Scene.
The **EventSystem** belongs to uGUI. It’s responsible for uGUI events, derived from either legacy Input Manager or the Input System package, through an interchangeable Input Module component.
The **Standalone Input Module** dispatches events to UI Toolkit elements.
When you activate the **Input System package** in your project, an [**Input System UI Input Module**](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/UISupport.html) is added instead of the **Standalone Input Module**. The **Input System UI Input Module** and its accompanying **EventSystem** ensure that the events from both UI Toolkit and uGUI elements are properly dispatched.
The **EventSystem** is responsible for reading the Scene and executing events, while the **Input System UI Input Module** processes input and initiates event execution. You can change the **Standalone Input Module** or **Input System UI Input Module** with other input modules, which can alter the type of input consumed. Regardless of the input module used, all events are executed through the **EventSystem**.
If you add and enable a uGUI **EventSystem** in the Scene, UI Toolkit detects it and creates two uGUI-compabible components for each UI Toolkit panel: [`PanelRaycaster`](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/api/UnityEngine.UIElements.PanelRaycaster.html) and [`PanelEventHandler`](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/api/UnityEngine.UIElements.PanelEventHandler.html). These components serve as intermediaries between uGUI events and UI Toolkit events. The presence of these components deactivates the UI Toolkit’s automated, built-in input processing. This means that the UI Toolkit relies on these components to handle input events when they are present.
If the Scene uses more than one Panel Settings asset, the event system dispatches pointer events to their panels based on their sorting order. UI Toolkit determines the recipient of pointer events by comparing the sorting order of its panel with that of uGUI canvases and other valid raycast targets. This process decides whether a UI Toolkit element, a uGUI object, or another object in the Scene receives the event. Similarly, UI Toolkit uses `currentSelectedGameObject` of the **EventSystem** to manage the focus. When a UI Toolkit panel wants to get focus, it removes the focus from other uGUI objects, and when a uGUI object becomes selected, UI Toolkit panels automatically lose their focus.
A pointer event propagates through the panels until a panel responds to it. The first panel that uses an event to affect the focused element becomes the focused panel for the event system. This panel continues to receive keyboard events until another event causes a different panel to become the focused panel.
**Note** : Stopping an event’s propagation and giving an element focus are distinct actions. For example, when you click a button, it stops the propagation and allows only the button to respond to the press, but it doesn’t prevent other default click actions, such as giving focus to the button or any clicked focusable element.
In some cases, you might need to add a one-frame delay after input is processed before requesting focus for an element, especially if that input affects focus through other code paths, as shown in the example below:
```
public class FocusOnNextFrameExample : MonoBehaviour
{
    void OnEnable()
    {
        var root = GetComponent<UIDocument>().rootVisualElement;
        root.Q<Button>("my-button").clicked += () =>
        {
            root.schedule.Execute(() => root.Q<TextField>("my-text-field").Focus());
        };
    }
}

```

## Additional resources
  * [Input System package](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/index.html)
  * [Get started with runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-runtime-ui.html)
  * [Render UI in the Game view](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-render-runtime-ui.html)
  * [Panel Settings properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
  * [FAQ for input and event systems with UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-ui-document-component.html)
UI Document component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html)
FAQ for input and event systems with UI Toolkit
