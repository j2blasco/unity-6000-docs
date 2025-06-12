* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-size.html

#  [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html).size
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) size; 
### Description
Property to set or get the size to render when the [SpriteRenderer.drawMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-drawMode.html) is set to [SpriteDrawMode.Sliced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Sliced.html) or [SpriteDrawMode.Tiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Tiled.html).
Assigning a Sprite to [SpriteRenderer.sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-sprite.html) when it is null will also set the [SpriteRenderer.size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-size.html) value to the Sprite's width and height.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb;
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sprRend;  
  
    void Awake()
    {
        sprRend = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>() as SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html);
        sprRend.drawMode = SpriteDrawMode.Sliced[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Sliced.html);  
  
        rb = gameObject.AddComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>() as Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html);
        rb.bodyType = RigidbodyType2D.Kinematic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html);
    }  
  
    void Start()
    {
        gameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>().sprite = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)<Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)>("image256x128");
        gameObject.transform.Translate(0.0f, 0.0f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key to increase the size of the sprite
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            sprRend.size += new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.05f, 0.01f);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) size: " + sprRend.size.ToString("F2"));
        }
    }
}

```

* * *
