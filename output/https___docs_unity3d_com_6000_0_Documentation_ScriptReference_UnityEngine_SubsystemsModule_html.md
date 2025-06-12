* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.SubsystemsModule.html

# UnityEngine.SubsystemsModule
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
The Subsystem module contains the definitions and runtime support for general subsystems in Unity.
### Classes
Class | Description  
---|---  
[IntegratedSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.html) | An IntegratedSubsystem is initialized from an IntegratedSubsystemDescriptor for a given Subsystem (Example, Input, Environment, Display, etc.) and provides an interface to interact with that given IntegratedSubsystem until it is Destroyed. After an IntegratedSubsystem is created it can be Started or Stopped to turn on and off functionality (and preserve performance). The base type for IntegratedSubsystem only exposes this functionality; this class is designed to be a base class for derived classes that expose more functionality specific to a given IntegratedSubsystem. Note: initializing a second IntegratedSubsystem from the same IntegratedSubsystemDescriptor will return a reference to the existing IntegratedSubsystem as only one IntegratedSubsystem is currently allowed for a single IntegratedSubsystem provider.   
[IntegratedSubsystemDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystemDescriptor.html) | Information about a subsystem that can be queried before creating a subsystem instance.  
[SubsystemDescriptorStore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemDescriptorStore.html) | Registration entry point for subsystems to register their descriptor.  
[SubsystemDescriptorWithProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemDescriptorWithProvider.html) | Information about a SubsystemWithProvider that can be queried before creating a subsystem instance.  
[SubsystemManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.html) | Gives access to subsystems which provide additional functionality through plugins.  
[SubsystemProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemProvider.html) | A provider that supplies data to a subsystem, generally for platform-specific implementations.  
[SubsystemWithProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemWithProvider.html) | A subsystem is initialized from a SubsystemDescriptorWithProvider for a given subsystem (Session, Plane, Face, etc.) and provides an interface to interact with that given subsystem until it is Destroyed. After a subsystem is created, it can be Started or Stopped to turn on and off functionality and preserve performance. The base type for the subsystem only exposes this functionality; this class is designed to be a base class for derived classes that expose more functionality specific to a given subsystem.*Note:* Initializing a second subsystem from the same subsystem descriptor will return a reference to the existing subsystem, because only one subsystem is currently allowed for a single subsystem provider.  
* * *
