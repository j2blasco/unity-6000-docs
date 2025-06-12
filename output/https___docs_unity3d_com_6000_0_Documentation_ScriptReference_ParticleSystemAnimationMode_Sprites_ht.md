* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationMode.Sprites.html

#  [ParticleSystemAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationMode.html).Sprites
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
Use a list of sprites to construct a sequence of animation frames.
Defines the sprites that are added to Texture Sheet Animation.  
  
Additional resources: [ParticleSystemAnimationMode.Grid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationMode.Grid.html)
```
using UnityEngine;  
  
// A particle sprite example.
// The gameobject this script is attached to must have the
// ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) attached.  The TextureSheetAnimation mode
// is set to Sprites.  This script adds a single texture to
// the ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex;
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite;  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        sprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(tex, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0.0f, 0.0f, tex.width, tex.height), Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html));  
  
        var textureSheetAnimation = ps.textureSheetAnimation;
        textureSheetAnimation.enabled = true;
        textureSheetAnimation.mode = ParticleSystemAnimationMode.Sprites[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationMode.Sprites.html);
        textureSheetAnimation.AddSprite(sprite);
    }
}

```

* * *
