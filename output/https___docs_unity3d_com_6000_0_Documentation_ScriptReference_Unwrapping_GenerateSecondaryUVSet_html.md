* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unwrapping.GenerateSecondaryUVSet.html

#  [Unwrapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unwrapping.html).GenerateSecondaryUVSet
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
public static bool GenerateSecondaryUVSet([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) src); 
## Declaration
public static bool GenerateSecondaryUVSet([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) src, [UnwrapParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnwrapParam.html) settings); 
### Parameters
Parameter | Description  
---|---  
src | The Mesh to update.  
settings | Settings that configure the calculation.  
### Returns
**bool** Returns true if the calculation succeeded. Otherwise, returns false. 
### Description
Compute a unique UV layout for a Mesh, and store it in [Mesh.uv2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv2.html).
When you import a model asset, you can instruct Unity to compute a lightmap UV layout for it using [[ModelImporter-generateSecondaryUV]] or the [Model Import Settings Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html). This function allows you to do the same to procedurally generated meshes.  
  
If this process requires multiple UV charts to flatten the the mesh, the mesh might contain more vertices than before. If the mesh uses 16-bit indices (see [Mesh.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexFormat.html)) and the process would result in more vertices than are possible to use with 16-bit indices, this function fails and returns `false`.  
  
Additional resources: [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) class, [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) class, [Generating Lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-GeneratingLightmappingUVs.html).
* * *
