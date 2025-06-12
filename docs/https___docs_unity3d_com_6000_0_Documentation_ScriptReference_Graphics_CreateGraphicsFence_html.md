* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CreateGraphicsFence.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).CreateGraphicsFence
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
public static [Rendering.GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html) CreateGraphicsFence([Rendering.GraphicsFenceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFenceType.html) fenceType, [Rendering.SynchronisationStageFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.html) stage = SynchronisationStage.PixelProcessing); 
### Parameters
Parameter | Description  
---|---  
fenceType | The [GraphicsFenceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFenceType.html) to create. Currently the only supported value is [GraphicsFenceType.AsyncQueueSynchronisation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFenceType.AsyncQueueSynchronisation.html).  
stage | Which [SynchronisationStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.html) to insert the fence after.  
### Returns
**GraphicsFence** Returns a new [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html). 
### Description
Creates a [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html).
The GPU passes through the `GraphicsFence` fence after it completes the `Blit`, `Clear`, `Draw`, `Dispatch` or texture copy command you sent before this call. This includes commands from [command buffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) that the GPU executes immediately before you create the fence.  
  
You can use the `stage` parameter to insert the [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html) fence after the end of either vertex or pixel processing. On some platforms, there's a gap between the end of vertex processing and the start of pixel processing in a draw call.  
  
If the previous command was a compute shader dispatch, Unity ignores `stage`.  
  
Some platforms cannot differentiate between the end of vertex processing and the end of pixel processing. On these platforms, you'll get the same results regardless of whether you use [SynchronisationStage.PixelProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.PixelProcessing.html) or [SynchronisationStage.VertexProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.VertexProcessing.html) as the value for `stage`.  
  
If you call `CreateGraphicsFence` on a platform that doesn't support fences, the fence has no function, and the methods [Graphics.WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.WaitOnAsyncGraphicsFence.html) and [CommandBuffer.WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.WaitOnAsyncGraphicsFence.html) do nothing. Use [SystemInfo.supportsGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsGraphicsFence.html) to check if a platform supports fences.  
  
Additional resources: [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html), [Graphics.WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.WaitOnAsyncGraphicsFence.html), [CommandBuffer.WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.WaitOnAsyncGraphicsFence.html).
* * *
