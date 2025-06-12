* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StereoEndRender.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).StereoEndRender
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
public void StereoEndRender([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
## Declaration
public void StereoEndRender([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, int eye); 
## Declaration
public void StereoEndRender([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, int eye, bool isFinalPass); 
### Parameters
Parameter | Description  
---|---  
camera | Camera to indicate completion of stereo rendering.  
eye | The current eye to be rendered.  
### Description
Schedule notification of completion of stereo rendering on a single frame.
Notify clients that stereo rendering has completed so they can begin any post-render work.  
  
Additionally, this API will reset properties on the `camera` that had been affected by stereo rendering.  
  
Additional resources: [SetupCameraProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.SetupCameraProperties.html), [StartMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StartMultiEye.html), [StopMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StopMultiEye.html), [Camera.TryGetCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.TryGetCullingParameters.html).
* * *
