* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-areVRStereoViewMatricesWithinSingleCullTolerance.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).areVRStereoViewMatricesWithinSingleCullTolerance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
areVRStereoViewMatricesWithinSingleCullTolerance; 
### Description
Determines whether the stereo view matrices are suitable to allow for a single pass cull.
If the stereo view matrices are set manually by calling [Camera.SetStereoViewMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoViewMatrix.html), then the Camera will use this check to determine whether the matrices are similar enough to enable single pass culling, which is more performant. The matrices need to point in the same direction as the center eye and be within eye distance apart.  
  
If this check fails, then  
• The camera performs a separate cull for each eye.  
• Shadows cannot be shared between the eyes.  
• Single-pass rendering cannot be used.  
  
Additional resources: [Camera.SetStereoViewMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoViewMatrix.html)
* * *
