* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices-deviceDisconnected.html

#  [InputDevices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.html).deviceDisconnected
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
### Parameters
Parameter | Description  
---|---  
value | The [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html) that just disconnected.  
### Description
Defines the delegate to use to register events when an [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html) is disconnected.
This delegate allows you to receive device disconnection events, so you know when the list of devices changes.  
  
**Note** : InputDevice.IsValid will be false for the passed-in device, and the only device data available will be [InputDevice.name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice-name.html), InputDevice.role, and comparison against other InputDevice objects.
* * *
