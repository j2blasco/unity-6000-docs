* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.html

# Clickable
class in UnityEngine.UIElements
/
Inherits from:[UIElements.PointerManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.html)
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
Manipulator that tracks Mouse events on an element and callbacks when the elements is clicked. 
### Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable-active.html) |  This property tracks the activation of the manipulator. Set it to true when the manipulator is activated.   
[lastMousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable-lastMousePosition.html) |  Specifies the mouse position saved during the last mouse event on the target Element.   
### Constructors
Constructor | Description  
---|---  
[Clickable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable-ctor.html) |  Constructor.   
### Protected Methods
Method | Description  
---|---  
[Invoke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.Invoke.html) |  Invokes a click action.   
[OnPointerDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.OnPointerDown.html) |  This method is called when a PointerDownEvent is sent to the target element.   
[OnPointerMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.OnPointerMove.html) |  This method is called when a PointerMoveEvent is sent to the target element.   
[OnPointerUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.OnPointerUp.html) |  This method is called when a PointerUpEvent is sent to the target element.   
[ProcessCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.ProcessCancelEvent.html) |  This method processes the up cancel sent to the target Element.   
[ProcessDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.ProcessDownEvent.html) |  This method processes the down event sent to the target Element.   
[ProcessMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.ProcessMoveEvent.html) |  This method processes the move event sent to the target Element.   
[ProcessUpEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.ProcessUpEvent.html) |  This method processes the up event sent to the target Element.   
[RegisterCallbacksOnTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.RegisterCallbacksOnTarget.html) |  Called to register mouse event callbacks on the target element.   
[UnregisterCallbacksFromTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.UnregisterCallbacksFromTarget.html) |  Called to unregister event callbacks from the target element.   
### Events
Event | Description  
---|---  
[clicked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable-clicked.html) |  Callback triggered when the target element is clicked.   
[clickedWithEventInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable-clickedWithEventInfo.html) |  Callback triggered when the target element is clicked, including event data.   
### Inherited Members
### Properties
Property | Description  
---|---  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator-target.html) |  VisualElement being manipulated.   
[activators](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator-activators.html) |  List of Activationfilters.   
### Protected Methods
Method | Description  
---|---  
[CanStartManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.CanStartManipulation.html) |  Checks whether MouseEvent satisfies all of the ManipulatorActivationFilter requirements.   
[CanStopManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.CanStopManipulation.html) |  Checks whether the MouseEvent is related to this Manipulator.   
[CanStartManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.CanStartManipulation.html) |  Checks whether PointerEvent satisfies all of the ManipulatorActivationFilter requirements.   
[CanStopManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.CanStopManipulation.html) |  Checks whether the PointerEvent is related to this Manipulator.   
* * *
