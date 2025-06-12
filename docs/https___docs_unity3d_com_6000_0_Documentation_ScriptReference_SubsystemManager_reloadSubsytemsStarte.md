* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager-reloadSubsytemsStarted.html

#  [SubsystemManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.html).reloadSubsytemsStarted
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
Called from [SubsystemManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.html) before reloading all XR SDK Provider packaged subsystems.
When the Editor starts or when packages are installed or removed, the [SubsystemManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.html) searches the packages and loads all XR SDK packages that it finds. Handling this event allows the user to do work they may need prior to the subsystem manager cleaning up any current subsystem descriptors.  
  
Additional resources: [SubsystemManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.html), SubsystemDescriptor.  
  
*Note:* This is deprecated, use beforeReloadSubsystems instead.
* * *
