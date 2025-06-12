* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-texture.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).texture
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
[Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture; 
### Description
Get the reference to the used Texture. If packed this will point to the atlas, if not packed will point to the source Sprite. 
This only returns the Texture the Sprite is currently using. You cannot change the Texture using this.
```
//Attach this script to a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Make sure it has a SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) component (should have by default)
//Next, attach a second Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) in the Inspector window of your first Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) m_SpriteRenderer;
    public Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) m_Sprite;  
  
    void Start()
    {
        //Fetch the SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) of the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)
        m_SpriteRenderer = GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        //Output the current Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) of the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) (this returns the source Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) if the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) isn't packed)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) 1 : " + m_SpriteRenderer.sprite.texture);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key to change the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) to the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) you attach in the Inspector
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Change the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)
            m_SpriteRenderer.sprite = m_Sprite;
            //Output the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) of the new Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) (this returns the source Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) if the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) isn't packed)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) 2 : " + m_SpriteRenderer.sprite.texture);
        }
    }
}

```

* * *
