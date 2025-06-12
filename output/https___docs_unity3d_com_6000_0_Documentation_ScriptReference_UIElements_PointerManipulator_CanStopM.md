* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.CanStopManipulation.html

#  [PointerManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.html).CanStopManipulation
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
## Declaration
protected bool CanStopManipulation([UIElements.IPointerEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html) e); 
### Parameters
Parameter | Description  
---|---  
e | PointerEvent to validate.  
### Returns
**bool** True if PointerEvent uses the current activator button. False otherwise. 
### Description
Checks whether the PointerEvent is related to this Manipulator. 
* * *
