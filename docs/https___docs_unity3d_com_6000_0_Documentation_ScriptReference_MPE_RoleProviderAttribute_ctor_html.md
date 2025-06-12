* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute-ctor.html

# RoleProviderAttribute Constructor
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
## Declaration
public RoleProviderAttribute(string name, [MPE.ProcessEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html) eventType); 
## Declaration
public RoleProviderAttribute([MPE.ProcessLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessLevel.html) level, [MPE.ProcessEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html) eventType); 
### Parameters
Parameter | Description  
---|---  
name | The name of the RoleProvider. For example, StandaloneProfiler.  
eventType | The event that the process triggered.  
level | The process level (either master or slave) that this handler should be registered on.  
### Description
Constructor for a RoleProviderAttribute. Allows you to register a handler that is triggered when a specific [ProcessEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html) is triggered in a UnityEditor process of a specific [ProcessLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessLevel.html).
* * *
