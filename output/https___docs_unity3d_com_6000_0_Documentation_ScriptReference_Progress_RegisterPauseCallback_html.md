* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.RegisterPauseCallback.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).RegisterPauseCallback
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
public static void RegisterPauseCallback(int id, Func<bool,bool> callback); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
callback | This function is called when a request to pause or resume the progress indicator's task is made. It takes a boolean parameter that specifies whether the task needs to pause or resume. When the value is true, the task needs to pause. When the value is false, the task needs to resume. The function returns true if it actually performed the requested action.  
### Description
Registers a callback that is called when the user requests to pause or resume a running progress indicator's task.
Additional resources: [Progress.Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Pause.html), [Progress.Resume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Resume.html), [Progress.UnregisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.UnregisterPauseCallback.html).
* * *
