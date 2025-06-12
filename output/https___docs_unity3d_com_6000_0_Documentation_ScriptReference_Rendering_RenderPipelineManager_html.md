* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html

# RenderPipelineManager
class in UnityEngine.Rendering
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
Render Pipeline manager.
### Static Properties
Property | Description  
---|---  
[currentPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-currentPipeline.html) | Returns the active RenderPipeline.  
[pipelineSwitchCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-pipelineSwitchCompleted.html) | Indicate when Render Pipeline switch is in progress.  
### Events
Event | Description  
---|---  
[activeRenderPipelineAssetChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineAssetChanged.html) | Delegate that you can use to invoke custom code when the current RenderPipelineAsset between frames has changed.  
[activeRenderPipelineCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineCreated.html) | Delegate that you can use to invoke custom code right after RenderPipelineManager.currentPipeline is created.  
[activeRenderPipelineDisposed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineDisposed.html) | Delegate that you can use to invoke custom code right before RenderPipelineManager.currentPipeline is disposed.  
[activeRenderPipelineTypeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineTypeChanged.html) | Delegate that you can use to invoke custom code when Unity changes the active render pipeline, and the new RenderPipeline has a different type to the old one.  
[beginCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginCameraRendering.html) | Delegate that you can use to invoke custom code before Unity renders an individual Camera.  
[beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html) | Delegate that you can use to invoke custom code at the start of RenderPipeline.Render.  
[beginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginFrameRendering.html) | Delegate that you can use to invoke custom code at the start of RenderPipeline.Render.  
[endCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) | Delegate that you can use to invoke custom code after Unity renders an individual Camera.  
[endContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html) | Delegate that you can use to invoke custom code at the end of RenderPipeline.Render.  
[endFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endFrameRendering.html) | Delegate that you can use to invoke custom code at the end of RenderPipeline.Render.  
* * *
