* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetLastPenContactEvent.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetLastPenContactEvent
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
public static [PenData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html) GetLastPenContactEvent(); 
### Returns
**PenData** Pen event details in the struct. 
### Description
Returns the [PenData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html) for the last stored pen up or down event.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
PenData.type will be set to PenEventType.Ignore if the event has already been processed by UIToolKit. GetPenEvent should be used to retrieve previous pen events.
* * *
