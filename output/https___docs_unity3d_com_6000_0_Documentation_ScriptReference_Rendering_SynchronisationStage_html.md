* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.html

# SynchronisationStage
enumeration
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
The stages of the draw call processing on the GPU.
Use `SynchronisationStage` to wait for a draw call stage to complete, for example when you create a [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html).
### Properties
Property | Description  
---|---  
[VertexProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.VertexProcessing.html) | The stage where the GPU processes vertices.  
[PixelProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.PixelProcessing.html) | The stage where the GPU creates and shades fragments.  
* * *
