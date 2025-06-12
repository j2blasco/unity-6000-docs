* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.html

# BatchDrawCommandFlags
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
Rendering options for the [BatchDrawCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand.html) struct.
.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.None.html) | This draw command does not have any special settings.  
[FlipWinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.FlipWinding.html) | Unity reverses the triangle winding in this draw command. Usage example: the transform has a negative scale.  
[HasMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.HasMotion.html) | The draw command renders per-object motion vectors.  
[IsLightMapped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.IsLightMapped.html) | The draw command uses light maps. Light maps might not work correctly unless this flag is set when a draw command uses them.  
[HasSortingPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.HasSortingPosition.html) | Instances in the draw command have explicit world space sorting positions in the instanceSortingPositions array. Unity uses those sorting positions for depth sorting.  
[LODCrossFadeKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.LODCrossFadeKeyword.html) | The draw command has LOD_FADE_CROSSFADE keyword enabled.  
[LODCrossFadeValuePacked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.LODCrossFadeValuePacked.html) | The draw command has instances that have an 8-bit crossfade dither factor in the highest bits of their visible instance index.  
[LODCrossFade](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.LODCrossFade.html) | The draw command has both LOD_FADE_CROSSFADE keyword enabled and has instances that have an 8-bit crossfade dither factor in the highest bits of their visible instance index.  
[UseLegacyLightmapsKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.UseLegacyLightmapsKeyword.html) | The draw command has USE_LEGACY_LIGHTMAPS keyword enabled. When this flag is set, BatchDrawCommand.lightmapIndex is used to determine batching.  
* * *
