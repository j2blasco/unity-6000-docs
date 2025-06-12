* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Pause.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).Pause
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
public static bool Pause(int id); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
### Returns
**bool** True if the task is paused, false if it cannot be paused. 
### Description
Pauses a runnning progress indicator, and invokes the pause callback for its task.
You can only call this method if a pause callback has been registered for the specified **id**.  
Additional resources: [Progress.RegisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.RegisterPauseCallback.html), [Progress.UnregisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.UnregisterPauseCallback.html), [Progress.Resume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Resume.html).
* * *
