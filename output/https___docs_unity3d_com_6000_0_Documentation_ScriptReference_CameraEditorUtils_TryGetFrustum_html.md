* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.TryGetFrustum.html

#  [CameraEditorUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.html).TryGetFrustum
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
public static bool TryGetFrustum([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, Vector3[] near, Vector3[] far, out float frustumAspect); 
### Parameters
Parameter | Description  
---|---  
camera | Camera to use.  
near | The corners of the near plane. (A minimum size of 4 elements is required.)  
far | The corners of the far plane. (A minimum size of 4 elements is required.)  
frustumAspect | The aspect ratio of the frustrum.  
### Returns
**bool** Whether the frustrum was calculated. 
### Description
Calculate the frustrum corners.  
  
Corners are calculated in this order: left bottom, left top, right top, right bottom.
* * *
