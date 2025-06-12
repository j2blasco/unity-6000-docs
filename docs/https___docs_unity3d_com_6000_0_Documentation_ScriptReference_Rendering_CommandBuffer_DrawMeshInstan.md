* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawMeshInstanced.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).DrawMeshInstanced
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
public void DrawMeshInstanced([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, Matrix4x4[] matrices, int count, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties); 
## Declaration
public void DrawMeshInstanced([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, Matrix4x4[] matrices, int count); 
## Declaration
public void DrawMeshInstanced([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, Matrix4x4[] matrices); 
### Parameters
Parameter | Description  
---|---  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to draw.  
submeshIndex | Which subset of the mesh to draw. This only applies to meshes that are composed of several materials.  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
shaderPass | Which pass of the shader to use, or -1 which renders all passes.  
matrices | The array of object transformation matrices.  
count | The number of instances to be drawn.  
properties | Additional Material properties to apply onto the Material just before this Mesh is drawn. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
### Description
Adds a "draw mesh with instancing" command.  
  
The mesh will be just drawn once, it won't be per-pixel lit and will not cast or receive realtime shadows.  
  
The command will not immediately fail and throw an exception if [Material.enableInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enableInstancing.html) is false, but it will log an error and skips rendering each time the command is being executed if such a condition is detected.  
  
InvalidOperationException will be thrown if the current platform doesn't support this API (i.e. if GPU instancing is not available). See [SystemInfo.supportsInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInstancing.html).
Additional resources: [DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawMesh.html), [Graphics.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstanced.html), [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).
* * *
