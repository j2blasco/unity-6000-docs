* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.SetIsVariant.html

#  [SpriteAtlasExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.html).SetIsVariant
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
## Declaration
public static void SetIsVariant([U2D.SpriteAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) spriteAtlas, bool value); 
### Description
Sets whether this Sprite Atlas is a variant or not.
A Variant will not repack a new texture from the packable list. Instead, it will duplicate the master's packed texture and downscale it according to SpriteAtlasExtensions.SetVariantMultiplier and save this scaled texture.  
  
Additional resources: [SpriteAtlasExtensions.SetMasterAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.SetMasterAtlas.html).
* * *
