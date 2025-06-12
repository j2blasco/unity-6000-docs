* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.html

# Priority
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
An enumeration that defines task priorities.
Progress indicators are sorted by priority, from highest to lowest. Priorities also determine the visual behavior of progress indicators. Each item in this enumeration defines the threshold value for each priority level. For example, [Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Low.html) is 2 and [Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Normal.html) is 6, so values between 2 and 5 are [Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Low.html) priorities.
### Properties
Property | Description  
---|---  
[Unresponsive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Unresponsive.html) | An unresponsive task is always shown as unresponsive.  
[Idle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Idle.html) | An idle priority task cannot be unresponsive, and is not displayed in the global progress bar.  
[Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Low.html) | A low priority task cannot be unresponsive, but is displayed in the global progress bar.  
[Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.Normal.html) | A normal priority task can be unresponsive, and is displayed in the global progress bar.  
[High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Priority.High.html) | A high priority task can be unresponsive, and is displayed in the global progress bar.  
* * *
