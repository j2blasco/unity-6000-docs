* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isDataSRGB.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).isDataSRGB
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
isDataSRGB; 
### Description
Returns `true` if the texture pixel data is in sRGB color space (Read Only).
This property describes whether the texture pixel data on disk, CPU memory, and GPU memory is in sRGB color space. Use [GraphicsFormatUtility.IsSRGBFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUtility.IsSRGBFormat.html) with [Texture.graphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsFormat.html) to check the GPU texture color space, which determines how Unity samples the pixel data on the GPU.  
  
Additional resources: [Linear and Gamma rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html).
* * *
