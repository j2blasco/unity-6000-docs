* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.html

# PointerManipulator
class in UnityEngine.UIElements
/
Inherits from:[UIElements.MouseManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.html)
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
PointerManipulators have a list of activation filters. 
### Protected Methods
Method | Description  
---|---  
[CanStartManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.CanStartManipulation.html) |  Checks whether PointerEvent satisfies all of the ManipulatorActivationFilter requirements.   
[CanStopManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.CanStopManipulation.html) |  Checks whether the PointerEvent is related to this Manipulator.   
### Inherited Members
### Properties
Property | Description  
---|---  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator-target.html) |  VisualElement being manipulated.   
[activators](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator-activators.html) |  List of Activationfilters.   
### Protected Methods
Method | Description  
---|---  
[RegisterCallbacksOnTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator.RegisterCallbacksOnTarget.html) |  Called to register event callbacks on the target element.   
[UnregisterCallbacksFromTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator.UnregisterCallbacksFromTarget.html) |  Called to unregister event callbacks from the target element.   
[CanStartManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.CanStartManipulation.html) |  Checks whether MouseEvent satisfies all of the ManipulatorActivationFilter requirements.   
[CanStopManipulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.CanStopManipulation.html) |  Checks whether the MouseEvent is related to this Manipulator.   
* * *
