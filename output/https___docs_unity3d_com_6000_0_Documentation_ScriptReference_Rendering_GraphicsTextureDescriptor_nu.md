* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor-numSamples.html

#  [GraphicsTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor.html).numSamples
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
numSamples; 
### Description
The number of samples per pixel in the GraphicsTexture.
Must always be 1 or more. A value greater than 1 indicates that the GraphicsTexture is using multi-sampled anti-aliasing, which requires [GraphicsTextureDescriptorFlags.RenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.RenderTarget.html) to be set. Anti-aliasing is not compatible with [GraphicsTextureDescriptorFlags.RandomWriteTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.RandomWriteTarget.html).
* * *
