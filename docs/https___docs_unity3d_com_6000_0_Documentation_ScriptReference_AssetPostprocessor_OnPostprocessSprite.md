* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessSprites.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessSprites(Texture2D, Sprite[])
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
Add this function to a subclass to get a notification when an texture of sprite(s) has completed importing.
For Multiple sprite-mode assets each sprite will be passed in the second argument as an array of sprites.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPostprocessSprites(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)[] sprites)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Sprites: " + sprites.Length);
    }  
  
    void OnPostprocessTexture(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html): (" + texture.width + "x" + texture.height + ")");
    }
}

```

* * *
