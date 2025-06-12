* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Navigation-Events.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * [Event reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Reference.html)
  * Navigation events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Mouse-Events.html)
Mouse events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Panel-Events.html)
Panel events
# Navigation events
Navigation events occur at runtime when the user presses the D-pad, moves a joystick, or presses the `Escape`, `Enter` or arrow keys. They’re an indicator that the user is trying to navigate the UI, but they’re not limited to a specific input device, such as a keyboard. The difference from a [Focus](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Focus-Events.html) event is that the navigation event doesn’t require the focus to move to a new UI element. 
The base class for all navigation events is [NavigationEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationEventBase_1.html).
All navigation events trickle down, bubble up, and are cancellable, but it’s recommended to listen to these events during the bubble-up propagation phase. This is because navigation events are triggered by input events that might also be used to interact with individual controls. For example, a button will react to a press of the `Enter` key with a button click, and it will cancel the `NavigationSubmitEvent`. Listening to these events during the bubble-up phase makes sure that they’re navigation events.
**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html) | Sent when user makes a move input. | ✔ | ✔ | ✔  
[NavigationCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationCancelEvent.html) | Sent when the user makes a cancel input. | ✔ | ✔ | ✔  
[NavigationSubmitEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationSubmitEvent.html) | Sent when the user makes a submit input. | ✔ | ✔ | ✔  
## Event list
### NavigationMoveEvent
The `NavigationMoveEvent` is sent when the user presses the D-pad, moves a joystick, or presses the arrow keys.
Some controls will use the arrow keys for their own functionality. For example, the [ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html) allows the user to select items using the up and down arrow keys. In this case, the control will cancel the `NavigationMoveEvent` and the event won’t enter the bubble-up phase.
**`direction`**: The direction of the navigation. (`None` , `Left`, `Up`, `Right`, `Down`)
**`move`**: The move vector. If the event was triggered by an analog axis input, like a joystick, this property gives access to the directional vector.
### NavigationCancelEvent
The `NavigationCancelEvent` is triggered when the user cancels the current navigation action, such as by pressing the `Escape`` key on the keyboard. It’s important to note that this event doesn’t affect the currently focused element, which means that the UI element that had focus before the cancellation remains selected.
### NavigationSubmitEvent
The `NavigationSubmitEvent` is triggered when the user presses the submit button, such as by pressing the `Enter`` key on the keyboard.
If a control handles the event itself, it cancels the event, preventing it from entering the bubble-up phase. For example, a [TextField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html) that has the focus will stop the `NavigationSubmitEvent` from bubbling up. On the other hand, a focusable [Label](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Label.html) or [Image](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html) will allow the `NavigationSubmitEvent` to bubble up to its parent elements, allowing them to handle the event if needed.
## Example
The following code example shows how to register callbacks for navigation events in a runtime UI:
```
using UnityEngine.UIElements;

public class MyNavigationHandler : MonoBehaviour
{
  void OnEnable()
  {
    // Get a reference to the root visual element
    var uiDocument = GetComponent<UIDocument>();
    var rootVisualElement = uiDocument.rootVisualElement;

    // Register for navigation events
    rootVisualElement.RegisterCallback<NavigationCancelEvent>(OnNavCancelEvent);
    rootVisualElement.RegisterCallback<NavigationMoveEvent>(OnNavMoveEvent);
    rootVisualElement.RegisterCallback<NavigationSubmitEvent>(OnNavSubmitEvent);
  }

  private void OnNavSubmitEvent(NavigationSubmitEvent evt)
  {
    Debug.Log($"OnNavSubmitEvent {evt.propagationPhase}");
  }

  private void OnNavMoveEvent(NavigationMoveEvent evt)
  {
    Debug.Log($"OnNavMoveEvent {evt.propagationPhase} - move {evt.move} - direction {evt.direction}");
  }

  private void OnNavCancelEvent(NavigationCancelEvent evt)
  {
    Debug.Log($"OnNavCancelEvent {evt.propagationPhase}");
  }
}

```

## Additional resources
  * [Dispatch events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html)
  * [Handle events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)
  * [Synthesize and send events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Synthesizing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Mouse-Events.html)
Mouse events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Panel-Events.html)
Panel events
