* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.CreateExternalTexture.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).CreateExternalTexture
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) CreateExternalTexture(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format, bool mipChain, bool linear, IntPtr nativeTex); 
### Parameters
Parameter | Description  
---|---  
nativeTex | Native 2D texture object.  
width | Width of texture in pixels.  
height | Height of texture in pixels.  
format | Format of underlying texture object.  
mipmap | Does the texture have mipmaps?  
linear | Is texture using linear color space?  
### Description
Creates a Unity Texture out of an externally created native texture object.
This function is mostly useful for [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html) that create platform specific texture objects outside of Unity, and need to use these textures in Unity Scenes. It is also possible to create a texture in Unity and get a pointer to the underlying platform representation; see [Texture.GetNativeTexturePtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GetNativeTexturePtr.html).  
  
Parameters passed to CreateExternalTexture should match what the texture actually is; and the underlying texture should be 2D.  
  
For **Direct3D** -like devices, the `nativeTex` parameter is a pointer to the underlying **Direct3D** base type, from which a texture can be created. They can be:  
  
• **D3D11** : `ID3D11ShaderResourceView*` or `ID3D11Texture2D*`  
• **D3D12** : `ID3D12Texture2D*`  
  
For **OpenGL** /**OpenGL ES** , the `nativeTex` parameter is a `GLuint`.  
  
For **Metal** , the `nativeTex` parameter is an `id<MTLTexture>`.  
  
For **Vulkan** , the `nativeTex` parameter is a `VkImage*`.  
  
Additional resources: [UpdateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.UpdateExternalTexture.html), [Texture.GetNativeTexturePtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GetNativeTexturePtr.html).
* * *
