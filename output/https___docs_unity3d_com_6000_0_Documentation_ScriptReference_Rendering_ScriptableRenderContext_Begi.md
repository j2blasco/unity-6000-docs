* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginScopedRenderPass.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).BeginScopedRenderPass
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
public [Rendering.ScopedRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScopedRenderPass.html) BeginScopedRenderPass(int width, int height, int samples, NativeArray<AttachmentDescriptor> attachments, int depthAttachmentIndex); 
### Parameters
Parameter | Description  
---|---  
width | The width of the render pass surfaces in pixels.  
height | The height of the render pass surfaces in pixels.  
samples | MSAA sample count; set to 1 to disable antialiasing.  
attachments | Array of color attachments to use within this render pass. The values in the array are copied immediately.  
depthAttachmentIndex | The index of the attachment to be used as the depth/stencil buffer for this render pass, or -1 to disable depth/stencil.  
### Description
Schedules the beginning of a new render pass. If you call this a using-statement, Unity calls EndRenderPass automatically when exiting the using-block. Only one render pass can be active at any time.
This method does the same as [BeginRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html), but it will return an _IDisposable_ that can be used in a _using_ -statement, and so it is not necesssary to manually call [EndRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.EndRenderPass.html).  
  
A render pass provides a new way to switch rendertargets in the context of a Scriptable Rendering Pipeline. As opposed to the SetRenderTargets function, the render pass specifies a clear beginning and an end for the rendering, alongside explicit load/store actions on the rendering surfaces.  
  
The render pass also allows running multiple subpasses within the same renderpass, where the pixel shaders have a read access to the current pixel value within the renderpass. This allows for efficient implementation of various rendering methods on tile-based GPUs, such as deferred rendering.  
  
Render passes are natively implemented on Metal (iOS) and Vulkan, but the API is fully functional on all rendering backends via emulation (using legacy SetRenderTargets calls and reading the current pixel values via texel fetches).  
  
The render pass mechanism has the following limitations: - All attachments must have the same resolution and MSAA sample count - The rendering results of previous subpasses are only available within the same screen-space pixel coordinate via the UNITY_READ_FRAMEBUFFER_INPUT(x) macro in the shader; the attachments cannot be bound as textures or otherwise accessed until the renderpass has ended - iOS Metal does not allow reading from the Z-Buffer, so an additional render target is needed to work around that - The maximum amount of attachments allowed per render pass is currently 8 + depth, but note that various GPUs may have stricter limits.  
  
Additional resources: [BeginScopedSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginScopedSubPass.html).
```
using UnityEngine;
using UnityEngine.Rendering;
using Unity.Collections;  
  
public static class DeferredRenderer
{
    public static void ExecuteRenderLoop(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, CullingResults[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) cullResults, ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context)
    {
        // Create the attachment descriptors. If these attachments are not specifically bound to any RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) using the ConfigureTarget calls,
        // these are treated as temporary surfaces that are discarded at the end of the renderpass
        var albedo = new AttachmentDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html)(RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
        var specRough = new AttachmentDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html)(RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
        var normal = new AttachmentDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html)(RenderTextureFormat.ARGB2101010[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB2101010.html));
        var emission = new AttachmentDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html)(RenderTextureFormat.ARGBHalf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGBHalf.html));
        var depth = new AttachmentDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html)(RenderTextureFormat.Depth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.Depth.html));  
  
        // At the beginning of the render pass, clear the emission buffer to all black, and the depth buffer to 1.0f
        emission.ConfigureClear(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.0f, 0.0f, 0.0f, 0.0f), 1.0f, 0);
        depth.ConfigureClear(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(), 1.0f, 0);  
  
        // Bind the albedo surface to the current camera target, so the final pass will render the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to the screen backbuffer
        // The second argument specifies whether the existing contents of the surface need to be loaded as the initial values;
        // in our case we do not need that because we'll be clearing the attachment anyway. This saves a lot of memory
        // bandwidth on tiled GPUs.
        // The third argument specifies whether the rendering results need to be written out to memory at the end of
        // the renderpass. We need this as we'll be generating the final image there.
        // We could do this in the constructor already, but the camera target may change on the fly, esp. in the editor
        albedo.ConfigureTarget(BuiltinRenderTextureType.CameraTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.CameraTarget.html), false, true);  
  
        // All other attachments are transient surfaces that are not stored anywhere. If the renderer allows,
        // those surfaces do not even have a memory allocated for the pixel values, saving RAM usage.  
  
        // Start the renderpass using the given scriptable rendercontext, resolution, samplecount, array of attachments that will be used within the renderpass and the depth surface
        var attachments = new NativeArray<AttachmentDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html)>(5, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        const int depthIndex = 0, albedoIndex = 1, specRoughIndex = 2, normalIndex = 3, emissionIndex = 4;
        attachments[depthIndex] = depth;
        attachments[albedoIndex] = albedo;
        attachments[specRoughIndex] = specRough;
        attachments[normalIndex] = normal;
        attachments[emissionIndex] = emission;
        using (context.BeginScopedRenderPass(camera.pixelWidth, camera.pixelHeight, 1, attachments, depthIndex))
        {
            attachments.Dispose();  
  
            // Start the first subpass, GBuffer creation: render to albedo, specRough, normal and emission, no need to read any input attachments
            var gbufferColors = new NativeArray<int>(4, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
            gbufferColors[0] = albedoIndex;
            gbufferColors[1] = specRoughIndex;
            gbufferColors[2] = normalIndex;
            gbufferColors[3] = emissionIndex;
            using (context.BeginScopedSubPass(gbufferColors))
            {
                gbufferColors.Dispose();  
  
                // Render the deferred G-Buffer
                // RenderGBuffer(cullResults, camera, context);
            }  
  
            // Second subpass, lighting: Render to the emission buffer, read from albedo, specRough, normal and depth.
            // The last parameter indicates whether the depth buffer can be bound as read-only.
            // Note that some renderers (notably iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) Metal) won't allow reading from the depth buffer while it's bound as Z-buffer,
            // so those renderers should write the Z into an additional FP32 render target manually in the pixel shader and read from it instead
            var lightingColors = new NativeArray<int>(1, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
            lightingColors[0] = emissionIndex;
            var lightingInputs = new NativeArray<int>(4, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
            lightingInputs[0] = albedoIndex;
            lightingInputs[1] = specRoughIndex;
            lightingInputs[2] = normalIndex;
            lightingInputs[3] = depthIndex;
            using (context.BeginScopedSubPass(lightingColors, lightingInputs, true))
            {
                lightingColors.Dispose();
                lightingInputs.Dispose();  
  
                // PushGlobalShadowParams(context);
                // RenderLighting(camera, cullResults, context);
            }  
  
            // Third subpass, tonemapping: Render to albedo (which is bound to the camera target), read from emission.
            var tonemappingColors = new NativeArray<int>(1, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
            tonemappingColors[0] = albedoIndex;
            var tonemappingInputs = new NativeArray<int>(1, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
            tonemappingInputs[0] = emissionIndex;
            using (context.BeginScopedSubPass(tonemappingColors, tonemappingInputs, true))
            {
                tonemappingColors.Dispose();
                tonemappingInputs.Dispose();  
  
                // present frame buffer.
                // FinalPass(context);
            }
        }
    }
}

```

* * *
