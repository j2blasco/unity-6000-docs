* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.WarmupShaderFromCollection.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html).WarmupShaderFromCollection
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
public static void WarmupShaderFromCollection([ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html) collection, [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, [Experimental.Rendering.ShaderWarmupSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmupSetup.html) setup); 
### Description
Prewarms the shader variants for a given [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) that are in a given [ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html), using a given rendering configuration.
For information on shader loading and prewarming, including a list of different prewarming techniques, see [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html).  
  
Unity needs more information to correctly build GPU representations of the shader variants ('pipeline state objects' or PSOs) if your application runs on one of the following graphics APIs: 
  * DirectX 12
  * Metal
  * Vulkan


If Unity has this information, it's more likely the prewarmed variants match what the GPU needs when it renders your Scene.  
  
To provide Unity with more information, you can do the following: 
  * Use the `setup` parameter to specify the vertex data layout you use with the shader.
  * Before you call `WarmupShader`, set the render state so it's as close as possible to the state you use with the shader. For example, set the [format of the render target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html), or use [render state commands](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-commands.html) to set states such as blend mode.


Unity also asynchronously prewarms shader variants using multiple background threads, if your application runs on a platform that supports it. Unity uses as many threads as it can. In your built application, you can use the `-max-async-pso-job-count` [command line argument](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html) to set the number of threads Unity uses.  
  
Additional resources: [ShaderWarmup.WarmupShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.WarmupShader.html), [Shader.WarmupAllShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.WarmupAllShaders.html), [ShaderVariantCollection.WarmUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUp.html), [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html)
* * *
