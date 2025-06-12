* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.SetIsVariant.html

#  [SpriteAtlasAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.html).SetIsVariant
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
public void SetIsVariant(bool value); 
### Description
Sets whether this Sprite Atlas is a Variant or not.
A Variant does not repack a new Texture from the packable list. Instead, it duplicates the Master Atlas's packed Texture and downscale it by the SpriteAtlasExtensions.SetVariantMultiplier and saves this scaled Texture. Additional resources: [SpriteAtlasExtensions.SetMasterAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.SetMasterAtlas.html).
* * *
