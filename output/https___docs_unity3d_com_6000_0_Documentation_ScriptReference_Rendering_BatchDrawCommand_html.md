* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand.html

# BatchDrawCommand
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
Represents a draw command for a [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html). 
### Properties
Property | Description  
---|---  
[batchID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-batchID.html) | The batch ID that this draw command uses. Determines the metadata values that are available to a shader.  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-flags.html) | Specifies rendering options for the draw command.  
[lightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-lightmapIndex.html) | The index of the baked lightmap used in this draw command. If BatchDrawCommandFlags.UseLegacyLightmapsKeyword is not set, this value is ignored.  
[materialID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-materialID.html) | Identifies which Material to use to render the instances in this draw command.  
[meshID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-meshID.html) | Identifies which Mesh to use to render the instances in this draw command.  
[sortingPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-sortingPosition.html) | Together with BatchDrawCommand.flags, this specifies how to depth sort the instances in this draw command.  
[splitVisibilityMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-splitVisibilityMask.html) | Indicates which splits that the draw command is visible in.  
[submeshIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-submeshIndex.html) | Specifies which sub-mesh of the Mesh identified by BatchDrawCommand.meshID to use to render the instances in this draw command.  
[visibleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-visibleCount.html) | The number of instances to draw with this draw command. This must be a value greater than 1.  
[visibleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-visibleOffset.html) | The index of the element in BatchCullingOutputDrawCommands.visibleInstances that matches the first instance in this draw command.  
* * *
