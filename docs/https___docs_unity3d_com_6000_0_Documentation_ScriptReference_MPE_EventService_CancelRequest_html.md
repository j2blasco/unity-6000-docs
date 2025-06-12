* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.CancelRequest.html

#  [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html).CancelRequest
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
public static bool CancelRequest(string eventType, string message); 
### Parameters
Parameter | Description  
---|---  
eventType | The event to cancel.  
message | The error message sent to the pending request.  
### Returns
**bool** Returns true if a pending request was found and cancelled false otherwise. 
### Description
Checks whether there is a pending request for a specific event and, if there is, cancels it. See [EventService.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Request.html) for more details on Request.
* * *
