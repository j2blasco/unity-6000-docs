* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRandomWriteTarget.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).SetRandomWriteTarget
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
public static void SetRandomWriteTarget(int index, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) uav, bool preserveCounterValue = false); 
## Declaration
public static void SetRandomWriteTarget(int index, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) uav, bool preserveCounterValue = false); 
## Declaration
public static void SetRandomWriteTarget(int index, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) uav); 
### Parameters
Parameter | Description  
---|---  
index | The index of the random write target.  
uav | Buffer or texture to set as the write target.  
preserveCounterValue | Whether to leave the append/consume counter value unchanged.  
### Description
Set random write target for [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level pixel shaders.
Shader Model 4.5 and above level pixel shaders can write into arbitrary locations of some textures and buffers, called "unordered access views" (UAV) in [UsingDX11GL3Features](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html). These "random write" targets are set similarly to how multiple render targets are set. You can either use a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) with `enableRandomWrite` flag set, or a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) as target.  
  
Offset the index value given to `SetRandomWriteTarget` by adding the number of render targets used. This value might not correspond exactly to the fixed register index set in the shaders as the UAV indexing value can vary between different platforms. Refer to the platform-specific documentation for details of these differences. On DX11, the first valid UAV index is the number of active render targets, so in the common case of a single render target, the UAV indexing will start from 1. Platforms using automatically translated HLSL shaders will match this behavior, however, with hand-written GLSL shaders the indexes will match the bindings.  
  
When setting a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), the `preserveCounterValue` parameter indicates whether to leave the counter value unchanged, or reset it to 0 (the default behaviour).  
  
The targets stay set until you manually clear them with [ClearRandomWriteTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ClearRandomWriteTargets.html). It is best practice to call ClearRandomWriteTargets after your rendering is complete. If you do not do this, rendering issues can occur and some built-in Unity rendering passes may crash.  
  
Additional resources: [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html), [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), [ComputeBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetCounterValue.html), [UsingDX11GL3Features](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html).
* * *
