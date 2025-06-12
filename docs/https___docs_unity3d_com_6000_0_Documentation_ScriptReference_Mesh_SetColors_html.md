* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetColors.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetColors
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
public void SetColors(Color32[] inColors); 
## Declaration
public void SetColors(Color[] inColors); 
## Declaration
public void SetColors(List<Color32> inColors); 
## Declaration
public void SetColors(List<Color> inColors); 
## Declaration
public void SetColors(NativeArray<T> inColors); 
### Parameters
Parameter | Description  
---|---  
inColors | Per-vertex colors.  
### Description
Set the per-vertex colors of the Mesh.
Unity internally stores Mesh data in the format matching the data you supply. For example, if you pass a [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) array Unity will store each color in 4 bytes (low precision, 0..1 range); whereas if you pass a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) array, Unity stores each color in 16 bytes (full 32 bit float per color channel).  
  
If you use a `List`, Unity copies the values. If you change the `List`, the Mesh colors won't change unless you call `Mesh.SetColors` again.  
  
Additional resources: [colors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors.html), [colors32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors32.html) properties.
* * *
## Declaration
public void SetColors(Color32[] inColors, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetColors(Color[] inColors, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetColors(List<Color32> inColors, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetColors(List<Color> inColors, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetColors(NativeArray<T> inColors, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
### Parameters
Parameter | Description  
---|---  
inColors | Per-vertex colors.  
start | Index of the first element to take from the input array.  
length | Number of elements to take from the input array.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Sets the per-vertex colors of the Mesh, using a part of the input array.
This method behaves as if you called SetColors with an array that is a slice of the whole array, starting at `start` index and being of a given `length`. The resulting Mesh has `length` amount of vertices.
* * *
