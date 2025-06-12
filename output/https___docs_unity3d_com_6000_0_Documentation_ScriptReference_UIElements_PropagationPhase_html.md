* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropagationPhase.html

# PropagationPhase
enumeration
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
The propagation phases of an event. 
When an element receives an event, the event propagates from the panel's root element to the target element.  
  
In the TrickleDown phase, the event is sent from the panel's root element to the target element.  
  
In the BubbleUp phase, the event is sent from the target element back to the panel's root element. 
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropagationPhase.None.html) |  The event is not propagated.   
[TrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropagationPhase.TrickleDown.html) |  The event is sent from the panel's root element to the target element.   
[BubbleUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropagationPhase.BubbleUp.html) |  The event is sent from the target element back to the panel's root element.   
* * *
