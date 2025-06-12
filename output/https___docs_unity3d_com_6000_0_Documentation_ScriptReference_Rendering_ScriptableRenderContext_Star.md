* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StartMultiEye.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).StartMultiEye
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
public void StartMultiEye([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
## Declaration
public void StartMultiEye([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, int eye); 
### Parameters
Parameter | Description  
---|---  
camera | Camera to enable stereo rendering on.  
eye | The current eye to be rendered.  
### Description
Schedules a fine-grained beginning of stereo rendering on the ScriptableRenderContext.
Activates stereo rendering on the [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) and `camera`. When used in conjunction with [StopMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StopMultiEye.html), these APIs provide fine-grained control of which draw calls are multi-plexed for stereo purposes. For example, you would wrap your opaque and transparent passes with [StartMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StartMultiEye.html) and [StopMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StopMultiEye.html), but you could exclude your shadow rendering.  
  
Note that only draws are affected by this API. Compute work is not automatically adjusted for stereo, therefore, per-eye compute work must be manually generated.  
  
Additional resources: [StopMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StopMultiEye.html), [SetupCameraProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.SetupCameraProperties.html), [StereoEndRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StereoEndRender.html), CullingResults.GetCullingParameters.
* * *
