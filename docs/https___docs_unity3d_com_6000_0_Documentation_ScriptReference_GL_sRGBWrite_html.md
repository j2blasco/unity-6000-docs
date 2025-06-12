* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-sRGBWrite.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).sRGBWrite
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
sRGBWrite; 
### Description
Controls whether Linear-to-sRGB color conversion is performed while rendering.
This property is only relevant when [Linear Color Space](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html) rendering is used. Typically when linear color space is used, non-HDR render textures are treated as sRGB data (i.e. "regular colors"), and fragment shaders outputs are treated as linear color values. So by default the fragment shader color value is converted into sRGB.  
  
However, if you know your fragment shader already outputs sRGB color value for some reason and want to temporarily turn off Linear-to-sRGB write color conversion, you can use this property to achieve that.  
  
Note that the ability to turn off sRGB writes is not supported on all platforms (typically mobile "tile based" GPUs can not do it), so this is considered a "feature of last resort". Usually it is better to create [RenderTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) with appropriate color space flag (linear vs sRGB) and not switch the conversions in the middle of rendering into it.  
  
Additional resources: [Linear Color Space](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html), [RenderTexture.sRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-sRGB.html), [RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html), [PlayerSettings.colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-colorSpace.html).
* * *
