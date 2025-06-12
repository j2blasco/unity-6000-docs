* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).renderQueue
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
renderQueue; 
### Description
Render queue of this shader. (Read Only)
Since different Render Pipelines require different render passes a shader's render queue depends on the active Render Pipeline. Note: When Unity runs in batch mode, it does not load Scriptable Render Pipelines (SRPs) until the first time something renders. Loading an SRP modifies the sub-shader selected for a given material which can lead to the value this function returns being different than expected.  
  
Additional resources: [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html), [RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html) enum, [subshader tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
* * *
