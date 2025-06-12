* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginContextRendering.html

#  [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html).BeginContextRendering
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
protected static void BeginContextRendering([Rendering.ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, List<Camera> cameras); 
### Description
Calls the [RenderPipelineManager.beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html) and [RenderPipelineManager.beginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginFrameRendering.html) delegates.
Use the delegates that this method calls to implement functionality at the start of [RenderPipeline.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html).  
  
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline (HDRP), Unity calls this method automatically at the start of [RenderPipeline.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html). If you are writing a custom Scriptable Render Pipeline, you can call this method yourself in the same place. This functionality is not compatible with the Built-in Render Pipeline.  
  
The delegates that this method calls work in the same way as one another, except that [RenderPipelineManager.beginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginFrameRendering.html) causes heap allocations and [RenderPipelineManager.beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html) does not. You should therefore use [RenderPipelineManager.beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html) to avoid unnecessary heap allocations and garbage collection.  
  
This method replaces [RenderPipeline.BeginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginFrameRendering.html). It does everything that method does, and in addition it calls the [RenderPipelineManager.beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html) delegate. If you are writing a custom Scriptable Render Pipeline, use this method instead of [RenderPipeline.BeginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginFrameRendering.html).  
  
The following code example demonstrates where to call this method if you are creating a custom Scriptable Render Pipeline: 
```
using UnityEngine;
using UnityEngine.Rendering;
using System.Collections.Generic;  
  
public class ExampleRenderPipelineInstance : RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html)
{
    public ExampleRenderPipelineInstance()
    {
    }  
  
    override protected void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, List<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)> cameras)
    {
        // Call the RenderPipelineManager.beginContextRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html) and RenderPipelineManager.beginFrameRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginFrameRendering.html) delegates
        BeginContextRendering(context, cameras);  
  
        // Put the rest of your Render method code here
    }  
  
    // Older version of the Render function that can generate garbage, needed for backwards compatibility
    override protected void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras)
    {
    }
}

```

Additional resources: [RenderPipelineManager.beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html), [RenderPipelineManager.beginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginFrameRendering.html), [RenderPipeline.EndContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndContextRendering.html), [Unity Manual: Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptableRenderPipeline.html)
* * *
