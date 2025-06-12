* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.html

# SynchronisationStageFlags
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
Describes the various stages of GPU processing against which the GraphicsFence can be set and waited against.
The enum values can be combined; for example, a GraphicsFence created with SynchronisationStageFlags.VertexProcessing | SynchronisationStageFlags.ComputeProcessing flags would complete once all previous draw calls have completed their vertex shaders and all previous compute shader dispatches have completed.
### Properties
Property | Description  
---|---  
[VertexProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.VertexProcessing.html) | All aspects of vertex processing in the GPU.  
[PixelProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.PixelProcessing.html) | All aspects of pixel processing in the GPU.  
[ComputeProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.ComputeProcessing.html) | All compute shader dispatch operations.  
[AllGPUOperations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.AllGPUOperations.html) | All previous GPU operations (vertex, pixel and compute).  
* * *
