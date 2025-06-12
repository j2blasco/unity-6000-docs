* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-projectChanged.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).projectChanged
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
Event that is raised whenever the state of the project changes.
Actions that trigger this event include creating, renaming, or reparenting assets, as well as moving or renaming folders in the project. Note that the event is not raised immediately in response to these actions, but rather during the next update of the editor application.  
  
Actions taken with assets that have [HideFlags.HideInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html) set will not cause this event to be raised.  
  
Additional resources: [EditorWindow.OnProjectChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnProjectChange.html).
* * *
