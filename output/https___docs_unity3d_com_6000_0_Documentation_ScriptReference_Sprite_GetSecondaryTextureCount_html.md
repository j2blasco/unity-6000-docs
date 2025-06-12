* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetSecondaryTextureCount.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).GetSecondaryTextureCount
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
public int GetSecondaryTextureCount(); 
### Returns
**int** Returns the number of Secondary Textures that the Sprite is using. 
### Description
Gets the number of Secondary Textures that the Sprite is using.
```
using UnityEngine;  
  
// Create a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) with Secondary Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) properties and retrieves the total number of
// Secondary Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) properties the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) has.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(64, 64);
        var secondaryTexture1 = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(64, 64);
        var secondaryTexture2 = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(64, 64);
        var secondaryTexture3 = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(64, 64);
        var secondarySpriteTexture = new[]
        {
            new SecondarySpriteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html)()
            {
                name = "_SecondaryTexture1",
                texture = secondaryTexture1
            },
            new SecondarySpriteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html)()
            {
                name = "_SecondaryTexture2",
                texture = secondaryTexture2
            },
            new SecondarySpriteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html)()
            {
                name = "_SecondaryTexture3",
                texture = secondaryTexture3
            }
        };  
  
        var sprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(texture, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, texture.width, texture.height), Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), 100, 0, SpriteMeshType.FullRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.FullRect.html), Vector4.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-zero.html), false, secondarySpriteTexture);
        int spriteSecondaryTextureCount = sprite.GetSecondaryTextureCount();
        // This will print 3 since there are 3 Secondary Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) properties in the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).
        print(spriteSecondaryTextureCount);
    }
}

```

* * *
