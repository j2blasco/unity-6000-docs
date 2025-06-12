* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-cameraRelativeLightCulling.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).cameraRelativeLightCulling
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
cameraRelativeLightCulling; 
### Description
Enable or disable using the camera position as the reference point for culling lights.
When Unity culls distant lights, a light that's far away from the world space origin can flicker. The flickering happens because GameObject coordinates become increasingly less precise as they get further away, so the light moves in and out of culling range.  
  
If you set `cameraRelativeLightCulling` to `true`, Unity uses the camera position as the reference point for culling lights instead of the world space origin. This can reduce flickering.  
  
If a light is closer to the world space origin than the camera position, setting `cameraRelativeLightCulling` to `true` may introduce flickering or make it worse. You can use the following approaches instead: 
  * Reduce [Camera.farClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-farClipPlane.html) to avoid the distance of lights becoming too large for precise calculations.
  * Make everything in your scene smaller, to reduce distances across your whole scene.


Additional resources: [GraphicsSettings.cameraRelativeShadowCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-cameraRelativeShadowCulling.html)
* * *
