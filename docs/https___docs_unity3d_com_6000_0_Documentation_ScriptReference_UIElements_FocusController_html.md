* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController.html

# FocusController
class in UnityEngine.UIElements
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
Class in charge of managing the focus inside a Panel. 
Each Panel should have an instance of this class. The instance holds the currently focused VisualElement and is responsible for changing it. 
### Properties
Property | Description  
---|---  
[focusedElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController-focusedElement.html) |  The currently focused VisualElement.   
### Constructors
Constructor | Description  
---|---  
[FocusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController-ctor.html) |  Constructor.   
### Public Methods
Method | Description  
---|---  
[IgnoreEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController.IgnoreEvent.html) |  Instructs the FocusController to ignore the given event. This will prevent the event from changing the current focused VisualElement or triggering focus events.   
* * *
