* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetUVs.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetUVs
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public void SetUVs(int channel, Vector2[] uvs); 
## Declaration
public void SetUVs(int channel, Vector3[] uvs); 
## Declaration
public void SetUVs(int channel, Vector4[] uvs); 
## Declaration
public void SetUVs(int channel, List<Vector2> uvs); 
## Declaration
public void SetUVs(int channel, List<Vector3> uvs); 
## Declaration
public void SetUVs(int channel, List<Vector4> uvs); 
## Declaration
public void SetUVs(int channel, NativeArray<T> uvs); 
### Parameters
Parameter | Description  
---|---  
channel | The channel, in [0..7] range.  
uvs | The UV data to set.  
### Description
Sets the texture coordinates (UVs) stored in a given channel.
Sets the UVs as a List of either [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html), [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html), or [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html). 2 dimensional (Vector2) data is the most common use case, but 3 or 4 dimensional data is sometimes used for special shader effects.  
  
Unity stores UVs in 0-1 space. [0,0] represents the bottom-left corner of the texture, and [1,1] represents the top-right. Values are not clamped; you can use values below 0 and above 1 if needed.  
  
A `channel` value of 0 corresponds to the channel that is commonly called "UV0", and maps to the shader semantic `TEXCOORD0`. A `channel` value of 1 returns the channel that is commonly called "UV1", and maps to the shader semantic `TEXCOORD1`. This continues up to and including a `channel` value of 7.  
  
By default, Unity uses the first channel (UV0) to store UVs for regular textures such as diffuse maps and specular maps. Unity can use the second channel (UV1) to store baked lightmap UVs, and the third channel (UV2) to store input data for real-time lightmap UVs. For more information on lightmap UVs and how Unity uses these channels, [Lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs.html).  
  
**Note:** You can also access UV data using [uv](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv.html) for UV0, [uv2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv2.html) for UV1, [uv3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv3.html) for UV2, and so on up to [uv8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv8.html). However, this older way of working is not recommended; the properties are less user-friendly than this function and [GetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVs.html), and they also cause heap allocations.  
  
Additional resources: [GetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVs.html).
* * *
## Declaration
public void SetUVs(int channel, Vector2[] uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetUVs(int channel, Vector3[] uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetUVs(int channel, Vector4[] uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetUVs(int channel, List<Vector2> uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetUVs(int channel, List<Vector3> uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetUVs(int channel, List<Vector4> uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetUVs(int channel, NativeArray<T> uvs, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
### Parameters
Parameter | Description  
---|---  
channel | The UV channel, in [0..7] range.  
uvs | UVs to set for the given index.  
start | Index of the first element to take from the input array.  
length | Number of elements to take from the input array.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Sets the UVs of the Mesh, using a part of the input array.
This method behaves as if you called SetUVs with an array that is a slice of the whole array, starting at `start` index and being of a given `length`. The resulting Mesh has `length` amount of vertices.
* * *
