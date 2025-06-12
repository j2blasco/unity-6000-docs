* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.WarmupAllShaders.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).WarmupAllShaders
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
## Declaration
public static void WarmupAllShaders(); 
### Description
Prewarms all shader variants of all Shaders currently in memory.
For information on shader loading and prewarming, including a list of different prewarming techniques, see [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html).  
  
While this method can be convenient, prewarming a large number of shader variants can result in long load times and high memory usage. If this is a problem, consider placing shader variants in a [ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html) instead.  
  
**Warning:** This method is fully supported on DX11 and OpenGL. On DX12, Vulkan, and Metal, the graphics driver might still need to perform work if the vertex layout and/or the render target setup is different from the data used to prewarm it. This can result in wasted work and GPU memory, and still leave visible stalls in your application. [ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html) is supported on all graphics APIs.  
  
Additional resources: [ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html), [ShaderVariantCollection.WarmUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUp.html), [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html)
* * *
