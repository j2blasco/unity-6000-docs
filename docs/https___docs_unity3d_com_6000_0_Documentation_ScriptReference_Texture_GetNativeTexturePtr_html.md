* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GetNativeTexturePtr.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).GetNativeTexturePtr
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
public IntPtr GetNativeTexturePtr(); 
### Returns
**IntPtr** Pointer to an underlying graphics API Texture resource. 
### Description
Retrieve a native (underlying graphics API) pointer to the Texture resource.
Use this function to retrieve a pointer/handle corresponding to a particular Texture as it is represented on the native graphics API level. This can be used to enable Texture manipulation from [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).  
  
Note: When you use the Unity APIs to modify the pixel data of a Texture object, it changes the underlying graphics API native pointer. Call GetNativeTexturePtr to get the new native pointer.  
  
For specific platforms, Unity has the following specifications: 
  * On Direct3D-like devices, Unity returns a pointer to the base Texture type (`ID3D11Resource` on D3D11, `ID3D12Resource` on D3D12).
  * On OpenGL-like devices, the GL Texture "name" is returned; cast the pointer to an integer type to get it.
  * On Metal, Unity returns an `id<MTLTexture>` pointer.
  * On Vulkan, Unity returns an `VkImage` pointer.
  * On platforms that do not support native code plug-ins, this function always returns NULL.


Note that calling this function when using multi-threaded rendering will synchronize with the rendering thread (a slow operation), so best practice is to set up needed Texture pointers only at initialization time.  
  
Additional resources: [Native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html), [Texture2D.CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.CreateExternalTexture.html), [Cubemap.CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.CreateExternalTexture.html), [RenderTexture.GetNativeDepthBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetNativeDepthBufferPtr.html).
* * *
