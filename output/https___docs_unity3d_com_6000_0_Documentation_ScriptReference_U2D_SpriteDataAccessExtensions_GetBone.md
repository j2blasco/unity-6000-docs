* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetBones.html

#  [SpriteDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html).GetBones
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
public static SpriteBone[] GetBones([Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite); 
### Parameters
Parameter | Description  
---|---  
sprite | The sprite to get the list of SpriteBone from.  
### Returns
**SpriteBone[]** An array of SpriteBone that belongs to this Sprite. 
### Description
Returns a list of SpriteBone in this Sprite.
SpriteBone is a richer set of information about the bind pose that this Sprite contains. It is useful for reconstructing the runtime skeleton for this Sprite and perform various other operations like resolving the bone path. It is via information in SpriteBone that the system knows if a sprite could be bound to a specific hierarchy.
* * *
