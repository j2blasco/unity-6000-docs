* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Drag-Events.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * [Event reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)
  * Drag-and-drop events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Command-Events.html)
Command events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Layout-Events.html)
Layout events
# Drag-and-drop events
Drag events are sent during operations where **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) have drag-and-drop behavior. This is an Editor-only event.
To implement drag-and-drop functionality, make sure that visual elements register callbacks for specific events.
Visual elements that support drag operations separate into two types:
  * Draggable visual elements
  * Droppable visual elements


You can select a draggable visual element, drag it to a droppable visual element, and release the element to drop it.
The base class for all drag-and-drop events is [DragAndDropEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragAndDropEventBase_1.html).
**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[DragExitedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragExitedEvent.html) | Sent when the drag-and-drop process ends. | ✔ | ✔ |   
[DragUpdatedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragUpdatedEvent.html) | Sent when the dragged element moves over a drop target. | ✔ | ✔ | ✔  
[DragPerformEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragPerformEvent.html) | Sent when the dragged element drops onto a target. | ✔ | ✔ | ✔  
[DragEnterEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragEnterEvent.html) | Sent when the dragged element enters a new `VisualElement`. | ✔ |  |   
[DragLeaveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragLeaveEvent.html) | Sent when the dragged element exits the current drop target. | ✔ |  |   
## Make visual elements draggable
To make a visual element draggable, you need to register callbacks on the following three event types:
  * [PointerDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html)
  * [PointerUpEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerUpEvent.html)
  * [PointerMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html)


Use the following steps for a drag operation:
  1. Set its state to “being dragged”.
  2. Add the appropriate data to [`DragAndDrop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).
  3. Call [`DragAndDrop.StartDrag()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.StartDrag.html).
  4. Provide a visual cue to the drag operation. The drop area visual element should remove this feedback when it receives a `DragPerformEvent` or a `DragExitedEvent`.


## Event list
### DragExitedEvent
The [`DragExitedEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragExitedEvent.html) is sent when the user drags any draggable object over a visual element and releases the mouse pointer. When a drop area visual element receives a `DragExitedEvent`, it needs to remove all feedback from drag operations.
### DragUpdatedEvent
The [`DragUpdatedEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragUpdatedEvent.html) is sent when the pointer moves over a visual element as the user moves a draggable object.
When a drop area visual element receives a `DragUpdatedEvent`, it needs to update the drop feedback. For example, you can move the “ghost” of the dragged object so it stays under the mouse pointer.
The drop area visual element should also examine [`DragAndDrop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html) properties and set `DragAndDrop.visualMode` to indicate the effect of a drop operation. For example, a drop operation could create a new object, move an existing object, or reject the drop operation.
### DragPerformEvent
The [`DragPerformEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragPerformEvent.html) is sent when the user drags any draggable object and releases the mouse pointer over a visual element. This only occurs if a visual element sets [`DragAndDrop.visualMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-visualMode.html) to something other than `DragAndDropVisualMode.None` or `DragAndDropVisualMode.Rejected` to indicate that it can accept dragged objects.
When a drop area visual element receives a `DragPerformEvent`, it needs to act on the dragged objects stored in `DragAndDrop.objectReferences`, `DragAndDrop.paths` or `DragAndDrop.GetGenericData()`.
For example, it might add new visual elements at the location where the user drops the objects.
### DragEnterEvent
The [`DragEnterEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragEnterEvent.html) is sent when the pointer enters a visual element during a drag operation.
When a drop area visual element receives a `DragEnterEvent`, it needs to provide feedback that lets the user know that it, or one of its children, is a target for a potential drop operation. For example, you can add a [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html) class to the target element and display a “ghost” of the dragged object under the mouse pointer.
### DragLeaveEvent
The [`DragLeaveEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragLeaveEvent.html) is sent when the pointer exits a visual element as the user moves a draggable object.
When a drop area visual element receives a `DragLeaveEvent`, it needs to stop providing drop feedback. For example, you can remove the USS class that you added when the target element received a `DragEnterEvent`, and no longer display the “ghost” of the dragged object.
## Examples
  * [Create a drag-and-drop UI to drag between Editor windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-drag-across-windows.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Command-Events.html)
Command events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Layout-Events.html)
Layout events
