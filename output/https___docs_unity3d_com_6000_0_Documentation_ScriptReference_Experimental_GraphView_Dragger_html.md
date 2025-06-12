* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# Dragger
class in UnityEditor.Experimental.GraphView
/
Inherits from:[UIElements.MouseManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.html)
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
Base manipulator for mouse-dragging elements.
### Properties
Property | Description  
---|---  
[clampToParentEdges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger-clampToParentEdges.html) | If true, it does not allow the dragged element to exit the parent's edges.  
[panSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger-panSpeed.html) | When elements are dragged near the edges of the Graph, panning occurs. This controls the speed for said panning.  
### Constructors
Constructor | Description  
---|---  
[Dragger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger-ctor.html) | Dragger constructor.  
### Protected Methods
Method | Description  
---|---  
[CalculatePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.CalculatePosition.html) | Calculate new position of the dragged element.  
[OnMouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.OnMouseDown.html) | Called on mouse down event.  
[OnMouseMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.OnMouseMove.html) | Called on mouse move event.  
[OnMouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.OnMouseUp.html) | Called on mouse up event.  
[RegisterCallbacksOnTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.RegisterCallbacksOnTarget.html) | Called to register click event callbacks on the target element.  
[UnregisterCallbacksFromTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.UnregisterCallbacksFromTarget.html) | Called to unregister event callbacks from the target element.  
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
* * *
