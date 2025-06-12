* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html

#  [GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html).Raw
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
GraphicsBuffer can be used as a raw byte-address buffer.
In HLSL shaders, this maps to `ByteAddressBuffer` or `RWByteAddressBuffer`. The underlying DirectX 11 format for shader access is typeless R32.  
  
See Microsoft's HLSL documentation on [ByteAddressBuffer](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-byteaddressbuffer) and [RWByteAddressBuffer](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwbyteaddressbuffer).  
  
Additional resources: [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html), [Mesh.vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferTarget.html), [Mesh.indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html).
* * *
