* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events-registeredPackages.html

#  [Events](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events.html).registeredPackages
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html "Go to PackageManager Component in the Manual")
### Parameters
Parameter | Description  
---|---  
value | A [PackageRegistrationEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageRegistrationEventArgs.html) structure describing the modifications to the registered packages list.  
### Description
Event raised after applying changes to the registered packages list.
Occurs after the asset database is done refreshing, which is after scripts are compiled and the Domain reloaded (if necessary). When you add, update, or remove a package that contains code, a [Domain Reload](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) occurs, which resets registered event handlers. To ensure that your event handler is called, use [InitializeOnLoadAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html) or [InitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadMethodAttribute.html) to register the event handler after the Domain Reload occurs but before the event is raised.   
**Note:** There is no guarantee that the [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html) will finish by the time this event is raised, so don't rely on the execution order for post-processing events.
* * *
