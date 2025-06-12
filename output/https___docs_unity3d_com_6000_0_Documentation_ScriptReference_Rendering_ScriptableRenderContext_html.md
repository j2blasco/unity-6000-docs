* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html

# ScriptableRenderContext
struct in UnityEngine.Rendering
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
Defines state and drawing commands that custom render pipelines use.
When you define a custom [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html), you use a ScriptableRenderContext to schedule and submit state updates and drawing commands to the GPU.  
  
A [RenderPipeline.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html) method implementation typically culls objects that the render pipeline doesn't need to render for every Camera (see [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html)), and then makes a series of calls to ScriptableRenderContext.DrawRenderers intermixed with [ScriptableRenderContext.ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.ExecuteCommandBuffer.html) calls. These calls set up global Shader properties, change render targets, dispatch compute shaders, and other rendering tasks. To actually execute the render loop, call [ScriptableRenderContext.Submit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Submit.html).  
  
Additional resources: [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html).
### Public Methods
Method | Description  
---|---  
[BeginRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html) | Schedules the beginning of a new render pass. Only one render pass can be active at any time.  
[BeginScopedRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginScopedRenderPass.html) | Schedules the beginning of a new render pass. If you call this a using-statement, Unity calls EndRenderPass automatically when exiting the using-block. Only one render pass can be active at any time.  
[BeginScopedSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginScopedSubPass.html) | Schedules the beginning of a new sub pass within a render pass. If you call this in a using-statement, Unity executes EndSubPass automatically when exiting the using-block. Render passes can never be standalone, they must always contain at least one sub pass. Only one sub pass can be active at any time.  
[BeginSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginSubPass.html) | Schedules the beginning of a new sub pass within a render pass. Render passes can never be standalone, they must always contain at least one sub pass. Only one sub pass can be active at any time.  
[CreateGizmoRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateGizmoRendererList.html) | Creates a new Gizmo RendererList.  
[CreateRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateRendererList.html) | Creates a new renderers RendererList.  
[CreateShadowRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateShadowRendererList.html) | Creates a new shadow RendererList.  
[CreateSkyboxRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateSkyboxRendererList.html) | Creates a new skybox RendererList.  
[CreateUIOverlayRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateUIOverlayRendererList.html) | Creates a new UIOverlay RendererList.  
[CreateWireOverlayRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateWireOverlayRendererList.html) | Creates a new WireOverlay RendererList.  
[Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html) | Performs culling based on the ScriptableCullingParameters typically obtained from the Camera currently being rendered.  
[CullShadowCasters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CullShadowCasters.html) | Performs shadow casters culling for all the visible lights.  
[DrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.DrawGizmos.html) | Schedules the drawing of a subset of Gizmos (before or after post-processing) for the given Camera.  
[DrawUIOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.DrawUIOverlay.html) | Draw the UI overlay.  
[DrawWireOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.DrawWireOverlay.html) | Schedules the drawing of a wireframe overlay for a given Scene view Camera.  
[EndRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.EndRenderPass.html) | Schedules the end of a currently active render pass.  
[EndSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.EndSubPass.html) | Schedules the end of the currently active sub pass.  
[ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.ExecuteCommandBuffer.html) | Schedules the execution of a custom graphics Command Buffer.  
[ExecuteCommandBufferAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.ExecuteCommandBufferAsync.html) | Schedules the execution of a Command Buffer on an async compute queue. The ComputeQueueType that you pass in determines the queue order.  
[HasInvokeOnRenderObjectCallbacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.HasInvokeOnRenderObjectCallbacks.html) | Check if any objects in the scene have OnRenderObject callbacks registered.  
[InvokeOnRenderObjectCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.InvokeOnRenderObjectCallback.html) | Schedules an invocation of the OnRenderObject callback for MonoBehaviour scripts.  
[PrepareRendererListsAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.PrepareRendererListsAsync.html) | Starts to process the provided RendererLists in the background.  
[QueryRendererListStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.QueryRendererListStatus.html) | Queries the status of a RendererList.  
[SetupCameraProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.SetupCameraProperties.html) | Schedules the setup of Camera specific global Shader variables.  
[StartMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StartMultiEye.html) | Schedules a fine-grained beginning of stereo rendering on the ScriptableRenderContext.  
[StereoEndRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StereoEndRender.html) | Schedule notification of completion of stereo rendering on a single frame.  
[StopMultiEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.StopMultiEye.html) | Schedules a stop of stereo rendering on the ScriptableRenderContext.  
[Submit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Submit.html) | Submits all the scheduled commands to the rendering loop for execution.  
[SubmitForRenderPassValidation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.SubmitForRenderPassValidation.html) | This method submits all the scheduled commands to the rendering loop for validation. The validation checks whether render passes that were started with the BeginRenderPass call can execute the scheduled commands.  
### Static Methods
Method | Description  
---|---  
[EmitGeometryForCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.EmitGeometryForCamera.html) | Emits UI geometry for rendering for the specified camera.  
[EmitWorldGeometryForSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.EmitWorldGeometryForSceneView.html) | Emits UI geometry into the Scene view for rendering.  
[PopDisableApiRenderers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.PopDisableApiRenderers.html) | Enable the immediate addition and removal of renderer scene nodes to the scene arrays.  
[PushDisableApiRenderers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.PushDisableApiRenderers.html) | Prevent the immediate addition or removal of renderer scene nodes to the scene arrays. This protects against the creation of invalid indices or dangling pointers caused by changes to the scene arrays after the culling output has been computed.  
* * *
