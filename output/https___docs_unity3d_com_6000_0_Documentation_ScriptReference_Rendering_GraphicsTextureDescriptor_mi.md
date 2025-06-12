* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-mipCount.html

#  [GraphicsTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor.html).mipCount
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
mipCount; 
### Description
The number of mipmap levels in this GraphicsTexture.
The value includes the base level, so it must always be 1 or more. Note that a GraphicsTexture represents what is uploaded to the GPU, so this value may differ from [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html) depending on the values of [Texture2D.activeMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-activeMipmapLimit.html) and [Texture2D.streamingMipmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmaps.html).  
  
If the [GraphicsTextureDescriptor.format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-format.html) is a depth-only format, then mipCount is ignored. 
* * *
