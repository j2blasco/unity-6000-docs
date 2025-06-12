* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISubsystem.html

# ISubsystem
interface in UnityEngine
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
Interface implemented by both Subsystem and [IntegratedSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.html) which provides control over the state of either. 
### Properties
Property | Description  
---|---  
[running](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISubsystem-running.html) | Will be true if asking the subsytem to start was successful. False in the case that the subsystem has stopped, was asked to stop or has not been started yet.  
### Public Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISubsystem.Destroy.html) | Destroys this instance of a subsystem.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISubsystem.Start.html) | Starts an instance of a subsystem.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISubsystem.Stop.html) | Stops an instance of a subsystem.  
* * *
