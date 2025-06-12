* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.html

# Options
enumeration
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
Options that define how a progress indicator behaves.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.None.html) | A progress indicator that starts with no other options activated. This is the default.  
[Sticky](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Sticky.html) | A sticky progress indicator displays progress information even after the task is complete. The system does not remove it automatically. You must remove it using a remove operation.  
[Indefinite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Indefinite.html) | An indefinite progress indicator shows that the associated task is in progress, but does not show how close it is to completion.  
[Synchronous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Synchronous.html) | A synchronous progress indicator updates the Editor UI as soon as it reports progress. This is the opposite of the default behavior, which is to report all progress asynchronously.  
[Managed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Managed.html) | Unity manages progress indicators. When a domain reload happens, the system cancels tasks that support cancellation, and removes their progress indicators. This is the default for progress indicators started from C#.  
[Unmanaged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Unmanaged.html) | An unmanaged progress indicator is one that Unity does not manage. Unity does not cancel unmanaged progress indicators when a domain reload happens. This is the default behavior for internal-use progress indicators started from C++ code.  
* * *
