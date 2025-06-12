* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-useMipMap.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).useMipMap
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
useMipMap; 
### Description
Render texture has mipmaps when this flag is set.
When set to `true`, rendering into this render texture will create and generate mipmap levels. By default render textures don't have mipmaps. This flag can be used only on render textures that have power-of-two size.  
  
By default the mipmaps will be automatically generated. If you want to render into texture mip levels manually, set [autoGenerateMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-autoGenerateMips.html) to false.  
  
Additional resources: [autoGenerateMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-autoGenerateMips.html), [GenerateMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GenerateMips.html).
* * *
