* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.html

# InputDeviceCharacteristics
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
A set of bit flags describing [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html) characteristics.
The XR system combines the **InputDeviceFlags** members into the [InputDevice.characteristics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice-characteristics.html) bitmask to describe the characteristics and capabilities of an input device. You can also pass a bitwise combination of flags from this enumeration to [InputDevices.GetDevicesWithCharacteristics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.GetDevicesWithCharacteristics.html) to get a list of devices with specific characteristics. For example, you could use the following to get the right-hand controller:  
  
`(InputDeviceCharacteristics.HeldInHand | InputDeviceCharacteristics.Right)`.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.None.html) | A default value specifying no flags.  
[HeadMounted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HeadMounted.html) | The InputDevice is attached to the head.  
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Camera.html) | The InputDevice has a camera and associated camera tracking information.  
[HeldInHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HeldInHand.html) | The InputDevice is held in the user's hand. Typically, a tracked controller.  
[HandTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HandTracking.html) | The InputDevice provides hand tracking information via a Hand input feature.  
[EyeTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.EyeTracking.html) | The InputDevice provides eye tracking information via an Eyes input feature.  
[TrackedDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.TrackedDevice.html) | The InputDevice provides 3DOF or 6DOF tracking data.  
[Controller](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Controller.html) | The InputDevice is a game controller.  
[TrackingReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.TrackingReference.html) | The InputDevice is an unmoving reference object used to locate and track other objects in the world.  
[Left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Left.html) | The InputDevice is associated with the left side of the user.  
[Right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Right.html) | The InputDevice is associated with the right side of the user.  
[Simulated6DOF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Simulated6DOF.html) | The InputDevice reports software approximated, positional data.  
* * *
