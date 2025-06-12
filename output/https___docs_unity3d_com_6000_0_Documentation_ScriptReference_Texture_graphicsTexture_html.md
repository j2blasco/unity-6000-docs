* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsTexture.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).graphicsTexture
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
[Rendering.GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) graphicsTexture; 
### Description
[GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) that represents the texture resource uploaded to the graphics device (Read Only).
This returns the current GraphicsTexture object corresponding to the Texture.  
  
For [RenderTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), this returns the `GraphicsTexture` object that represents the color buffer. If the `RenderTexture` is depth-only and has a [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) of `None`, this returns the `GraphicsTexture` object representing the depth buffer.  
  
Note: When you use the Unity APIs to reinitialize the properties of a Texture object, or when a different mipmap level is streamed in, it changes the underlying GraphicsTexture object. Rather than caching the value, get `Texture.graphicsTexture` again to retrieve the new GraphicsTexture.
* * *
