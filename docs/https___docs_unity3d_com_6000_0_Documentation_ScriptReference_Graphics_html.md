* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html

# Graphics
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Raw interface to Unity's drawing functions.
This is the high-level shortcut into the optimized mesh drawing functionality of Unity.
### Static Properties
Property | Description  
---|---  
[activeColorBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeColorBuffer.html) | Currently active color buffer (Read Only).  
[activeColorGamut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeColorGamut.html) | Returns the currently active color gamut.  
[activeDepthBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeDepthBuffer.html) | Currently active depth/stencil buffer (Read Only).  
[activeTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeTier.html) | The GraphicsTier for the current device.  
[minOpenGLESVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-minOpenGLESVersion.html) | The minimum OpenGL ES version. The value is specified in PlayerSettings.  
[preserveFramebufferAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-preserveFramebufferAlpha.html) | True when rendering over native UI is enabled in Player Settings (readonly).  
### Static Methods
Method | Description  
---|---  
[Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html) | Uses a shader to copy the pixel data from a texture into a render target.  
[BlitMultiTap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.BlitMultiTap.html) | Copies source texture into destination, for multi-tap shader.  
[ClearRandomWriteTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ClearRandomWriteTargets.html) | Unset random write targets for Shader Model 4.5 level pixel shaders.  
[ConvertTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ConvertTexture.html) | Copies the pixel data from one texture, converts the data into a different format, and copies it into another texture.  
[CopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyBuffer.html) | Copies the contents of one GraphicsBuffer into another.  
[CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) | Copies pixel data from one texture to another.  
[CreateAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CreateAsyncGraphicsFence.html) | Shortcut for calling Graphics.CreateGraphicsFence with GraphicsFenceType.AsyncQueueSynchronisation as the first parameter.  
[CreateGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CreateGraphicsFence.html) | Creates a GraphicsFence.  
[DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html) | Draw a mesh.  
[DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstanced.html) | Draws the same mesh multiple times using GPU instancing.  
[DrawMeshInstancedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedIndirect.html) | This function is now obsolete. Use Graphics.RenderMeshIndirect instead. Draws the same mesh multiple times using GPU instancing.  
[DrawMeshInstancedProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedProcedural.html) | This function is now obsolete. Use Graphics.RenderMeshPrimitives instead. Draws the same mesh multiple times using GPU instancing. This is similar to Graphics.DrawMeshInstancedIndirect, except that when the instance count is known from script, it can be supplied directly using this method, rather than via a ComputeBuffer.  
[DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html) | Draw a mesh immediately.  
[DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html) | This function is now obsolete. For non-indexed rendering, use Graphics.RenderPrimitives instead. For indexed rendering, use Graphics.RenderPrimitivesIndexed. Draws procedural geometry on the GPU.  
[DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirect.html) | Draws procedural geometry on the GPU.  
[DrawProceduralIndirectNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirectNow.html) | Draws procedural geometry on the GPU.  
[DrawProceduralNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralNow.html) | Draws procedural geometry on the GPU.  
[DrawTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawTexture.html) | Draw a texture in screen coordinates.  
[ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBuffer.html) | Execute a command buffer.  
[ExecuteCommandBufferAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBufferAsync.html) | Executes a command buffer on an async compute queue with the queue selected based on the ComputeQueueType parameter passed.  
[RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html) | Renders a mesh with given rendering parameters.  
[RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html) | Renders multiple instances of a mesh using GPU instancing and rendering command arguments from commandBuffer.  
[RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html) | Renders multiple instances of a mesh using GPU instancing.  
[RenderMeshPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshPrimitives.html) | Renders multiple instances of a Mesh using GPU instancing and a custom shader.  
[RenderPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitives.html) | Renders non-indexed primitives with GPU instancing and a custom shader.  
[RenderPrimitivesIndexed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexed.html) | Renders indexed primitives with GPU instancing and a custom shader.  
[RenderPrimitivesIndexedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexedIndirect.html) | Renders indexed primitives with GPU instancing and a custom shader with rendering command arguments from commandBuffer.  
[RenderPrimitivesIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndirect.html) | Renders primitives with GPU instancing and a custom shader using rendering command arguments from commandBuffer.  
[SetRandomWriteTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRandomWriteTarget.html) | Set random write target for Shader Model 4.5 level pixel shaders.  
[SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html) | Sets current render target.  
[WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.WaitOnAsyncGraphicsFence.html) | Instructs the GPU to pause processing of the queue until it passes through the GraphicsFence fence.  
* * *
