* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.SpriteUtility.GetSpriteTexture.html

#  [SpriteUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.SpriteUtility.html).GetSpriteTexture
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetSpriteTexture([Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite, bool getAtlasData); 
### Parameters
Parameter | Description  
---|---  
getAtlasData | If [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) is packed, it is possible to access data as if it was on the atlas texture.  
### Description
Returns the generated [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) texture. If [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) is packed, it is possible to query for both source and atlas textures.
Note that the sprite atlas cache must be up to date for this API to return valid data.
* * *
