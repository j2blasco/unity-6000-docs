* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-capture-the-pointer.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * Capture the pointer with a manipulator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html)
Dispatch events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
Handle event callbacks and value changes
# Capture the pointer with a manipulator
When you handle pointer input, you might want the control to capture a pointer. When a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) captures a pointer, Unity sends all the events associated with the pointer to the visual element regardless of whether the pointer hovers over the visual element. For example, if you create a control that receives drag events and captures the pointer, the control still receives drag events regardless of the pointer location.
The [`Manipulator`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator.html) class provides a convenient way to capture the pointer. The `Manipulator` class is a base class for all manipulators. A manipulator is a class that handles pointer input and sends events to a visual element. For example, the [`Clickable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.html) class is a manipulator that sends a [`PointerDownEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html) when the user clicks on a visual element. After a [`PointerDownEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html), some elements must capture the pointer position to ensure it receives all subsequent pointer events, even when the cursor is no longer hovering over the element. For example, when you click on a button, slider, or scroll bar.
To capture the pointer, call [`PointerCaptureHelper.CapturePointer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.CapturePointer.html).
To release the pointer, call [`PointerCaptureHelper.ReleasePointer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.ReleasePointer.html). If another element is already capturing the pointer when you call `CapturePointer()`, the element receives a [`PointerCaptureOutEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureOutEvent.html) event and loses the capture.
Only one element in the application can have the capture at any moment. While an element has the capture, it’s the target of all subsequent pointer events except mouse wheel events. This only applies to pointer events that don’t already have a set target and rely on the dispatch process to determine the target.
For more information, see the [Capture events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Capture-Events.html).
## Additional resources
  * [Capture events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Capture-Events.html)
  * [Create a drag-and-drop UI inside a custom Editor window](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-ui.html)
  * [Manipulators](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-manipulators.html)
  * [Events reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html)
Dispatch events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
Handle event callbacks and value changes
