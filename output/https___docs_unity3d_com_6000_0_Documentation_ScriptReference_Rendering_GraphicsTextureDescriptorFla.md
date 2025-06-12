* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.RandomWriteTarget.html

#  [GraphicsTextureDescriptorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.html).RandomWriteTarget
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
Allows random write access into this [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) on Shader Model 5.0 level shaders.
Allows Shader Model 5.0 level pixel or compute shaders to write into arbitrary locations on this texture, called "unordered access views" in [UsingDX11GL3Features](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html). Note that this flag does nothing if [GraphicsTextureDescriptorFlags.RenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.RenderTarget.html) is not also set. [GraphicsTextureDescriptor.numSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-numSamples.html) must be 1, as random write access is not compatible with anti-aliasing.  
  
Additional resources: [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html).
* * *
