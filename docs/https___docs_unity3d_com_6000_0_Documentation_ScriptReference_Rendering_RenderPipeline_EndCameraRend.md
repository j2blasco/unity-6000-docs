* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndCameraRendering.html

#  [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html).EndCameraRendering
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
protected static void EndCameraRendering([Rendering.ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Description
Calls the [RenderPipelineManager.endCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) delegate.
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline (HDRP), Unity calls this method automatically after performing rendering operations for an individual Camera. If you are writing a custom Scriptable Render Pipeline, you can call this method manually to use the [RenderPipelineManager.endCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) delegate.  
  
The following code example demonstrates where to call this method if you are creating a custom Scriptable Render Pipeline:
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ExampleRenderPipelineInstance : RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html)
{
    public ExampleRenderPipelineInstance()
    {
    }  
  
    override protected void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras)
    {
        for (var i = 0; i < cameras.Length; i++)
        {
            var camera = cameras[i];  
  
            // Put your code for rendering the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) here  
  
            // Call the RenderPipelineManager.endCameraRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) delegate
            EndCameraRendering(context, camera);
        }
    }
}

```

Additional resources: [RenderPipelineManager.endCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html), [RenderPipeline.BeginCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginCameraRendering.html), [RenderPipeline.BeginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginFrameRendering.html), [RenderPipeline.EndFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndFrameRendering.html), [Unity Manual: Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptableRenderPipeline.html)
* * *
