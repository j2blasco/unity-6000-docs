* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDevice-fovZoomFactor.html

#  [XRDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDevice.html).fovZoomFactor
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
fovZoomFactor; 
### Description
Zooms the XR projection.
Set this to zoom the XR projection matrix by scaling the viewing frustum. The value is clamped so that it will never fall below 1.0f. For asymmetric XR projections, setting the FoV doesn't make sense, so use this property to scale the frustum half angles uniformly by a single value.  
  
For example: A symmetric frustum starting with an FoV of 90 degrees, an fovZoomFactor of 2 will scale the viewing frustum so that it has an FoV of 45 degrees.
* * *
