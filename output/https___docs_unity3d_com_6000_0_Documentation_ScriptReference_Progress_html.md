* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html

# Progress
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
The Progress utility class reports the progress of asynchronous tasks to Unity.
The Progress utility class can be used to report progress of asynchronous tasks in multiple ways. Here is an example of a task that runs on the [EditorApplication.update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) loop and reports progress:
```
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class ProgressReport_EditorUpdate
{
    static IEnumerator s_CurrentEnumerator;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ProgressReport/EditorUpdate")]
    static void RunEditorUpdate()
    {
        if (s_CurrentEnumerator == null)
        {
            s_CurrentEnumerator = RunTaskWithReport();
        }
        EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) -= RunTaskOnUpdate;
        EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) += RunTaskOnUpdate;
    }  
  
    static void RunTaskOnUpdate()
    {
        if (s_CurrentEnumerator == null)
        {
            return;
        }  
  
        // Execute one step of the task
        var atEnd = !s_CurrentEnumerator.MoveNext();  
  
        // If there is nothing more to do, remove the update callback
        if (atEnd)
        {
            s_CurrentEnumerator = null;
            EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) -= RunTaskOnUpdate;
        }
    }  
  
    static IEnumerator RunTaskWithReport()
    {
        // Create a new progress indicator
        int progressId = Progress.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Start.html)("Running one task");  
  
        // Report the progress status at anytime
        for (int frame = 0; frame <= 1000; ++frame)
        {
            string description;
            if (frame < 250)
                description = "First part of the task";
            else if (frame < 750)
                description = "Second part of the task";
            else
                description = "Last part of the task";
            Progress.Report[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html)(progressId, frame / 1000.0f, description);  
  
            // Do your computation that you want to report progress on
            // ...
            yield return null;
        }  
  
        // The task is finished. Remove the associated progress indicator.
        Progress.Remove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Remove.html)(progressId);
    }
}

```

Here is another example of a task that runs on a separate thread and reports progress:
```
using System.Threading;
using System.Threading.Tasks;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class ProgressReport_Threaded
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ProgressReport/Threaded")]
    static void RunThreaded()
    {
        Task.Run(RunTaskWithReport);
    }  
  
    static void RunTaskWithReport()
    {
        // Create a new progress indicator
        int progressId = Progress.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Start.html)("Running one task");  
  
        // Report the progress status at anytime
        for (int frame = 0; frame <= 1000; ++frame)
        {
            string description;
            if (frame < 250)
                description = "First part of the task";
            else if (frame < 750)
                description = "Second part of the task";
            else
                description = "Last part of the task";
            Progress.Report[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html)(progressId, frame / 1000.0f, description);  
  
            // Do your computation that you want to report progress on
            ComputeSlowStep();
        }  
  
        // The task is finished. Remove the associated progress indicator.
        Progress.Remove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Remove.html)(progressId);
    }  
  
    static void ComputeSlowStep()
    {
        // Simulate a slow computation with a 1 millisecond sleep
        Thread.Sleep(1);
    }
}

```

### Static Properties
Property | Description  
---|---  
[globalProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress-globalProgress.html) | Returns the global average progression of all running tasks.  
[globalRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress-globalRemainingTime.html) | Returns the maximum time remaining for all running progress indicators.  
[running](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress-running.html) | Returns true if there is at least one running progress indicator, false otherwise.  
### Static Methods
Method | Description  
---|---  
[Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Cancel.html) | Cancels a runnning progress indicator, and invokes the cancel callback for the associated task.  
[ClearRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.ClearRemainingTime.html) | Resets the computation of a progress indicator's remaining time.  
[EnumerateItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.EnumerateItems.html) | Returns an enumerator to loop over all progress indicators.  
[Exists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Exists.html) | Checks whether a progress indicator with the specified ID exists.  
[Finish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Finish.html) | Marks the progress indicator as finished.  
[GetCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetCount.html) | Gets the number of available progress indicators.  
[GetCountPerStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetCountPerStatus.html) | For each available status, gets the number of progress indicators with that status.  
[GetCurrentStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetCurrentStep.html) | Gets the current step for a progress indicator.  
[GetDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetDescription.html) | Gets a progress indicator's description.  
[GetEndDateTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetEndDateTime.html) | Gets the timestamp of when the progress indicator ended.  
[GetId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetId.html) | Finds a progress indicator's unique ID using its index in the set of all available progress indicators.  
[GetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetName.html) | Gets a progress indicator's name.  
[GetOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetOptions.html) | Gets the options that you specified when you started the progress indicator.  
[GetParentId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetParentId.html) | Gets the unique ID of the progress indicator's parent, if any.  
[GetPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetPriority.html) | Gets a progress indicator's priority.  
[GetProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetProgress.html) | Gets a progress indicator's progress.  
[GetProgressById](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetProgressById.html) | Gets information about a progress indicator.  
[GetRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetRemainingTime.html) | Gets a progress indicator's remaining time, in seconds.  
[GetRunningProgressCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetRunningProgressCount.html) | Gets the number of active or running progress indicators.  
[GetStartDateTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetStartDateTime.html) | Gets the timestamp of when the progress indicator started.  
[GetStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetStatus.html) | Gets the progress indicator's status.  
[GetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetStepLabel.html) | Gets the label that displays a progress indicator's steps.  
[GetTimeDisplayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetTimeDisplayMode.html) | Get a progress indicator's time display mode.  
[GetTotalSteps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetTotalSteps.html) | Gets the total number of steps, from start to finish, for a progress indicator.  
[GetUpdateDateTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetUpdateDateTime.html) | Gets the time that the progress indicator last changed, or finished.  
[IsCancellable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.IsCancellable.html) | Indicates whether you can cancel the progress indicator's associated task.  
[IsPausable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.IsPausable.html) | Indicates whether you can pause the progress indicator's task.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Pause.html) | Pauses a runnning progress indicator, and invokes the pause callback for its task.  
[RegisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.RegisterCancelCallback.html) | Registers a callback that is called when the user requests to cancel a running progress indicator's associated task.  
[RegisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.RegisterPauseCallback.html) | Registers a callback that is called when the user requests to pause or resume a running progress indicator's task.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Remove.html) | Finishes and removes an active progress indicator.  
[Report](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html) | Reports a running progress indicator's current status.  
[Resume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Resume.html) | Resumes a paused progress indicator, and invokes the pause callback for the associated task.  
[SetDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetDescription.html) | Sets the progress indicator's description. To clear the description pass null.  
[SetPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetPriority.html) | Sets a progress indicator's priority.  
[SetRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetRemainingTime.html) | Sets the progress indicator's remaining time, in seconds.  
[SetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetStepLabel.html) | Sets the label that displays a progress indicator's steps.  
[SetTimeDisplayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetTimeDisplayMode.html) | Set a progress indicator's time display mode.  
[ShowDetails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.ShowDetails.html) | Opens the progress window for background tasks.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Start.html) | This method starts a new progress indicator.  
[UnregisterCancelCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.UnregisterCancelCallback.html) | Unregisters a previously registered progress cancellation callback.  
[UnregisterPauseCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.UnregisterPauseCallback.html) | Unregisters a previously registered progress pause callback.  
### Events
Event | Description  
---|---  
[added](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress-added.html) | An event raised when a new progress indicator starts.  
[removed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress-removed.html) | An event raised when a progress indicator is removed.  
[updated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress-updated.html) | An event raised when a progress indicator's state updates.  
* * *
