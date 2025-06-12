* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.html

# WebCamKind
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
Enum representing the different types of web camera device.
On iOS devices, the [WebCamDevice.kind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice-kind.html) is reported directly by the hardware. On Android devices, the hardware does not report this value, so Unity determines the [WebCamDevice.kind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice-kind.html) by calculating the [Equivalent Focal Length](https://en.wikipedia.org/wiki/35_mm_equivalent_focal_length) from a calculation based on the reported focal length and matrix size. Therefore, on some Android devices, the default camera may be detected as [WebCamKind.UltraWideAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.UltraWideAngle.html) or [WebCamKind.Telephoto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.Telephoto.html). As there is currently no web API that returns the focal length of a webcam device, the WebGL applications always return [WebCamDevice.kind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice-kind.html) as WideAngle.  
  
Additional resources: [WebCamDevice.kind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamDevice-kind.html).
### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.Unknown.html) | The camera type is unknown.  
[WideAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.WideAngle.html) | Wide angle (default) camera.  
[Telephoto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.Telephoto.html) | A Telephoto camera device. These devices have a longer focal length than a wide-angle camera.  
[ColorAndDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.ColorAndDepth.html) | Camera which supports synchronized color and depth data (currently these are only dual back and true depth cameras on latest iOS devices).  
[UltraWideAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamKind.UltraWideAngle.html) | Ultra wide angle camera. These devices have a shorter focal length than a wide-angle camera.  
* * *
