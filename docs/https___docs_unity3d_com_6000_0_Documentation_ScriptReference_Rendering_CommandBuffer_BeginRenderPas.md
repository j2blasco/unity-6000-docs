* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BeginRenderPass.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).BeginRenderPass
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
public void BeginRenderPass(int width, int height, int samples, NativeArray<AttachmentDescriptor> attachments, int depthAttachmentIndex, NativeArray<SubPassDescriptor> subPasses); 
## Declaration
public void BeginRenderPass(int width, int height, int volumeDepth, int samples, NativeArray<AttachmentDescriptor> attachments, int depthAttachmentIndex, NativeArray<SubPassDescriptor> subPasses); 
## Declaration
public void BeginRenderPass(int width, int height, int samples, NativeArray<AttachmentDescriptor> attachments, int depthAttachmentIndex, NativeArray<SubPassDescriptor> subPasses, ReadOnlySpan<byte> debugNameUtf8); 
## Declaration
public void BeginRenderPass(int width, int height, int volumeDepth, int samples, NativeArray<AttachmentDescriptor> attachments, int depthAttachmentIndex, NativeArray<SubPassDescriptor> subPasses, ReadOnlySpan<byte> debugNameUtf8); 
### Parameters
Parameter | Description  
---|---  
width | The width of the render pass surfaces in pixels.  
height | The height of the render pass surfaces in pixels.  
samples | MSAA sample count; set to 1 to disable antialiasing.  
attachments | Array of color attachments to use within this render pass. The values in the array are copied immediately.  
depthAttachmentIndex | The index of the attachment to be used as the depth/stencil buffer for this render pass, or -1 to disable depth/stencil.  
subPasses | Array containing information of each subpass. The values in the array are copied immediately.  
### Description
Begin a new native render pass.
The render pass allows multiple subpasses within the same renderpass, where the pixel shaders have a read access to the current pixel value within the renderpass. This allows for efficient implementation of various rendering methods on tile-based GPUs, such as deferred rendering.  
  
Render passes are natively implemented on Metal (iOS) and Vulkan, but the API is fully functional on all rendering backends via emulation (using legacy SetRenderTargets calls and reading the current pixel values via texel fetches).  
  
The render pass mechanism has the following limitations: - All attachments must have the same resolution and MSAA sample count - The rendering results of previous subpasses are only available within the same screen-space pixel coordinate via the UNITY_READ_FRAMEBUFFER_INPUT(x) macro in the shader; the attachments cannot be bound as textures or otherwise accessed until the renderpass has ended - iOS Metal does not allow reading from the Z-Buffer, so an additional render target is needed to work around that - The maximum amount of attachments allowed per render pass is currently 8 + depth, but note that various GPUs may have stricter limits.  
  
The first subpass is started implictly upon calling this function with following subpasses activating upon [NextSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.NextSubPass.html). After the last subpass has been scheduled, you need to close the render pass using [EndRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EndRenderPass.html).  
  
Only one render pass can be active at any time.  
  
Additional resources: [EndRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EndRenderPass.html), [NextSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.NextSubPass.html).
* * *
