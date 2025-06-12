* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.OverrideGeometry.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).OverrideGeometry
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
public void OverrideGeometry(Vector2[] vertices, ushort[] triangles); 
### Parameters
Parameter | Description  
---|---  
vertices | Array of vertex positions in Sprite Rect space.  
triangles | Array of sprite mesh triangle indices.  
### Description
Sets up new Sprite geometry.
Vertex positions are in [Sprite.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html) space meaning from [Rect.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-zero.html) to [Rect.size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-size.html). Pivot offset and transformation to unit space is done automatically.  
  
The size of the triangle array must always be a multiple of 3. The vertices connected to the triangle can be shared by simply indexing into the same vertex.  
  
Sprite UVs are calculated automatically by mapping the provided geometry onto the Sprite's Texture.  
  
The Sprite's mesh type will be changed to [SpriteMeshType.Tight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.Tight.html) when the API is called.  
  
Additional resources: [Sprite.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html).  
  
The script example below shows an example on how the API can be used. 
```
// Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)'s geometry between a triangle and a quad.
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) m_SpriteRenderer;
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) m_ButtonPos;
    void Start()
    {
        m_SpriteRenderer = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        // Create a blank Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) and Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) to override later on.
        var texture2D = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(64, 64);
        m_SpriteRenderer.sprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(texture2D, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, texture2D.width, texture2D.height), Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), 64);  
  
        m_ButtonPos = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10.0f, 10.0f, 200.0f, 30.0f);
    }  
  
    // Use OverrideGeometry to switch the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)'s mesh to a triangle or quad
    void ChangeSprite()
    {
        Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) o = m_SpriteRenderer.sprite;
        if (o.triangles.Length != 3)
        {
            var sv = new[]
            {
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0),
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(o.textureRect.width, 0),
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(o.textureRect.width * 0.5f, o.textureRect.height),
            };
            var indices = new ushort[] { 0, 1, 2 };
            o.OverrideGeometry(sv, indices);
        }
        else
        {
            var sv = new[]
            {
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0),
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(o.textureRect.width, 0),
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(o.textureRect.width, o.textureRect.height),
                new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, o.textureRect.height),
            };
            var indices = new ushort[] { 0, 1, 2, 2, 3, 0 };
            o.OverrideGeometry(sv, indices);
        }
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(m_ButtonPos, "Perform OverrideGeometry"))
            ChangeSprite();
    }
}

```

* * *
