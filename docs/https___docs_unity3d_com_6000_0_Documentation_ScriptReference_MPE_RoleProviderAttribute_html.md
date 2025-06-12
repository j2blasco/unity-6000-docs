* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute.html

# RoleProviderAttribute
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
An attribute used to decorate function that defines how a slave process can interact with a main instance of Unity.
### Properties
Property | Description  
---|---  
[eventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute-eventType.html) | The event that the process triggered.  
[level](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute-level.html) | The process level (either master or slave) that the handler is registered on.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute-name.html) | The name of the RoleProvider. For example, StandaloneProfiler.  
### Constructors
Constructor | Description  
---|---  
[RoleProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute-ctor.html) | Constructor for a RoleProviderAttribute. Allows you to register a handler that is triggered when a specific ProcessEvent is triggered in a UnityEditor process of a specific ProcessLevel.  
* * *
