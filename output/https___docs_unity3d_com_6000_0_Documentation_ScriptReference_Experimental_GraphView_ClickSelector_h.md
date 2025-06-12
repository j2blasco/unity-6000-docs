* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ClickSelector.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# ClickSelector
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
Selects element on single click.
### Constructors
Constructor | Description  
---|---  
[ClickSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ClickSelector-ctor.html) | Constructor for ClickSelector.  
### Protected Methods
Method | Description  
---|---  
[OnMouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ClickSelector.OnMouseDown.html) | Called on mouse down event.  
[RegisterCallbacksOnTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ClickSelector.RegisterCallbacksOnTarget.html) | Called to register click event callbacks on the target element.  
[UnregisterCallbacksFromTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ClickSelector.UnregisterCallbacksFromTarget.html) | Called to unregister event callbacks from the target element.  
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
