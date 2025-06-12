* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DepthTextureMode.DepthNormals.html

#  [DepthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DepthTextureMode.html).DepthNormals
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
Generate a depth + normals texture.
Will generate a screen-space depth and view space normals texture as seen from this camera. Texture will be in [RenderTextureFormat.ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html) format and will be set as `_CameraDepthNormalsTexture` global shader property. Depth and normals will be specially encoded, see [Camera Depth Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture.html) page for details.  
  
Additional resources: [Using camera's depth textures](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture.html), [Camera.depthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-depthTextureMode.html).
* * *
