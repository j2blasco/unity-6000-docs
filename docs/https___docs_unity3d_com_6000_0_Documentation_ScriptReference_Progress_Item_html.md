* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html

# Item
class in UnityEditor
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
A data structure that provides information about a progress indicator.
### Properties
Property | Description  
---|---  
[cancellable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-cancellable.html) | Returns true if the progress indicator's associated event can be canceled.  
[currentStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-currentStep.html) | Returns the current step for this progress indicator.  
[description](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-description.html) | Returns the progress indicator's description.  
[elapsedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-elapsedTime.html) | Returns the number of seconds that the progress indicator has been running for.  
[endTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-endTime.html) | Returns the time when the progress indicator ended.  
[exists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-exists.html) | Checks whether the progress indicator exists.  
[finished](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-finished.html) | Returns true if the progress indicator is finished, but not removed.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-id.html) | Returns the progress indicator's unique identifier.  
[indefinite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-indefinite.html) | Returns true if the progress indicator is indefinite.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-name.html) | Returns the progress indicator's name.  
[options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-options.html) | Returns the option flags used to start the progress indicator.  
[parentId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-parentId.html) | Returns the unique ID of the progress indicator's parent, or -1 if the progress indicator is not a child of another progress indicator.  
[pausable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-pausable.html) | Returns true if the progress indicator's task can be paused.  
[paused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-paused.html) | Returns true if the progress indicator is paused.  
[priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-priority.html) | Returns the progress indicator's priority.  
[progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-progress.html) | Returns the progress value of a progress indicator's associated task.  
[remainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-remainingTime.html) | Returns this progress indicator's remaining time to completion.  
[responding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-responding.html) | Returns true if progress is ongoing, false if the progress indicator has not received any progress report for more than 5 seconds.  
[running](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-running.html) | Returns true if the progress indicator is running and active.  
[startTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-startTime.html) | Returns the time when the progress indicator started.  
[status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-status.html) | Returns the progress indicator's status.  
[stepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-stepLabel.html) | Returns the label that displays the progress indicator's steps.  
[timeDisplayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-timeDisplayMode.html) | Returns the progress indicator's time display mode.  
[totalSteps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-totalSteps.html) | Returns the total number of steps, from start to finish, for this progress indicator.  
[updateTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item-updateTime.html) | Returns the last time the progress indicator was updated.  
### Public Methods
Method | Description  
---|---  
[Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.Cancel.html) | Cancels a running progress indicator.  
[ClearRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.ClearRemainingTime.html) | Resets the computation of the progress indicator's remaining time.  
[Finish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.Finish.html) | Marks the progress indicator as finished.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.Pause.html) | Pauses a running progress indicator.  
[RegisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.RegisterCancelCallback.html) | Registers a callback that is called when the user cancels a running progress indicator's associated task.  
[RegisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.RegisterPauseCallback.html) | Registers a callback that is called when a user pauses a running progress indicator's task.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.Remove.html) | Finishes and removes an active progress indicator.  
[Report](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.Report.html) | Reports the progress indicator's current status.  
[Resume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.Resume.html) | Resumes a paused progress indicator.  
[SetDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.SetDescription.html) | Sets the progress indicator's description. To clear the description pass null.  
[SetPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.SetPriority.html) | Sets the progress indicator's priority.  
[SetRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.SetRemainingTime.html) | Sets the progress indicator's remaining time, in seconds.  
[SetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.SetStepLabel.html) | Sets the label that displays the progress indicator's steps.  
[SetTimeDisplayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.SetTimeDisplayMode.html) | Set a progress indicator's time display mode.  
[UnregisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.UnregisterCancelCallback.html) | Unregisters a previously registered progress cancellation callback.  
[UnregisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.UnregisterPauseCallback.html) | Unregisters a previously registered progress pause callback.  
* * *
