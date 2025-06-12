* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events-registeringPackages.html

#  [Events](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events.html).registeringPackages
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
Event raised before applying changes to the registered packages list.
Occurs before the asset database begins refreshing. Packages about to be modified or removed are still present and functional, because the package registration process has not yet begun.   
**Note:** There is no guarantee that the [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html) pipeline will finish by the time this event is raised, so don't rely on the execution order for pre-processing events.
* * *
