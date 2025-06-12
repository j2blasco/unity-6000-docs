* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).Create
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
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot, float pixelsPerUnit, uint extrude); 
## Declaration
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot, float pixelsPerUnit, uint extrude, [SpriteMeshType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.html) meshType); 
## Declaration
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot, float pixelsPerUnit, uint extrude, [SpriteMeshType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.html) meshType, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) border, bool generateFallbackPhysicsShape); 
## Declaration
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot, float pixelsPerUnit, uint extrude, [SpriteMeshType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.html) meshType, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) border); 
## Declaration
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot); 
## Declaration
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot, float pixelsPerUnit); 
## Declaration
public static [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Create([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivot, float pixelsPerUnit, uint extrude, [SpriteMeshType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.html) meshType, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) border, bool generateFallbackPhysicsShape, SecondarySpriteTexture[] secondaryTextures); 
### Parameters
Parameter | Description  
---|---  
texture | The Texture to obtain the Sprite graphic from.   
rect | The rectangular section of the Texture to use for the Sprite.   
pivot | The Sprite's pivot point relative to its graphic rectangle.   
pixelsPerUnit | The number of pixels in the Sprite that correspond to one unit in world space.   
extrude | The amount by which the Sprite mesh should be expanded outwards.   
meshType | The type of mesh that is generated for the Sprite.   
border | The border sizes of the Sprite (X=left, Y=bottom, Z=right, W=top).   
generateFallbackPhysicsShape | Whether to generate a default physics shape for the Sprite.  
secondaryTextures | The Secondary Texture properties to be used by the created Sprite.   
### Description
Create a new Sprite object.
[Sprite.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html) creates a new [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) which can be used in game applications. A Texture needs to be loaded and assigned to [Sprite.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html) in order to control how the new [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) will look. In the script example below a new Sprite is displayed when the button is pressed. The new Sprite is created in Start.  
  
The second argument `rect` defines the sub-texture used. The `rect` argument is defined in pixels of the Texture. A Rect(50.0f, 10.0f, 200.0f, 140.0f) would create a left to right range from 50.0f to 50.0f + 200.0f = 250.0f. The bottom to top range would be 10.0f to 10.0f + 140.0f = 150.0f. The third argument `pivot` determines what becomes the center of the [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html). This is a `Vector2` relative to the `rect` where Vector2(0.0f, 0.0f) is the bottom left and Vector2(1.0f, 1.0f) is the top right. The [pixelsPerUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-pixelsPerUnit.html) value controls the size of the Sprite. Reducing this below 100 pixels per world increases the size of the Sprite. The `extrude` value defines the number of pixels which surround the `Sprite`. This is useful if the [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) is included in an atlas. `meshType` selects whether `FullRect` or `Tight` is used. Finally `border` determines the slicing of the Sprite and is usually used to define Sprite tiling behaviour. The values are in pixel units.  
  
Additional resources: [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) class.
```
// Create a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) at startup.
// Assign a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) when the button is pressed.  
  
using UnityEngine;  
  
public class SpriteCreate : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex;
    private Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) mySprite;
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sr;  
  
    void Awake()
    {
        sr = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>() as SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html);
        sr.color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.9f, 1.0f);  
  
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.5f, 1.5f, 0.0f);
    }  
  
    void Start()
    {
        mySprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(tex, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0.0f, 0.0f, tex.width, tex.height), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.5f, 0.5f), 100.0f);
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 30), "Add sprite"))
        {
            sr.sprite = mySprite;
        }
    }
}

```

The following code example shows how to create a Sprite at startup with Secondary Texture properties.
```
using UnityEngine;  
  
// Create a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) at startup with Secondary Textures properties  
  
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
    }
}

```

* * *
