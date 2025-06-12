* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CreateAsyncGraphicsFence.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).CreateAsyncGraphicsFence
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
public static [Rendering.GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html) CreateAsyncGraphicsFence([Rendering.SynchronisationStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.html) stage = SynchronisationStage.PixelProcessing); 
## Declaration
public static [Rendering.GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html) CreateAsyncGraphicsFence(); 
### Parameters
Parameter | Description  
---|---  
stage | Which [SynchronisationStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.html) to insert the fence after.  
### Returns
**GraphicsFence** Returns a new [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html). 
### Description
Shortcut for calling [Graphics.CreateGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CreateGraphicsFence.html) with [GraphicsFenceType.AsyncQueueSynchronisation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFenceType.AsyncQueueSynchronisation.html) as the first parameter.
Additional resources: [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html), [Graphics.WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.WaitOnAsyncGraphicsFence.html), [CommandBuffer.WaitOnAsyncGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.WaitOnAsyncGraphicsFence.html).
* * *
