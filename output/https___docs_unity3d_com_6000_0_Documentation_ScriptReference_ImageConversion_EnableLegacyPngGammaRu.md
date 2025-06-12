* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EnableLegacyPngGammaRuntimeLoadBehavior.html

#  [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html).EnableLegacyPngGammaRuntimeLoadBehavior
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
EnableLegacyPngGammaRuntimeLoadBehavior; 
### Description
Enables legacy PNG runtime import behavior.
In previous versions of Unity, texture data from all PNG textures containing a gAMA block was returned in gamma 2.0 space. If you want to retain this old behavior, for example when working with older projects that dynamically load textures using [ImageConversion.LoadImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.LoadImage.html) or `Texture2D.LoadImage`, set this flag to `true`.
* * *
