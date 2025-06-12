* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.IsRequestPending.html

#  [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html).IsRequestPending
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
public static bool IsRequestPending(string eventType); 
### Parameters
Parameter | Description  
---|---  
eventType | Event type name.  
### Returns
**bool** True if there is a pending request for this event. False otherwise. 
### Description
Checks whether a request is pending on a specific event. For more information about Request, see [EventService.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Request.html).
* * *
