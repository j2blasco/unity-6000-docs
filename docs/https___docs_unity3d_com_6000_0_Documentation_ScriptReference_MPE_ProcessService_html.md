* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.html

# ProcessService
class in UnityEditor.MPE
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
*This is an experimental feature.* The ProcessService allows you to start slave instance of UnityEditor, opened to the same Project as the master instance, with a specific [RoleProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute.html).
The Standalone Profiler workflow uses this technology.
### Static Properties
Property | Description  
---|---  
[level](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService-level.html) | The ProcessLevel of the running instance of UnityEditor.  
[roleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService-roleName.html) | The role name of the running UnityEditor process. For more information about how to register handlers for a specific process role, see RoleProviderAttribute. For a UnityEditor process of ProcessLevel Master, the roleName is always empty.  
### Static Methods
Method | Description  
---|---  
[DisableProfileConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.DisableProfileConnection.html) | Closes the Profiler connection.  
[EnableProfileConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.EnableProfileConnection.html) | Enables a connection to the Profiler. The standalone Profiler uses this method.  
[GetProcessState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.GetProcessState.html) | Gets the ProcessState of a given instance of UnityEditor.  
[HasCapability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.HasCapability.html) | Checks whether the current process has a given capability.  
[IsChannelServiceStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.IsChannelServiceStarted.html) | Checks whether the ChannelService is already started.  
[Launch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.Launch.html) | Launches a secondary instance of UnityEditor on the same project as the master instance.  
[ReadParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.ReadParameter.html) | A utility function to read command line arguments passed to the current process.  
[Terminate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.Terminate.html) | Terminates an editor process.  
### Events
Event | Description  
---|---  
[ProcessExitedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.ProcessExitedEvent.html) | An event triggered in a master instance of UnityEditor when you start a slave instance with ProcessService.Launch exit.  
[SlaveProcessExitedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.SlaveProcessExitedEvent.html) | An event triggered in a master instance of UnityEditor when you start a slave instance with ProcessService.LaunchSlave exit.  
* * *
