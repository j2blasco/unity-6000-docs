* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Cancel.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).Cancel
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
public static bool Cancel(int id); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
### Returns
**bool** True if the associated task is cancelled, false if it cannot be cancelled. 
### Description
Cancels a runnning progress indicator, and invokes the cancel callback for the associated task.
You can only call this method if a cancel callback has been registered for the specified **id**.  
Additional resources: [Progress.RegisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.RegisterCancelCallback.html), [Progress.UnregisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.UnregisterCancelCallback.html).
* * *
