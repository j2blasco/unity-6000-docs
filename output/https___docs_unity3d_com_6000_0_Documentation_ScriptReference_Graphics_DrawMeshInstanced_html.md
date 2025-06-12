* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstanced.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawMeshInstanced
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
public static void DrawMeshInstanced([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, Matrix4x4[] matrices, int count = matrices.Length, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows = ShadowCastingMode.On, bool receiveShadows = true, int layer = 0, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = null, [Rendering.LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) lightProbeUsage = LightProbeUsage.BlendProbes, [LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) lightProbeProxyVolume = null); 
## Declaration
public static void DrawMeshInstanced([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, List<Matrix4x4> matrices, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows = ShadowCastingMode.On, bool receiveShadows = true, int layer = 0, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = null, [Rendering.LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) lightProbeUsage = LightProbeUsage.BlendProbes, [LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) lightProbeProxyVolume = null); 
### Parameters
Parameter | Description  
---|---  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to draw.  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
matrices | The array of object transformation matrices.  
count | The number of instances to be drawn.  
properties | Additional material properties to apply. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
castShadows | Determines whether the Meshes should cast shadows.  
receiveShadows | Determines whether the Meshes should receive shadows.  
layer |  [Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) to use.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be drawn in the given Camera only.  
lightProbeUsage |  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) for the instances.  
### Description
Draws the same mesh multiple times using GPU instancing.
Similar to [Graphics.DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html), this function draws meshes for one frame without the overhead of creating unnecessary game objects. This function is now obsolete. Use [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html) instead. Use this function in situations where you want to draw the same mesh for a particular amount of times using an instanced shader. Unity culls and sorts instanced Meshes as a group. It creates an axis-aligned bounding box that contains all the Meshes, calculates the center point, then uses this information to cull and sort the Mesh instances. Note that after culling and sorting the combined instances, Unity does not further cull individual instances by the view frustum or baked occluders. It also does not sort individual instances for transparency or depth efficiency.  
  
The transformation matrix of each instance of the mesh should be packed into the `matrices` array. You can specify the number of instances to draw, or by default it is the length of the `matrices` array. Other per-instance data, if required by the shader, should be provided by creating arrays on the MaterialPropertyBlock argument using [SetFloatArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetFloatArray.html), [SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetVectorArray.html) and [SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetMatrixArray.html).  
  
To render the instances with light probes, provide the light probe data via the MaterialPropertyBlock and specify `lightProbeUsage` with [LightProbeUsage.CustomProvided](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.CustomProvided.html). Check [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) for the details.  
  
Note: You can only draw a maximum of 1023 instances at once.  
  
InvalidOperationException will be thrown if the material doesn't have [Material.enableInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enableInstancing.html) set to true, or the current platform doesn't support this API (i.e. if GPU instancing is not available). See [SystemInfo.supportsInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInstancing.html).  
  
Additional resources: [Graphics.DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html).
* * *
