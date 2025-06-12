* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerEnter2D.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).OnTriggerEnter2D(Collider2D)
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
### Parameters
Parameter | Description  
---|---  
other | The other [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) involved in this collision.  
### Description
Sent when another object enters a trigger collider attached to this object (2D physics only).
Further information about the other collider is reported in the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) parameter passed during the call.  
  
Trigger events will be sent to disabled [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)s, to allow enabling [Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)s in response to collisions.  
  
Additional resources: The [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) class and the [OnTriggerExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerExit2D.html) and [OnTriggerStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerStay2D.html) messages.  
  
An [OnTriggerEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerEnter2D.html) example is shown. This example has two empty [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)s, called `GameObject1` and `GameObject2`. These both have script files which makes the example work. The first script, `Example1`, creates a [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) and adds a [BoxCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) and a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). This object falls under gravity and collides with `Example2`. `Example2` has no visibility. (The rectangle it creates is visible in the Scene window.) Both [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)s report the collision.  
  
The script below is Example1.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Create GameObject1 that falls under gravity.  It will pass through
// Example2 and cause a collision.  GameObject1 is moved back to
// the start position and it will again start to fall under gravity.  
  
public class Example1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Awake()
    {
        SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sr;
        sr = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>() as SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html);
        sr.color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.1f, 1.0f);  
  
        BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) bc;
        bc = gameObject.AddComponent<BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html)>() as BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html);
        bc.size = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.0f, 1.0f);  
  
        Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb;
        rb = gameObject.AddComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>() as Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html);
        rb.gravityScale = 1.0f;  
  
        // A square in the Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) folder is used.
        gameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>().sprite = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)<Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)>("square");  
  
        // GameObject1 starts 3 units in the Up direction.
        gameObject.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 3.0f, 0.0f);
        gameObject.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.5f, 0.5f, 1.0f);
    }  
  
    private float timer = 0.0f;
    private bool restart = false;  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        if (restart == true)
        {
            timer = timer + Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
            if (timer > 0.25f)
            {
                gameObject.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 3.0f, 0.0f);
                gameObject.GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>().velocity = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.0f, 0.0f);
                restart = false;
            }
        }
    }  
  
    // called when this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) collides with GameObject2.
    void OnTriggerEnter2D(Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) col)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("GameObject1 collided with " + col.name);
        restart = true;
        timer = 0.0f;
    }
}

```

This is `Example2` which is the collide script for the second [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html):
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Create a rectangle that the other GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) will collide with.
// Note that this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has no visibility.
// (View in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view to see this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).)  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Awake()
    {
        BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) bc;
        bc = gameObject.AddComponent<BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html)>() as BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html);
        bc.size = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(3.0f, 1.0f);
        bc.isTrigger = true;  
  
        gameObject.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(3.0f, 1.0f, 1.0f);
        gameObject.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, -2.0f, 0.0f);
    }  
  
    void OnTriggerEnter2D(Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) col)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("GameObject2 collided with " + col.name);
    }
}

```

* * *
