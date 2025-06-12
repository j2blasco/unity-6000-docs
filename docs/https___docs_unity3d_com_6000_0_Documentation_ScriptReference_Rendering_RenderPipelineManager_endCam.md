* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html

#  [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html).endCameraRendering
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
Delegate that you can use to invoke custom code after Unity renders an individual Camera.
When Unity calls [RenderPipeline.EndCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndCameraRendering.html), it executes the methods in this delegate's invocation list.  
  
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline (HDRP), Unity calls [RenderPipeline.EndCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndCameraRendering.html) automatically. If you are writing a custom Scriptable Render Pipeline and you want to use this delegate, you must add a call to [RenderPipeline.EndCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndCameraRendering.html).  
  
The following code example demonstrates how to add a method to this delegate's invocation list, and later remove it.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        RenderPipelineManager.endCameraRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) += OnEndCameraRendering;
    }  
  
    void OnEndCameraRendering(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera)
    {
        // Put the code that you want to execute after the camera renders here
        // If you are using URP or HDRP, Unity calls this method automatically
        // If you are writing a custom SRP, you must call RenderPipeline.EndCameraRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndCameraRendering.html)
    }  
  
    void OnDestroy()
    {
        RenderPipelineManager.endCameraRendering[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) -= OnEndCameraRendering;
    }
}

```

Additional resources: [RenderPipeline.BeginCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginCameraRendering.html), [RenderPipeline.EndCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndCameraRendering.html), [RenderPipeline.BeginFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.BeginFrameRendering.html), [RenderPipeline.EndFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.EndFrameRendering.html), [Unity Manual: Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptableRenderPipeline.html)
* * *
