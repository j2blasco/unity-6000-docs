* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-alphaIsTransparency.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).alphaIsTransparency
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
alphaIsTransparency; 
### Description
If the alpha channel of your texture represents transparency, enable this property to dilate the color channels of visible texels into fully transparent areas. This effectively adds padding around transparent areas that prevents filtering artifacts from forming on their edges. Unity does not support this property for HDR textures.  
  
This property makes the color data of invisible texels undefined. Disable this property to preserve invisible texels' original color data.
* * *
