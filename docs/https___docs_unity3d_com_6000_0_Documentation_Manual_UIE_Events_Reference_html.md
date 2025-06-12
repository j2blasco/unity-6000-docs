* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * Event reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Synthesizing.html)
Synthesize and send events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Capture-Events.html)
Capture events
# Event reference
UI Toolkit raises an event when a user interacts with and changes the state of elements from UI Toolkit. The event design is similar to the [Event interface](https://developer.mozilla.org/en-US/docs/Web/API/Event) for HTML elements.
Event types fit into a hierarchy based on the [EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html) class. Each event family implements an interface that defines the common characteristics of all events of the same family. For example, `BlurEvent` and `FocusEvent` use the [FocusEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusEventBase_1.html) class.
Select any of the event types listed below for more information on the event, its parent class, and links to the API documentation.
Topic | Description  
---|---  
[Capture events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Capture-Events.html) | Events that capture the user’s interaction with the UI.  
[Change events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Change-Events.html) | Events that occur when the user changes the state of an element.  
[Click events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Click-Events.html) | Events that occur when the user clicks an element.  
[Command events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Command-Events.html) | Events that occur when the user invokes a command.  
[Drag and drop events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Drag-Events.html) | Events that occur when the user drags and drops an element.  
[Layout events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Layout-Events.html) | Events that occur when the layout engine changes the layout of an element.  
[Focus events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Focus-Events.html) | Events that occur when the user focuses on an element.  
[Input events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Input-Events.html) | Events that occur when the user inputs text.  
[Keyboard events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Keyboard-Events.html) | Events that occur when the user presses a key.  
[Mouse events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Mouse-Events.html) | Events that occur when the user moves the mouse.  
[Navigation events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Navigation-Events.html) | Events that occur when the user navigates through the UI.  
[Panel events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Panel-Events.html) | Events that occur when the user interacts with a panel.  
[Pointer events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Pointer-Events.html) | Events that occur when the user interacts with a pointer device.  
[Tooltip events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Tooltip-Events.html) | Events that occur when the user interacts with a tooltip.  
[Transition events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transition-Events.html) | Events that inform you of changes to the state of transition.  
[ContextualMenu events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-contextual-menus.html) | Events that occur when the user interacts with a contextual menu.  
[IMGUI events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-IMGUI-Events.html) | Events that occur when the user interacts with an IMGUI element.  
## Additional resources
  * [Dispatch events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html)
  * [Handle events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
  * [Synthesize and send events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Synthesizing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Synthesizing.html)
Synthesize and send events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Capture-Events.html)
Capture events
