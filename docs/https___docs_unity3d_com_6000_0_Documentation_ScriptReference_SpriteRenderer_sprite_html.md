* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-sprite.html

#  [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html).sprite
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
[Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite; 
### Description
The Sprite to render.
The [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) component will render the assigned Sprite.sprite sprite. The rendered sprite can be changed by specifying a different sprite in the [sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-sprite.html) variable.
```
// Example that loads sprites from a texture in the Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) folder
// and allows them to be chosen by the selection button.  
  
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private string spriteNames = "part_explosion";
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) buttonPos;
    private int spriteVersion = 0;
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) spriteR;
    private Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)[] sprites;  
  
    void Start()
    {
        buttonPos = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10.0f, 10.0f, 150.0f, 50.0f);
        spriteR = gameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        sprites = Resources.LoadAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html)<Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)>(spriteNames);
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(buttonPos, "Choose next sprite"))
        {
            spriteVersion += 1;
            if (spriteVersion > 3)
                spriteVersion = 0;
            spriteR.sprite = sprites[spriteVersion];
        }
    }
}

```

* * *
