* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect.html

# BatchDrawCommandIndirect
struct in UnityEngine.Rendering
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
Represents an indirect draw command for a [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html). 
This type of draw command has a reference to both a material and a mesh. The actual draw data to be used is passed by the GPU in the buffer set up as the indirectArgsBufferHandle. 
### Properties
Property | Description  
---|---  
[batchID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-batchID.html) | The batch ID that this draw command uses. Determines the metadata values that are available to a shader.  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-flags.html) | Specifies rendering options for the draw command.  
[indirectArgsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-indirectArgsBufferHandle.html) |  GraphicsBufferHandle of the GraphicsBuffer from which the indirect draw command will be read.  
[indirectArgsBufferOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-indirectArgsBufferOffset.html) | Offset in bytes from which the indirect draw command will be read.  
[lightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-lightmapIndex.html) | The index of the baked lightmap used in this draw command. If lightmap texture arrays are enabled, this value is always -1 (0xFFFF).  
[materialID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-materialID.html) | Identifies which Material to use to render the instances in this draw command.  
[meshID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-meshID.html) | Identifies which Mesh to use to render the instances in this draw command.  
[sortingPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-sortingPosition.html) | Together with BatchDrawCommand.flags, this specifies how to depth sort the instances in this draw command.  
[splitVisibilityMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-splitVisibilityMask.html) | Indicates which splits that the draw command is visible in.  
[topology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-topology.html) | The primitive topology to use when executing the draw command.  
[visibleInstancesBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-visibleInstancesBufferHandle.html) | Handle of the GraphicsBuffer from which the draw command will read visible instance index.  
[visibleInstancesBufferWindowOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-visibleInstancesBufferWindowOffset.html) | Offset of the visible instances buffer that will be bound as element zero.  
[visibleInstancesBufferWindowSizeBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-visibleInstancesBufferWindowSizeBytes.html) | Amount of data in the buffer to be bound, starting from the visibleInstancesBufferWindowOffset value.  
[visibleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect-visibleOffset.html) | The index of the element in BatchCullingOutputDrawCommands.visibleInstances that matches the first instance in this draw command.  
* * *
