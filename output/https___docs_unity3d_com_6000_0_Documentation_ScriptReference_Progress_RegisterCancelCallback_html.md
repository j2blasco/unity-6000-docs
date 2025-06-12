* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.RegisterCancelCallback.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).RegisterCancelCallback
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
public static void RegisterCancelCallback(int id, Func<bool> callback); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
callback | The function called when a request to cancel a progress indicator's associated task is made. The function returns true if it actually cancelled the task.  
### Description
Registers a callback that is called when the user requests to cancel a running progress indicator's associated task.
Additional resources: [Progress.Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Cancel.html), [Progress.UnregisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.UnregisterCancelCallback.html).
* * *
