* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullSpherical.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).layerCullSpherical
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
layerCullSpherical; 
### Description
How to perform per-layer culling for a Camera.
Normally this type of culling is performed by moving the Camera's far plane closer to the eye. By setting this value to true, the culling is instead based on spherical distance. The benefit is that rotating on the same spot does not affect which objects are visible.  
  
This API is only available with the Built-in renderer.  
  
Additional resources: [layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html).
* * *
