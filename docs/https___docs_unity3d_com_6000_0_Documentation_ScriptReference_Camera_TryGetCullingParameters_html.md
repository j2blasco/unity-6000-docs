* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.TryGetCullingParameters.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).TryGetCullingParameters
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
## Declaration
public bool TryGetCullingParameters(out [Rendering.ScriptableCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html) cullingParameters); 
## Declaration
public bool TryGetCullingParameters(bool stereoAware, out [Rendering.ScriptableCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html) cullingParameters); 
### Parameters
Parameter | Description  
---|---  
cullingParameters | Resultant culling parameters.  
stereoAware | Generate single-pass stereo aware culling parameters.  
### Returns
**bool** Flag indicating whether culling parameters are valid. 
### Description
Get culling parameters for a camera.
Returns false if camera is invalid to render (empty viewport rectangle, invalid clip plane setup etc.).  
  
Both left and right stereo eyes are considered in the generated culling parameters when `stereoAware` is `true` and single-pass stereo is enabled.  
  
Additional resources: [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html), [ScriptableCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html), [ScriptableRenderContext.SetupCameraProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.SetupCameraProperties.html), [ScriptableRenderContext.StartMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StartMultiEye.html), [ScriptableRenderContext.StopMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StopMultiEye.html), [ScriptableRenderContext.StereoEndRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StereoEndRender.html).
* * *
