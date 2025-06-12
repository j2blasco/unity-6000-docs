* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.html

# CameraEditorUtils
class in UnityEditor
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
Utilities for cameras.
### Static Properties
Property | Description  
---|---  
[GameViewAspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.GameViewAspectRatio.html) | The aspect ratio of the game view.  
[virtualCameraPreviewInstantiator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils-virtualCameraPreviewInstantiator.html) | Override this function to pass your own Camera provider to generate previews for virtual cameras.  
### Static Methods
Method | Description  
---|---  
[DrawFrustumGizmo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.DrawFrustumGizmo.html) | Draw the frustrum gizmo of a camera.  
[GetFrustumAspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.GetFrustumAspectRatio.html) | Calculate the frustrum aspect ratio of a camera.  
[GetFrustumPlaneAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.GetFrustumPlaneAt.html) | Calculate the points of the frustrum plane facing the viewer at a specific distance.The points array will be filled with the calculated points in the following order: left bottom, left top, right top and right bottom.  
[HandleFrustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.HandleFrustum.html) | Draw the frustrum handles for a camera.  
[IsViewportRectValidToRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.IsViewportRectValidToRender.html) | Check whether a viewport is valid.  
[PerspectiveClipToWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.PerspectiveClipToWorld.html) | Calculate the world space position of a point in clip space.The z component will be used to get the point at the distance z from the viewer.  
[TryGetFrustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.TryGetFrustum.html) | Calculate the frustrum corners.Corners are calculated in this order: left bottom, left top, right top, right bottom.  
[TryGetSensorGateFrustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.TryGetSensorGateFrustum.html) | Calculate the frustrum corners from the sensor physical properties, without taking gate fitting into account. To get the actual frustum with gate fit adjustment, use CameraEditorUtils.TryGetFrustum. This method is equivalent to CameraEditorUtils.TryGetFrustum for non-physical cameras.Corners are calculated in this order: left bottom, left top, right top, right bottom.  
* * *
