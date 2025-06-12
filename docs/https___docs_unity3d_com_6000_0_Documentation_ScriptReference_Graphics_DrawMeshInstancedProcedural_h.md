* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedProcedural.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawMeshInstancedProcedural
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
public static void DrawMeshInstancedProcedural([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, int count, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows, int layer, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [Rendering.LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) lightProbeUsage, [LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) lightProbeProxyVolume); 
### Parameters
Parameter | Description  
---|---  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to draw.  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
bounds | The bounding volume surrounding the instances you intend to draw.  
count | The number of instances to be drawn.  
properties | Additional material properties to apply. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
castShadows | Determines whether the Meshes should cast shadows.  
receiveShadows | Determines whether the Meshes should receive shadows.  
layer |  [Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) to use.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be drawn in the given Camera only.  
lightProbeUsage |  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) for the instances.  
### Description
This function is now obsolete. Use [Graphics.RenderMeshPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshPrimitives.html) instead. Draws the same mesh multiple times using GPU instancing. This is similar to [Graphics.DrawMeshInstancedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedIndirect.html), except that when the instance count is known from script, it can be supplied directly using this method, rather than via a ComputeBuffer.
To render the instances with light probes, provide the light probe data via the MaterialPropertyBlock and specify `lightProbeUsage` with [LightProbeUsage.CustomProvided](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.CustomProvided.html). Check [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) for the details. Additional resources: [Graphics.RenderMeshPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshPrimitives.html).
* * *
