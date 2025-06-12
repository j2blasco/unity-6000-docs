* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Subsystem.html

**Method group is Obsolete**   

# Subsystem
class in UnityEngine
/
Implemented in:[UnityEngine.SubsystemsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.SubsystemsModule.html)
Leave feedback
  

Implements interfaces:[ISubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISubsystem.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
**Obsolete** Use SubsystemWithProvider instead.
### Description
A Subsystem is initialized from a [SubsystemDescriptorWithProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemDescriptorWithProvider.html) for a given Subsystem (Example, Input, Display, etc.) and provides an interface to interact with that given Subsystem until it is Destroyed. After a Subsystem is created it can be Started or Stopped to turn on and off functionality (and improve performance). The base type for subsystems only exposes this functionality; this class is designed to be a base class for derived classes that expose more functionality specific to a given Subsystem.  
  
Note: initializing a second Subsystem from the same SubsystemDescriptor will return a reference to the existing Subsystem as only one Subsystem is currently allowed for a single Subsystem provider.  
  
This subsystem base-class is deprecated. If you are creating a new subsystem type, derive from [SubsystemWithProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemWithProvider.html) instead.
* * *
