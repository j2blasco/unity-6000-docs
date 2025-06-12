* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).renderQueue
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
renderQueue; 
### Description
Render queue of this material.
By default materials use [render queue](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html) of the shader it uses. You can override the render queue used using this variable. Note that if a shader on the material is changed, the render queue resets to that of the shader itself.  
  
Render queue value should be in [0..5000] range to work properly; or -1 to use the render queue from the shader.  
  
Note: When Unity runs in batch mode, it does not load Scriptable Render Pipelines (SRPs) until the first time something renders. Loading an SRP modifies the sub-shader selected for a given material which can lead to the value this function returns being different than expected.  
  
Additional resources: [Shader.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html), [RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html) enum, [subshader tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
* * *
