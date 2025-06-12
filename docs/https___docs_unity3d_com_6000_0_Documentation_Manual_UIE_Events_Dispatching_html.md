* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * Dispatch events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
Control behavior with events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-capture-the-pointer.html)
Capture the pointer with a manipulator
# Dispatch events
The **event system** A way of sending events to objects in the application based on input, be it keyboard, mouse, touch, or custom input. The Event System consists of a few components that work together to send events. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#EventSystem) listens for events that come from the operating system or **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), then uses the [EventDispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcher.html) to dispatch those events to **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). The event dispatcher determines an appropriate dispatching strategy for each event it sends. Once determined, the dispatcher executes the strategy.
Visual elements implement default behaviors for several events. This involves the creation and execution of additional events. For example, a [`PointerMoveEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html) can generate an additional [`PointerEnterEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEnterEvent.html) and a [`PointerLeaveEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerLeaveEvent.html). These events enter a queue and process after the current event. For example, the `PointerMoveEvent` finishes processing before the `PointerEnterEvent` and `PointerLeaveEvent` events.
## Dispatch behavior of event types
Each event type has its own dispatch behavior. The behavior of each event type breaks down into two stages:
  * **Trickles down** : Events sent to elements during the trickle-down phase.
  * **Bubbles up** : Events sent to elements during the bubble-up phase.


For a list of dispatch behavior for each event type, see the [Event reference page](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html).
## Event propagation
After the event dispatcher selects the event target, it computes the propagation path of the event. The propagation path is an ordered list of visual elements that receive the event. The propagation path occurs in the following order:
  1. The path starts at the root of the visual element tree and descends towards the target. This is the **trickle-down phase**.
  2. The event target receives the event.
  3. The event then ascends the tree towards the root. This is the **bubble-up phase**.

![Propagation path](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIElementsEvents.png) Propagation path
Most event types are sent to all elements along the propagation path. Some event types skip the bubble-up phase, and some event types are sent to the event target only.
If you hide or disable an element, it won’t receive events. Events still propagate to the ancestors and descendants of a hidden or disabled element.
## Event target
As an event travels along the propagation path, `Event.currentTarget` updates to the element handling the event. Within an event callback function, there are two properties that log the dispatch behavior:
  * [`EventBase.currentTarget`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-currentTarget.html) is the visual element on which the callback was registered.
  * [`EventBase.target`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-target.html) is the element where the event occurs, for example, the element directly under the pointer.


The target of an event depends on the event type. For pointer events, the target is most commonly the topmost pickable element, directly under the pointer. For keyboard events, the target is the element that has focus.
UI Toolkit events have a `target` property that contains a reference to the element where the event occurred. For most events that originate from the operating system, the dispatch process finds the event target automatically.
The target element is stored in `EventBase.target` and doesn’t change during the dispatch process. The property `Event.currentTarget` updates to the visual element currently handling the event.
## Picking mode and custom shapes
Most pointer events use the picking mode to decide their target. The `VisualElement` class has a `pickingMode` property that supports the following values:
  * [`PickingMode.Position`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.Position.html) (default): performs picking based on the position rectangle.
  * [`PickingMode.Ignore`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.Ignore.html): prevents picking as the result of a pointer event.


You can override the [`VisualElement.ContainsPoint()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ContainsPoint.html) method to perform custom intersection logic.
## Additional resources
  * [Handle event callbacks and value changes](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
  * [Synthesize and send events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Synthesizing.html)
  * [Events reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
Control behavior with events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-capture-the-pointer.html)
Capture the pointer with a manipulator
