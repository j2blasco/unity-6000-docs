* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html

#  [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html).endContextRendering
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
Delegate that you can use to invoke custom code at the end of [RenderPipeline.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html).
When Unity calls [RenderPipeline.BeginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginContextRendering.html) at the end of [RenderPipeline.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html), it executes the methods in this delegate's invocation list.  
  
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline (HDRP), Unity calls [RenderPipeline.BeginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginContextRendering.html) automatically. If you are writing a custom Scriptable Render Pipeline, you must call the method yourself. This functionality is not compatible with the Built-in Render Pipeline.  
  
This delegate works in the same way as [RenderPipelineManager.endFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endFrameRendering.html), except that this version does not cause heap allocations.  
  
The following code example demonstrates how to add a method to this delegate's invocation list, and later remove it. 
```
using UnityEngine;
using UnityEngine.Rendering;
using System.Collections.Generic;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        RenderPipelineManager.endContextRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html) += OnEndContextRendering;
    }  
  
    void OnEndContextRendering(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, List<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)> cameras)
    {
        // Put the code that you want to execute at the end of RenderPipeline.Render[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html) here
    }  
  
    void OnDestroy()
    {
        RenderPipelineManager.endContextRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html) -= OnEndContextRendering;
    }
}

```

Additional resources: [RenderPipeline.EndContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndContextRendering.html), [RenderPipelineManager.beginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-beginContextRendering.html), [RenderPipeline.BeginContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginContextRendering.html), [Unity Manual: Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptableRenderPipeline.html)
* * *
