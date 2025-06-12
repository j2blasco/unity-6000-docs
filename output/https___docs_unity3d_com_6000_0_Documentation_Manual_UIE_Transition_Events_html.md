* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transition-Events.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * [Event reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)
  * Transition events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Tooltip-Events.html)
Tooltip event
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-contextual-menus.html)
Contextual menu events
# Transition events
Transition events inform you of the changes in a transition’s state.
UI Toolkit uses transitions when a `VisualElement`’s style property is modified. Changes to `VisualElement` property are immediately reflected visually. However, you can use the [`transition` USS property](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitions.html#transition-properties) to interpolate between the initial and end results gradually.
## The transition’s lifecycle
A transition’s lifecycle has the following stages:
  1. A `VisualElement`’s property is modified when you:
     * Add or remove a class with C# methods. For example: `element.ToggleInClassList()` (where `element` is any `VisualElement`).
     * Use USS with selectors like `:hover`.
     * Manipulate the element’s `style` property. For example: `element.style.backgroundColor = Color.red;` (where `element` is any `VisualElement`).
  2. A `TransitionRunEvent` is sent.
  3. If the resolved `transition-delay` property for the changing property has a value other than `0`, nothing happens for the duration of the delay.
  4. After the delay, a `TransitionStartEvent` is sent, and the transition starts with the property at its initial value.
  5. For the length of time set by `transition-duration`, the transition occurs. During that time, the property goes from its initial to its final value.
  6. If the property is changed to a new value during the transition, `TransitionCancelEvent` is sent. The transition process restarts at step 2.
  7. After the `transition-duration` elapses, the property sets to its final value. A `TransitionEndEvent` is sent.


## Transition events reference table
The following table describes the transition events and their propagation phases:
**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[TransitionRunEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionRunEvent.html) | Sent when a transition is created. |  | Yes |   
[TransitionStartEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionStartEvent.html) | Sent when a transition’s delay phase ends and the transition starts. |  | Yes |   
[TransitionEndEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionEndEvent.html) | Sent when a transition ends. |  | Yes |   
[TransitionCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionCancelEvent.html) | Sent when an a transition is canceled. |  | Yes |   
## Behavior
Each transition property has its own lifecycle and its own transition events. You can access the current property with an event’s `stylePropertyNames` property.
If a shorthand USS property is changed, every component also gets its own lifecycle. For example, if you change `margin`, `margin-left`, `margin-right`, `margin-top` and `margin-bottom`, they all get their own `TransitionRunEvent`, `TransitionStartEvent` and `TransitionEndEvent`, for a total of 12 separate events.
If you set `transition-delay` to `0`, the `TransitionRunEvent` and `TransitionStartEvent` are sent one after the other within a few milliseconds.
If you set `transition-delay` to a value below `0`, the transition won’t start at the beginning. For example, with a `transition-delay` of `-3` seconds and `transition-duration` of `5` seconds, the `TransitionRunEvent` and `TransitionStartEvent` is sent with an `elapsedTime` property set to `3` seconds and the transition effectively starts at the third second of a five-second animation.
## Event list
This section describes the `target`, `stylePropertyNames`, and `elapsedTime` of each transition event.
### TransitionRunEvent
A `TransitionRunEvent` event is sent when a transition is created.
  * **`target`**: The element that executes the transition.
  * **`stylePropertyNames`**: The list of properties modified by the transition.
  * **`elapsedTime`**: The time since the start of the transition.


### TransitionStartEvent
A `TransitionStartEvent` event is sent when the transition’s delay phase ends and the transition begins.
  * **`target`**: The element that executes the transition.
  * **`stylePropertyNames`**: The list of properties modified by the transition.
  * **`elapsedTime`**: The time since the start of the transition.


### TransitionEndEvent
A `TransitionEndEvent` event is sent when a transition ends.
  * **`target`**: The element that executes the transition.
  * **`stylePropertyNames`**: The list of properties modified by the transition.
  * **`elapsedTime`**: The time since the start of the transition.


**Note** : `TransitionEndEvent` might not fire if there’s no previous style state to transition from, such as when a style is first applied or modified without an initial value. This happens because UI Toolkit skips the transition if it can’t detect a change from a cached value. To work around this, set an initial style value before applying the transition-triggering change, or delay the change using a [`schedule.Execute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.Execute.html).
### TransitionCancelEvent
A `TransitionCancelEvent` event is sent when a transition is interrupted by the property being changed again.
  * **`target`**: The element that executes the transition.
  * **`stylePropertyNames`**: The list of properties modified by the transition.
  * **`elapsedTime`**: The time since the start of the transition.


## Examples
  * [Create a transition event](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-transition-event-example.html): This example demonstrates the lifecycle of a transition event.
  * [Create looping transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-transition-event-loop-example.html): This example demonstrates how to leverage the `TransitionEndEvent` to create transitions that loop.
  * [Create a simple transition with UI Builder and C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-transition-example.html): This example demonstrates how to create simple transitions with the UI Builder and C# script.


## Additional resources
  * [USS transition](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Tooltip-Events.html)
Tooltip event
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-contextual-menus.html)
Contextual menu events
