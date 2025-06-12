* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRegistered.html

#  [SpriteAtlasManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager.html).atlasRegistered
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
Trigger when a [SpriteAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) is registered via invoking the callback in [SpriteAtlasManager.atlasRequested](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRequested.html).
```
using UnityEngine;
using UnityEngine.U2D;  
  
public class AtlasRegistrationListener : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnEnable()
    {
        SpriteAtlasManager.atlasRegistered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRegistered.html) += AtlasRegistered;
    }  
  
    void OnDisable()
    {
        SpriteAtlasManager.atlasRegistered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRegistered.html) -= AtlasRegistered;
    }  
  
    void AtlasRegistered(SpriteAtlas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) spriteAtlas)
    {
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Registered {0}.", spriteAtlas.name);
    }
}

```

Additional resources: [SpriteAtlasManager.atlasRegistered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager-atlasRegistered.html).
* * *
