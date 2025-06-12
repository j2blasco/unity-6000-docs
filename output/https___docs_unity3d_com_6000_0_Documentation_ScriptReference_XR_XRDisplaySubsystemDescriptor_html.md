* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor.html

# XRDisplaySubsystemDescriptor
class in UnityEngine.XR
/
Inherits from:[IntegratedSubsystemDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystemDescriptor.html)
/
Implemented in:[UnityEngine.XRModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html)
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
Class providing information about [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html) registration.
### Properties
Property | Description  
---|---  
[disablesLegacyVr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor-disablesLegacyVr.html) | Indicates whether legacy VR settings must be disabled for the subsystem. Set to true if the Editor must disable the legacy VR settings disabled; otherwise false.  
[enableBackBufferMSAA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor-enableBackBufferMSAA.html) | Indicates whether MSAA must be resolved in the back buffer. Set to true if MSAA needs to be resolved in the back buffer; otherwise false.  
### Public Methods
Method | Description  
---|---  
[GetAvailableMirrorBlitModeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor.GetAvailableMirrorBlitModeCount.html) | Get current display subsystem's total number of supported mirror blit modes.  
[GetMirrorBlitModeByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor.GetMirrorBlitModeByIndex.html) | Get a supported mirror view blit mode from the current display subsystem descriptor.  
### Inherited Members
### Properties
Property | Description  
---|---  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystemDescriptor-id.html) | A unique string that identifies the subsystem that this Descriptor can create.  
* * *
