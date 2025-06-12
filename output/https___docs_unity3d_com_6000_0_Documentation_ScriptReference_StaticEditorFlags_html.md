* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html

# StaticEditorFlags
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
Describes which Unity systems consider the GameObject as static, and include the GameObject in their precomputations in the Unity Editor.
Setting StaticEditorFlags at runtime has no effect on these systems.  
  
For more information, see the [ Unity Manual documentation on StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html).  
  
Additional resources: [GameObjectUtility.SetStaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html), [GameObject.isStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-isStatic.html)
### Properties
Property | Description  
---|---  
[ContributeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html) | Include the target Mesh Renderer in global illumination calculations.  
[OccluderStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.OccluderStatic.html) | Mark the GameObject as a Static Occluder in the occlusion culling system.  
[OccludeeStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.OccludeeStatic.html) | Mark the GameObject as a Static Occludee in the occlusion culling system.  
[BatchingStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.BatchingStatic.html) | Combine the GameObject's Mesh with other eligible Meshes, to potentially reduce runtime rendering costs.  
[ReflectionProbeStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ReflectionProbeStatic.html) | Include this GameObject when when precomputing data for Reflection Probes whose Type property is set to Baked.  
* * *
