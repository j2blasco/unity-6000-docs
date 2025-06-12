* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager.html

# SpriteAtlasManager
class in UnityEngine.U2D
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Manages [SpriteAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) during runtime.
A [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) can be loaded without referencing any Sprite Atlas, thus having no texture. It will be invisible until the user registers an atlas to the Sprite by listening to the [SpriteAtlasManager.atlasRequested](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRequested.html) callback. When triggered, it will pass in the atlas tag and a System.Action which will take in an atlas object.
### Events
Event | Description  
---|---  
[atlasRegistered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRegistered.html) | Trigger when a SpriteAtlas is registered via invoking the callback in SpriteAtlasManager.atlasRequested.  
[atlasRequested](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRequested.html) | Trigger when any Sprite was bound to SpriteAtlas but couldn't locate the atlas asset during runtime.  
* * *
