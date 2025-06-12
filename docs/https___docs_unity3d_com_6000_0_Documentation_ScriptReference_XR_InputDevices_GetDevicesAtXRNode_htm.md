* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.GetDevicesAtXRNode.html

#  [InputDevices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.html).GetDevicesAtXRNode
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
public static void GetDevicesAtXRNode([XR.XRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html) node, List<InputDevice> inputDevices); 
### Parameters
Parameter | Description  
---|---  
node | The XRNode that owns the requested device.  
inputDevices | A List of type InputDevices to receive the available input devices.  
### Description
Gets a list of active input devices available to the XR Input Subsystem at a given [XRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html) endpoint.
* * *
