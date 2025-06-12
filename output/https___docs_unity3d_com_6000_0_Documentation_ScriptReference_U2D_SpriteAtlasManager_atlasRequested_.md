* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRequested.html

#  [SpriteAtlasManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager.html).atlasRequested
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
Trigger when any [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) was bound to [SpriteAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) but couldn't locate the atlas asset during runtime.
This usually means the sprite was packed to an atlas which is not included in build  
  
This callback does not expect an immediate response from the user. Instead, it passes on a System.Action. The user can load the atlas object later and use this System.Action to pass back the loaded atlas.
```
using UnityEngine;
using UnityEngine.U2D;  
  
public class AtlasLoader : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnEnable()
    {
        SpriteAtlasManager.atlasRequested[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRequested.html) += RequestAtlas;
    }  
  
    void OnDisable()
    {
        SpriteAtlasManager.atlasRequested[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRequested.html) -= RequestAtlas;
    }  
  
    void RequestAtlas(string tag, System.Action<SpriteAtlas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html)> callback)
    {
        var sa = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)<SpriteAtlas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html)>(tag);
        callback(sa);
    }
}

```

Additional resources: U2D.SpriteAtlasManager.RequestAtlasCallback.
* * *
