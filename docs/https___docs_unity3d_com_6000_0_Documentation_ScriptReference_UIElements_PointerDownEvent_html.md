* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html

# PointerDownEvent
class in UnityEngine.UIElements
/
Inherits from:[UIElements.PointerEventBase_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1.html)
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
Sends when a pointer is pressed inside a visual element. 
In a runtime UI, a `PointerDownEvent` is sent each time a user touches the screen or presses a mouse button.   
  
In an Editor UI, a `PointerDownEvent` is sent when a user initially touches the screen or presses a mouse button. However, If the user presses additional mouse buttons (right or middle) without releasing the initial one, the PointerMoveEvents is sent not the `PointerDownEvent`. Releasing all mouse buttons and pressing a mouse button again sends a new `PointerDownEvent`.   
  
A `PointerDownEvent` follows the default pointer [event propagation path](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html). It trickles down, bubbles up, and is cancellable.   
  
Disabled elements don't receive this event.   
  
For information about how the `PointerDownEvent` relates to other pointer events, refer to [PointerEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1.html) and [Pointer events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Pointer-Events.html).   
  
Additional resources: [PointerMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html), [PointerUpEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerUpEvent.html), [PointerCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCancelEvent.html)   
  

```
 // This example creates a ClickDetector class to detect a click sequence.
 
 namespace UnityEngine.UIElements
 {
     public class ClickDetector : VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
     {
         public ClickDetector()
         {
             RegisterCallback<PointerDownEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html)>(ProcessEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html));
             RegisterCallback<PointerMoveEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html)>(ProcessEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html));
             RegisterCallback<PointerUpEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerUpEvent.html)>(ProcessEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html));
         }
         private void ProcessEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html)<TEvent>(PointerEventBase<TEvent> evt)
             where TEvent : PointerEventBase<TEvent>, new()
         {
             if (evt.eventTypeId == PointerDownEvent.TypeId() && evt.button == 0)
             {
                 StartClickTracking(evt);
             }
             else if (evt.eventTypeId == PointerMoveEvent.TypeId())
             {
                 // Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) 1 was pressed while another button was already pressed.
                 if (evt.button == 0 && (evt.pressedButtons & 1) == 1)
                 {
                     StartClickTracking(evt);
                 }
                 // Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) 1 is released while another button is still pressed.
                 else if (evt.button == 0 && (evt.pressedButtons & 1) == 0)
                 {
                     SendClickEvent(evt);
                 }
                 // Pointer movement detected or button state changed.
                 else
                 {
                     UpdateClickStatus(evt);
                 }
             }
             else if (evt.eventTypeId == PointerUpEvent.TypeId() && evt.button == 0)
             {
                 SendClickEvent(evt);
             }
         }  
  
         private void StartClickTracking(IPointerEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html) evt) { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Starting click sequence"); }
         private void UpdateClickStatus(IPointerEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html) evt) { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Tracking"); }
         private void SendClickEvent(IPointerEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html) evt) { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Completed click"); }
     }
 }

```

