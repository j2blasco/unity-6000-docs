* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SinglePassStereoMode.Multiview.html

#  [SinglePassStereoMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SinglePassStereoMode.html).Multiview
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
Render stereo using OpenGL multiview.
In multiview single-pass stereo rendering, the rendering pipeline traverses the scene graph only once and issues a single, instanced draw call for each render node, thus reducing the bandwidth required to render the scene. Scene culling and shadow map rendering is shared between both eyes. The main render target must be an array of render targets.  
  
Special GPU hardware support is required for this mode to run. Depending on their graphics capabilities, certain GPUs can run this stereo rendering mode and others can run [SinglePassStereoMode.Instancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SinglePassStereoMode.Instancing.html). The two modes are otherwise very similar. 
* * *
