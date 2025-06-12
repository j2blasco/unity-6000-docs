* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * Handle event callbacks and value changes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-capture-the-pointer.html)
Capture the pointer with a manipulator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-focus-order.html)
Focus order of elements
# Handle event callbacks and value changes
Events in UI Toolkit are similar to [HTML events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events). When an event occurs, UI Toolkit sends it to the target **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) and all elements within the propagation path in the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree).
The event handling sequence is as follows:
  1. Execute event callbacks on elements from the root element down to the event target. This is the **trickle-down** phase of the dispatch process.
  2. Execute event callbacks on elements from the event target up to the root. This is the **bubble-up phase** of the dispatch process.


As an event moves along the propagation path, the `Event.currentTarget` property updates to the element currently handling the event. Within an event callback function:
  * `Event.currentTarget` is the visual element that the callback registers on.
  * `Event.target` is the visual element where the original event occurs.


For more information, see [Dispatching events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html).
## Register an event callback
You can register an event callback to customize the behavior of an individual instance of an existing class, such as reacting to a mouse click on a text label. To register a callback for an event, use the `RegisterCallback()` method to register the callback directly on the element.
Each element along the propagation path (except the target) can receive an event twice:
  * Once during the trickle-down phase.
  * Once during the bubble-up phase.


By default, a registered callback executes during the target phase and the bubble-up phase. This default behavior ensures that a parent element reacts after its child element.
However, if you want a parent element to react before its child, register your callback with the `TrickleDown.TrickleDown` option like this:
```
using UnityEngine;
using UnityEngine.UIElements;

...
VisualElement myElement = new VisualElement();

// Register a callback for the trickle-down phase.
myElement.RegisterCallback<PointerDownEvent>(MyCallback, TrickleDown.TrickleDown);
...

```

This informs the dispatcher to execute the callback at the target phase and the trickle-down phase.
To add a custom behavior to a specific visual element, register an event callback on that element like this:
```
// Register a callback on a pointer down event
myElement.RegisterCallback<PointerDownEvent>(MyCallback);

```

The signature for the callback function looks like this:
```
void MyCallback(PointerDownEvent evt) { /* ... */ }

```

For an element whose child elements handle the event, to register a callback, use the `Q()` method to find the child element and register the callback on it.
The following example registers a callback on a slider’s drag container element to handle the pointer up event for the slider. In this case, you must register the callback on the drag container element instead of the slider itself because the drag container captures the pointer during pointer down events, which makes it the only receiver for the next pointer up event.
```
var dragContainer = slider.Q("unity-drag-container");
dragContainer.RegisterCallback<PointerUpEvent> ( evt => Debug.Log("PointerUpEvent"));

```

**Note** : You can register multiple callbacks for an event. However, you can only register the same callback function on the same event and propagation phase once.
To remove a callback from a `VisualElement`, call the `myElement.UnregisterCallback()` method.
For information on how to get access to a visual element from a MonoBehaviour, refer to [Get started with runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-runtime-ui.html).
## Send custom data to an event callback
You can send custom data along with the callback to an event. To attach custom data, you must extend the call to register the callback.
The following example registers a callback for `PointerDownEvent` and sends custom data to the callback function:
```
// Send user data along to the callback
myElement.RegisterCallback<PointerDownEvent, MyType>(MyCallbackWithData, myData);

```

The signature for the callback function looks like this:
```
void MyCallbackWithData(PointerDownEvent evt, MyType data) { /* ... */ }

```

## Manage the value of a control
UI controls use the `value` property to hold data for their internal state. For example:
  * A `Toggle` holds a Boolean value that changes when the `Toggle` is turned on or off.
  * An `IntegerField` holds an integer that holds the field’s value.


To get the value of a control:
  * Get the value from the control directly: `int val = myIntegerField.value;`.
  * Listen to a `ChangeEvent` sent by the control and process the change when it happens. You must register your callback to the event like this:
```
//RegisterValueChangedCallback is a shortcut for RegisterCallback<ChangeEvent>.
//It constrains the right type of T for any VisualElement that implements an
//INotifyValueChange interface.
myIntegerField.RegisterValueChangedCallback(OnIntegerFieldChange);

```

The signature for the callback function looks like this:
```
void OnIntegerFieldChange(ChangeEvent<int> evt) { /* ... */ }

```



To change the value of a control:
  * Directly change the `value` variable: `myControl.value = myNewValue;`. This triggers a new `ChangeEvent`.
  * Use `myControl.SetValueWithoutNotify(myNewValue);`. This doesn’t trigger a new `ChangeEvent`.


For more information, see [Change events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Change-Events.html)
## Additional resources
  * [Synthesize and send events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Synthesizing.html)
  * [Events reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)
  * [Manipulators](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-manipulators.html)
  * [Change events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Change-Events.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-capture-the-pointer.html)
Capture the pointer with a manipulator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-focus-order.html)
Focus order of elements
