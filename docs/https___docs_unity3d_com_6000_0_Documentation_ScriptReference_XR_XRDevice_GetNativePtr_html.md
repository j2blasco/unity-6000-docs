* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDevice.GetNativePtr.html

#  [XRDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDevice.html).GetNativePtr
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
public static IntPtr GetNativePtr(); 
### Returns
**IntPtr** The native pointer to the XR device. 
### Description
This method returns an IntPtr representing the native pointer to the XR device if one is available, otherwise the value will be IntPtr.Zero.
This native pointer can be used along with other plugins or extensions to access additional details or functionality related to the XR device.
* * *
