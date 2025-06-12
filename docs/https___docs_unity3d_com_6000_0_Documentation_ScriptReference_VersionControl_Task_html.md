* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html

# Task
class in UnityEditor.VersionControl
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
A Task describes an instance of a version control operation.
An object of this type allows you to process operations such as [Provider.Checkout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Checkout.html), [Provider.GetLatest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetLatest.html), and [Provider.Submit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Submit.html). Unity creates this item almost every time you ask [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html) to perform an action. Task objects, that version control operations return, execute in the background and don't always finish immediately, use [Task.Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.Wait.html) if you need to wait for them to finish.
### Properties
Property | Description  
---|---  
[assetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-assetList.html) | The result of some types of tasks.  
[changeSets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-changeSets.html) | List of changesets returned by some tasks.  
[description](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-description.html) | A short description of the current task.  
[messages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-messages.html) | May contain messages from the version control plugins.  
[progressPct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-progressPct.html) | A progress percentage for the current task.  
[resultCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-resultCode.html) | Some task return result codes, these are stored here.  
[secondsSpent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-secondsSpent.html) | Total time spent in task since the task was started.  
[success](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-success.html) | Get whether or not the task was completed succesfully.  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-text.html) | Will contain the result of the Provider.ChangeSetDescription task.  
### Public Methods
Method | Description  
---|---  
[SetCompletionAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.SetCompletionAction.html) | Upon completion of a task a completion task will be performed if it is set.  
[Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.Wait.html) | A blocking wait for the task to complete.  
* * *
