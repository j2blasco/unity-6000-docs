* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-vertices.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).vertices
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
vertices; 
### Description
Returns a copy of the array containing Sprite mesh vertex positions. 
```
// Obtain the vertices from the script and modify the position of one of them. Use OverrideGeometry() for this.
//Attach this script to a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//To see the vertices changing, make sure you have your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) tab visible while in Play mode.
//Press the "Draw Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html)" Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) in the Game tab during Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html) to draw the shape. Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) back to the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) tab to see the shape.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) m_SpriteRenderer;
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) buttonPos1;
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) buttonPos2;  
  
    void Start()
    {
        m_SpriteRenderer = gameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        buttonPos1 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10.0f, 10.0f, 200.0f, 30.0f);
        buttonPos2 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10.0f, 50.0f, 200.0f, 30.0f);
    }  
  
    void OnGUI()
    {
        //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to show the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) triangles (in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) tab)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(buttonPos1, "Draw Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html)"))
            DrawDebug();
        //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to edit the vertices obtained from the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(buttonPos2, "Perform OverrideGeometry"))
            ChangeSprite();
    }  
  
    // Show the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) triangles
    void DrawDebug()
    {
        Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite = m_SpriteRenderer.sprite;  
  
        ushort[] triangles = sprite.triangles;
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] vertices = sprite.vertices;
        int a, b, c;  
  
        // draw the triangles using grabbed vertices
        for (int i = 0; i < triangles.Length; i = i + 3)
        {
            a = triangles[i];
            b = triangles[i + 1];
            c = triangles[i + 2];  
  
            //To see these you must view the game in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) tab while in Play mode
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(vertices[a], vertices[b], Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 100.0f);
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(vertices[b], vertices[c], Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 100.0f);
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(vertices[c], vertices[a], Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 100.0f);
        }
    }  
  
    // Edit the vertices obtained from the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).  Use OverrideGeometry to
    // submit the changes.
    void ChangeSprite()
    {
        //Fetch the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) and vertices from the SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)
        Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite = m_SpriteRenderer.sprite;
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] spriteVertices = sprite.vertices;  
  
        for (int i = 0; i < spriteVertices.Length; i++)
        {
            spriteVertices[i].x = Mathf.Clamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html)(
                (sprite.vertices[i].x - sprite.bounds.center.x -
                    (sprite.textureRectOffset.x / sprite.texture.width) + sprite.bounds.extents.x) /
                (2.0f * sprite.bounds.extents.x) * sprite.rect.width,
                0.0f, sprite.rect.width);  
  
            spriteVertices[i].y = Mathf.Clamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html)(
                (sprite.vertices[i].y - sprite.bounds.center.y -
                    (sprite.textureRectOffset.y / sprite.texture.height) + sprite.bounds.extents.y) /
                (2.0f * sprite.bounds.extents.y) * sprite.rect.height,
                0.0f, sprite.rect.height);  
  
            // Make a small change to the second vertex
            if (i == 2)
            {
                //Make sure the vertices stay inside the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) rectangle
                if (spriteVertices[i].x < sprite.rect.size.x - 5)
                {
                    spriteVertices[i].x = spriteVertices[i].x + 5;
                }
                else spriteVertices[i].x = 0;
            }
        }
        //Override the geometry with the new vertices
        sprite.OverrideGeometry(spriteVertices, sprite.triangles);
    }
}

```

* * *
