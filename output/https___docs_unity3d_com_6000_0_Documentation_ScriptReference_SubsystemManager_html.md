* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.html

# SubsystemManager
class in UnityEngine
/
Implemented in:[UnityEngine.SubsystemsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.SubsystemsModule.html)
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
Gives access to subsystems which provide additional functionality through plugins.
Provides the ability to query for SubsystemDescriptors which enumerate features. Given an SubsystemDescriptor, you can create an Subsystem to utilize the subsystem.
### Static Methods
Method | Description  
---|---  
[GetAllSubsystemDescriptors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.GetAllSubsystemDescriptors.html) | Gets all of the currently known subsystem descriptors regardless of specific subsystem type.  
[GetSubsystemDescriptors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.GetSubsystemDescriptors.html) | Returns a list of SubsystemDescriptors which describe additional functionality that can be enabled.  
[GetSubsystems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.GetSubsystems.html) | Returns active Subsystems of a specific instance type.  
### Events
Event | Description  
---|---  
[afterReloadSubsystems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager-afterReloadSubsystems.html) | Called from SubsystemManager when it has completed reloading all XR SDK Provider packaged subsystems.  
[beforeReloadSubsystems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager-beforeReloadSubsystems.html) | Called from SubsystemManager before reloading all XR SDK Provider packaged subsystems.  
[reloadSubsytemsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager-reloadSubsytemsCompleted.html) | Called from SubsystemManager when it has completed reloading all XR SDK Provider packaged subsystems.  
[reloadSubsytemsStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager-reloadSubsytemsStarted.html) | Called from SubsystemManager before reloading all XR SDK Provider packaged subsystems.  
* * *