### Constructors
Constructor | Description  
---|---  
[PointerDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent-ctor.html) |  Constructor. Avoid creating new event instances. Instead, use GetPooled() to get an instance from a pool of reusable event instances.   
### Protected Methods
Method | Description  
---|---  
[Init](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.Init.html) |  Resets the event members to their initial values.   
### Inherited Members
### Properties
Property | Description  
---|---  
[bubbles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-bubbles.html) |  Returns whether this event type bubbles up in the event propagation path.   
[dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-dispatch.html) |  Indicates whether the event is being dispatched to a visual element. An event cannot be redispatched while it being dispatched. If you need to recursively dispatch an event, it is recommended that you use a copy of the event.   
[imguiEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-imguiEvent.html) |  The IMGUIEvent at the source of this event. The source can be null since not all events are generated by IMGUI.   
[isImmediatePropagationStopped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-isImmediatePropagationStopped.html) |  Indicates whether StopImmediatePropagation() was called for this event.   
[isPropagationStopped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-isPropagationStopped.html) |  Whether StopPropagation() was called for this event.   
[originalMousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-originalMousePosition.html) |  The original mouse position of the IMGUI event, before it is transformed to the current target local coordinates.   
[pooled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-pooled.html) |  Whether the event is allocated from a pool of events.   
[propagationPhase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-propagationPhase.html) |  The current propagation phase for this event.   
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-target.html) |  The target visual element that received this event. Unlike currentTarget, this target does not change when the event is sent to other elements along the propagation path.   
[timestamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-timestamp.html) |  The time when the event was created, in milliseconds.   
[tricklesDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase-tricklesDown.html) |  Returns whether this event is sent down the event propagation path during the TrickleDown phase.   
[eventTypeId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase_1-eventTypeId.html) |  Retrieves the type ID for this event instance.   
[actionKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-actionKey.html) |  Gets a boolean value that indicates whether the platform-specific action key is pressed. True means the action key is pressed. False means it isn't.   
[altitudeAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-altitudeAngle.html) |  Gets the angle of the stylus relative to the surface, in radians   
[altKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-altKey.html) |  Gets a boolean value that indicates whether the Alt key is pressed. True means the Alt key is pressed. False means it isn't.   
[azimuthAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-azimuthAngle.html) |  Gets the angle of the stylus relative to the x-axis, in radians.   
[button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-button.html) |  Gets a value that indicates which mouse button was pressed or released (if any) to cause this event: 0 is the left button, 1 is the right button, 2 is the middle button. A negative value indicates that no mouse button changed state during this event.   
[clickCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-clickCount.html) |  Gets the number of times the button was pressed.   
[commandKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-commandKey.html) |  Gets a boolean value that indicates whether the Windows/Cmd key is pressed. True means the Windows/Cmd key is pressed. False means it isn't.   
[ctrlKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-ctrlKey.html) |  Gets a boolean value that indicates whether the Ctrl key is pressed. True means the Ctrl key is pressed. False means it isn't.   
[currentTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-currentTarget.html) |  Gets the current target of the event.   
[deltaPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-deltaPosition.html) |  Gets the difference between the pointer's position during the previous mouse event and its position during the current mouse event.   
[deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-deltaTime.html) |  Gets the amount of time that has elapsed since the last recorded change in pointer values, in seconds.   
[isPrimary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-isPrimary.html) |  Gets a boolean value that indicates whether the pointer is a primary pointer. True means the pointer is a primary pointer. False means it isn't.   
[localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-localPosition.html) |  Gets the pointer position in the current target's coordinate system.   
[modifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-modifiers.html) |  Gets flags that indicate whether modifier keys (Alt, Ctrl, Shift, Windows/Cmd) are pressed.   
[penStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-penStatus.html) |  Specifies the state of the pen. For example, whether the pen is in contact with the screen or tablet, whether the pen is inverted, and whether buttons are pressed. On macOS, penStatus will not reflect changes to button mappings.   
[pointerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-pointerId.html) |  Gets the identifier of the pointer that sent the event.   
[pointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-pointerType.html) |  Gets the type of pointer that created the event.   
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-position.html) |  Gets the pointer position in the Screen or World coordinate system.   
[pressedButtons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-pressedButtons.html) |  Gets a bitmask that describes the buttons that are currently pressed.   
[pressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-pressure.html) |  Gets the amount of pressure currently applied by a touch.   
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-radius.html) |  Gets an estimate of the radius of a touch.   
[radiusVariance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-radiusVariance.html) |  Gets the accuracy of the touch radius.   
[shiftKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-shiftKey.html) |  Gets a boolean value that indicates whether the Shift key is pressed. True means the Shift key is pressed. False means it isn't.   
[tangentialPressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-tangentialPressure.html) |  Gets the pressure applied to an additional pressure-sensitive control on the stylus.   
[tilt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-tilt.html) |  Specifies the angle of the pen relative to the X and Y axis respectively, in radians.   
[twist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1-twist.html) |  Gets the rotation of the stylus around its axis, in radians.   
### Public Methods
Method | Description  
---|---  
[StopImmediatePropagation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.StopImmediatePropagation.html) |  Immediately stops the propagation of the event. The event isn't sent to other elements along the propagation path. This method prevents other event handlers from executing on the current target.   
[StopPropagation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.StopPropagation.html) |  Stops propagating this event. The event is not sent to other elements along the propagation path. This method does not prevent other event handlers from executing on the current target. If this method is called during the TrickleDown propagation phase, it will prevent default actions to be processed, such as an element getting focused as a result of a PointerDownEvent.   
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase_1.Dispose.html) |  Implementation of IDispose.   
### Protected Methods
Method | Description  
---|---  
[PostDispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.PostDispatch.html) |  Allows subclasses to perform custom logic after the event has been dispatched.   
[PreDispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.PreDispatch.html) |  Allows subclasses to perform custom logic before the event is dispatched.   
### Static Methods
Method | Description  
---|---  
[RegisterEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.RegisterEventType.html) |  Registers an event class to the event type system.   
[GetPooled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase_1.GetPooled.html) |  Gets an event from the event pool. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use Dispose() to release them.   
[TypeId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase_1.TypeId.html) |  Retrieves the type ID for this event instance.   
[GetPooled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1.GetPooled.html) |  Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use Dispose() to release them.   
* * *
