* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineDisposed.html

#  [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html).activeRenderPipelineDisposed
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
Delegate that you can use to invoke custom code right before [RenderPipelineManager.currentPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-currentPipeline.html) is disposed.
Whenever you switch [GraphicsSettings.currentRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html) or [QualitySettings.renderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html), Unity will dispose the current `RenderPipeline` before instantiate the new `RenderPipeline`. You can subscribe to this event to know when current `RenderPipeline` will be disposed. To access the currently disposing `RenderPipeline` object you can rely on [RenderPipelineManager.currentPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-currentPipeline.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class CurrentRenderPipelineDisposedExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        RenderPipelineManager.activeRenderPipelineDisposed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineDisposed.html) += RenderPipelineManager_activeRenderPipelineDisposed;
    }  
  
    private void OnDestroy()
    {
        RenderPipelineManager.activeRenderPipelineDisposed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineDisposed.html) -= RenderPipelineManager_activeRenderPipelineDisposed;
    }  
  
    private void RenderPipelineManager_activeRenderPipelineDisposed()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Render Pipeline {RenderPipelineManager.currentPipeline.GetType().Name} is disposing.");
    }
}

```

* * *
