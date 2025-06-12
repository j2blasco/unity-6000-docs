* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.GetVertexBuffer.html

#  [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html).GetVertexBuffer
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html "Go to SkinnedMeshRenderer Component in the Manual")
## Declaration
public [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) GetVertexBuffer(); 
### Returns
**GraphicsBuffer** The skinned mesh vertex buffer as a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html). 
### Description
Retrieves a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) that provides direct access to the GPU vertex buffer for this skinned mesh, for the current frame.
During motion vector rendering (used for motion blur, temporal anti-aliasing, or other effects), skinned meshes that have [skinnedMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-skinnedMotionVectors.html) on alternate between two GPU vertex buffers. You can access the GPU vertex buffer for the current frame using `GetVertexBuffer`, and for the previous frame using [GetPreviousVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.GetPreviousVertexBuffer.html).  
  
You can use this method to access the skinned mesh vertex buffer for the current frame in a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html). To do that, first request an appropriate buffer binding target via [vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-vertexBufferTarget.html), then get the graphics buffer using `GetVertexBuffer`, and then set it up as a parameter for your shaders using ComputeBuffer.SetBuffer, [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html) and similar methods.  
  
Additional resources: [vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-vertexBufferTarget.html), [GetPreviousVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.GetPreviousVertexBuffer.html).
* * *
