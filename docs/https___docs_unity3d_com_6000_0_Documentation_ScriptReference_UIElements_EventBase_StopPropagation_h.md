* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.StopPropagation.html

#  [EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html).StopPropagation
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
public void StopPropagation(); 
### Description
Stops propagating this event. The event is not sent to other elements along the propagation path. This method does not prevent other event handlers from executing on the current target. If this method is called during the TrickleDown propagation phase, it will prevent default actions to be processed, such as an element getting focused as a result of a PointerDownEvent. 
* * *
