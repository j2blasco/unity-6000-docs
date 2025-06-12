* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.TryGetSensorGateFrustum.html

#  [CameraEditorUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.html).TryGetSensorGateFrustum
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
public static bool TryGetSensorGateFrustum([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, Vector3[] near, Vector3[] far, out float frustumAspect); 
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
Calculate the frustrum corners from the sensor physical properties, without taking gate fitting into account. To get the actual frustum with gate fit adjustment, use [CameraEditorUtils.TryGetFrustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.TryGetFrustum.html). This method is equivalent to [CameraEditorUtils.TryGetFrustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.TryGetFrustum.html) for non-physical cameras.  
  
Corners are calculated in this order: left bottom, left top, right top, right bottom.
* * *
