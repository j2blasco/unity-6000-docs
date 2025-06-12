* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager-pickingChanged.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).pickingChanged
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
The event raised whenever the picking state of a GameObject changes.
For performance reasons, this event is not raised for every picking operation. For example, if you select multiple GameObjects and disable picking on them all at once, the event will be raised only once.
* * *
