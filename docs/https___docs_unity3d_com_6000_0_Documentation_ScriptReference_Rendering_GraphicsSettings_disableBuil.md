* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-disableBuiltinCustomRenderTextureUpdate.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).disableBuiltinCustomRenderTextureUpdate
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
disableBuiltinCustomRenderTextureUpdate; 
### Description
Disables the built-in update loop for Custom Render Textures, so that you can write your own update loop.
When this is set to true, Unity does not call internally CustomRenderTextureManager.Update, which in turn means that Unity does not call [CustomRenderTexture.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Update.html) on CustomRenderTextures. You can then implement your own update loop for CustomRenderTextures using CommandBuffers.  
  
When this is set to false, Unity calls CustomRenderTextureManager.Update, which in turn calls [CustomRenderTexture.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Update.html) on CustomRenderTextures. This is the default behavior.
* * *
