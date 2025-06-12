* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.CustomProvided.html

#  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html).CustomProvided
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
The light probe shader uniform values are extracted from the material property block set on the renderer.
Property `unity_SHAr`, `unity_SHAg`, `unity_SHAb`, `unity_SHBr`, `unity_SHBg`, `unity_SHBb` and `unity_SHC` will be set to zero if they are not part of the MaterialPropertyBlock.  
Property `unity_ProbesOcclusion` will be calculated as in normal lighting if it is not part of the MaterialPropertyBlock.  
  
Note that using the light probe values baked at a different place may lead to incorrect rendering, especially when local lights (i.e. point lights and spot lights) are used. This mode is more useful when drawing instanced objects with [Graphics.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstanced.html), where the light probe data is pre-calculated and provided as arrays.  
  
Additional resources: [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), [MaterialPropertyBlock.CopySHCoefficientArraysFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopySHCoefficientArraysFrom.html), [MaterialPropertyBlock.CopyProbeOcclusionArrayFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html).
* * *
