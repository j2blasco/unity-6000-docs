* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.UpdateExternalTexture.html

#  [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).UpdateExternalTexture
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
public void UpdateExternalTexture(IntPtr nativeTexture); 
### Parameters
Parameter | Description  
---|---  
nativeTexture | Native cubemap texture object.  
### Description
Updates Unity cubemap to use different native cubemap texture object.
This method is mostly useful for [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html) that create platform specific cubemap texture objects outside of Unity, and need to use these cubemaps in Unity scenes. For a cubemap created with [CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.CreateExternalTexture.html), this method switches to another underlying cubemap texture object if/when it changes.  
  
The actual contents of the native texture object will vary based on the native graphics API in use. For example, if DirectX is in use, the native texture object will need to be a pointer to an ID3D11ShaderResourceView. If OpenGL/OpenGL ES is in use, the native texture object should be a GLuint. If Metal, then the native texture object should be a MTLTexture.  
  
Additional resources: [CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.CreateExternalTexture.html).
* * *
