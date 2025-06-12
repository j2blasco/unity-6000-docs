* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.html

# TrackingOriginModeFlags
enumeration
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
This enum provides context to where the 0,0,0 point of tracking for [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html)s is.
Each [XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html) has a single origin for all reported [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html)s. The origin can be relative to either real-world objects, such as a physical tracking device, or virtual objects, such as the center of a user-drawn bounding region.
### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Unknown.html) | TrackingOriginModeFlags.Unknown enumerates when the XRInputSubsystem was not able to set its tracking origin or has no tracking.  
[Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Device.html) |  XRInputSubsystem tracks all InputDevices in reference to the first known location of a specific InputDevice when set to TrackingOriginModeFlags.Device.  
[Floor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Floor.html) |  XRInputSubsystem tracks all InputDevices in reference to a point on the floor when set to TrackingOriginModeFlags.Floor.  
[TrackingReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.TrackingReference.html) |  XRInputSubsystem tracks all InputDevices in reference to an InputDevice with the InputDeviceCharacteristics.TrackingReference flag set when set to TrackingOriginModeFlags.TrackingReference.  
[Unbounded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Unbounded.html) |  XRInputSubsystem tracks all InputDevices in relation to a world anchor. This world anchor can change at any time, and is chosen by the runtime.  
* * *
