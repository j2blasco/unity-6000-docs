* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTexture3DSize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).maxTexture3DSize
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
maxTexture3DSize; 
### Description
Maximum 3D texture size in pixels (Read Only).
The largest 3D texture width, height and depth that your graphics hardware supports.  
  
Unity only supports textures up to a size of 16384, even if `maxTexture3DSize` returns a larger size.  
  
You can only create a texture with the maximum size if you have enough memory. For example, to create a 3D texture with a size of 2048 in an uncompressed format such as [TextureFormat.RGBA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html), you need 32 gigabytes of memory because the amount of data is 4 bytes per pixel × 2048 x 2048 × 2048.  
  
Additional resources: [maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureSize.html), [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).
* * *
