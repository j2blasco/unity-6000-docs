* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusRing.html

# VisualElementFocusRing
class in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
Leave feedback
  

Implements interfaces:[IFocusRing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IFocusRing.html)
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
Implementation of a linear focus ring. Elements are sorted according to their focusIndex. 
### Properties
Property | Description  
---|---  
[defaultFocusOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusRing-defaultFocusOrder.html) |  The focus order for elements having 0 has a focusIndex.   
### Constructors
Constructor | Description  
---|---  
[VisualElementFocusRing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusRing-ctor.html) |  Constructor.   
### Public Methods
Method | Description  
---|---  
[GetFocusChangeDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusRing.GetFocusChangeDirection.html) |  Get the direction of the focus change for the given event. For example, when the Tab key is pressed, focus should be given to the element to the right in the focus ring.   
[GetNextFocusable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusRing.GetNextFocusable.html) |  Get the next element in the given direction.   
* * *
