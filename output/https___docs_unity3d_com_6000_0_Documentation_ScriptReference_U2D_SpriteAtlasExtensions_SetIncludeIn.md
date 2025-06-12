* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.SetIncludeInBuild.html

#  [SpriteAtlasExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.html).SetIncludeInBuild
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
public static void SetIncludeInBuild([U2D.SpriteAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) spriteAtlas, bool value); 
### Description
Define if this sprite atlas's packed texture is included in the build with the [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) after packing is done.
Include this to ensure that the sprite refers to the atlas's packed texture at runtime.  
  
Conversely, the packed texture will not be in the build. It can be late bound to the sprite at runtime.
* * *
