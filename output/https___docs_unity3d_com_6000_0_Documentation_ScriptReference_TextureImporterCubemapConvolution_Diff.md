* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterCubemapConvolution.Diffuse.html

#  [TextureImporterCubemapConvolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterCubemapConvolution.html).Diffuse
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
Diffuse convolution (aka irradiance [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html)).
Each pixel of this [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) texture is replaced with the cosine-weighted integral of the corresponding hemisphere of incident illumination. In simpler terms texture is nicely blurred.  
  
Can be used to light diffuse object by sampling with its surface normal.  
  
Additional resources: [TextureImporterSettings.cubemapConvolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-cubemapConvolution.html).
* * *
