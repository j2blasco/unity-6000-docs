* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-rawRenderQueue.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).rawRenderQueue
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
rawRenderQueue; 
### Description
Raw render queue of this material.
This property returns the render queue override value of this material. The value returned is -1 if no override has been specified (i.e. the actual renderQueue value used for rendering will be [Shader.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html)), or a custom value in [0..5000] range if set.  
  
For purposes of getting the actual render queue value used for rendering, refer to [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html).  
  
Additional resources: [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html), [Shader.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html), [RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html) enum, [subshader tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
* * *
