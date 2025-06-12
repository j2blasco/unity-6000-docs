* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUp.html

#  [ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html).WarmUp
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
public void WarmUp(); 
### Description
Prewarms all shader variants in this shader variant collection.
For information on shader loading and prewarming, including a list of different prewarming techniques, see [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html).  
  
**Warning:** This method is fully supported on DX11 and OpenGL. On DX12, Vulkan, and Metal, the graphics driver might still need to perform work if the vertex layout and/or the render target setup is different from the data used to prewarm it. This can result in wasted work and GPU memory, and still leave visible stalls in your application. [ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html) is supported on all graphics APIs.  
  
Additional resources: [ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html), [Shader.WarmupAllShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.WarmupAllShaders.html), [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html)
* * *
