* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities.html

# HapticCapabilities
struct in UnityEngine.XR
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
Describes the haptic capabilities of the device at an [XRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html) in the XR input subsystem.
### Properties
Property | Description  
---|---  
[bufferFrequencyHz](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities-bufferFrequencyHz.html) | The frequency (in Hz) that this device plays back buffered haptic data.  
[bufferMaxSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities-bufferMaxSize.html) | The maximum amount of data that can be sent to an InputDevice via InputDevice.SendHapticBuffer.  
[bufferOptimalSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities-bufferOptimalSize.html) | The optimal buffer size an InputDevice expects to be sent via InputDevice.SendHapticBuffer in order to provide a continuous rumble between individual frames.  
[numChannels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities-numChannels.html) | The number of channels that this device plays back haptic data.  
[supportsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities-supportsBuffer.html) | True if this device supports sending a haptic buffer.  
[supportsImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities-supportsImpulse.html) | True if this device supports sending a haptic impulse.  
* * *
