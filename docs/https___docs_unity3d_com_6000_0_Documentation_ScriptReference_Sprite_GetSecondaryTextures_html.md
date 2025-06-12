* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetSecondaryTextures.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).GetSecondaryTextures
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
public int GetSecondaryTextures(SecondarySpriteTexture[] secondaryTexture); 
### Parameters
Parameter | Description  
---|---  
secondaryTexture | The array of [SecondarySpriteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html) to contain the Secondary Textures properties used by the Sprite.  
### Returns
**int** Returns the number of Secondary Textures properties retrieved. 
### Description
Retrieves an array of [SecondarySpriteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html) used by the Sprite.
If the size of the arrays passed in as parameters are less than the number of [SecondarySpriteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html) used by the sprite, the arrays will not be resized and the results will be limited.  
  
If the size of the arrays passed in as parameters are bigger than the number of [SecondarySpriteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html) used by the sprite, the number of elements used in the array will be indicated by the return value of the method. 
```
using UnityEngine;  
  
// Create a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) with Secondary Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) properties and retrieves the
// Secondary Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) properties with various input parameter array length.  
  
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
        var secondarySpriteTextureResult = new SecondarySpriteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html)[2];
        var resultCount = sprite.GetSecondaryTextures(secondarySpriteTextureResult);
        // There are 3 Secondary Textures, but the array is only size of 2, so the entire array is used
        print(resultCount);
        for (var i = 0; i < resultCount; ++i)
        {
            // This will print
            //_SecondaryTexture1
            //_SecondaryTexture2
            print(secondarySpriteTextureResult[i].name);
        }  
  
        secondarySpriteTextureResult = new SecondarySpriteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html)[4];
        resultCount = sprite.GetSecondaryTextures(secondarySpriteTextureResult);
        // There are 3 Secondary Textures, but the array is only size of 4, so only 3 will be used
        print(resultCount);
        for (var i = 0; i < resultCount; ++i)
        {
            // This will print
            //_SecondaryTexture1
            //_SecondaryTexture2
            //_SecondaryTexture3
            print(secondarySpriteTextureResult[i].name);
        }
    }
}

```

* * *
