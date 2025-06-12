* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html

# GraphicsTexture
class in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Represents the view on a single texture resource that is uploaded to the graphics device.
A GraphicsTexture specifically represents the actual resource that a [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) object uploads to the GPU. A Texture may create several different GraphicsTextures in its lifetime (such as to represent different mipmap levels or the color and depth buffers in a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)) and will recreate GraphicsTextures when certain changes are made to the Texture (such as resizing). Use [Texture.graphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsTexture.html) to get a Texture's current GraphicsTexture.  
  
GraphicsTextures are useful for getting the current uploaded state of a texture on the graphics device. [GraphicsTextureDescriptor.mipCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-mipCount.html) represents only the uploaded mipmap levels when using texture streaming or [mipmap limit settings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-activeMipmapLimit.html). Consequently, [GraphicsTextureDescriptor.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-width.html) and [GraphicsTextureDescriptor.height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-height.html) represent the width and height of the maximum uploaded mipmap level.  
  
GraphicsTextures are purely run-time objects and cannot be saved as assets.  
  
To use a GraphicsTexture as a render target, it must have [GraphicsTextureDescriptorFlags.RenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.RenderTarget.html) enabled in its [GraphicsTextureDescriptor.flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-flags.html).  
  
Additional resources: [Texture.graphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsTexture.html), [Graphics.SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html).
### Static Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture-active.html) | Currently active graphics texture.  
### Properties
Property | Description  
---|---  
[descriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture-descriptor.html) | Contains all the information Unity uses to create a GraphicsTexture.  
[state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture-state.html) | The current state of a GraphicsTexture.  
* * *
