* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter2D.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnTriggerEnter2D(Collider2D)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Parameters
Parameter | Description  
---|---  
other | The other Collider2D involved in this collision.  
### Description
Sent when another object enters a trigger collider attached to this object (2D physics only).
Further information about the other collider is reported in the Collider2D parameter passed during the call.  
  
This message is sent to the trigger Collider2D and the Rigidbody2D (if any) that the trigger Collider2D belongs to, and to the Rigidbody2D (or the Collider2D if there is no Rigidbody2D) that touches the trigger.  
  
**Note:** Trigger events are only sent if one of the Colliders also has a Rigidbody2D attached. Trigger events are sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.  
  
Additional resources: [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) class, [OnTriggerExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerExit2D.html), [OnTriggerStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerStay2D.html).  
  
The following two script examples create an [OnTriggerEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter2D.html) demo. Example1 generates a Unity logo sprite, `GameObject1`. This sprite is collided with by the Example2 sprite, `GameObject2`. The Example1 script creates the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). The kinematic mode is used on this script. Example2 supports the [OnCollisionEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter2D.html) method. This is called when GameObject2 collides with `GameObject1`. The script code for `GameObject2` controls the time it takes to collide with `GameObject1`. `GameObject2` is animated left-to-right repeatedly. When on the left side of the screen `GameObject2` moves right towards `GameObject1`. When these have collided `GameObject2` returns back to the left. The left side of the screen is the starting point for `GameObject2`. The right side of the screen is the constant position of `GameObject1`. The Example2 script code makes `GameObject2` collide with `GameObject1`. `GameObject2` stays collided for a short length of time.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) bc;
    private Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb;  
  
    void Awake()
    {
        SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sprRend = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>() as SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html);
        sprRend.color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.9f, 1.0f);  
  
        bc = gameObject.AddComponent<BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html)>() as BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html);
        bc.size = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.3f, 1.3f);
        bc.isTrigger = true;  
  
        rb = gameObject.AddComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>() as Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html);
        rb.bodyType = RigidbodyType2D.Kinematic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html);
    }  
  
    void Start()
    {
        gameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>().sprite = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)<Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)>("logo");
        gameObject.transform.Translate(4.0f, 0.0f, 0.0f);
        gameObject.transform.localScale = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(2.0f, 2.0f);
    }
}

```

Example2. This is the sprite that moves forwards and backwards and triggers with Example1.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float spriteMove;  
  
    void Awake()
    {
        SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sprRend;
        sprRend = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>() as SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html);
        sprRend.color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.9f, 1.0f);  
  
        BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) bc;
        bc = gameObject.AddComponent<BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html)>() as BoxCollider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html);
        bc.size = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.3f, 1.3f);
        bc.isTrigger = true;
    }  
  
    void Start()
    {
        gameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>().sprite = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)<Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)>("circle");
        gameObject.transform.Translate(-4.0f, 0.0f, 0.0f);
        spriteMove = 0.1f;
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        gameObject.transform.Translate(spriteMove, 0.0f, 0.0f);  
  
        if (gameObject.transform.position.x < -4.0f)
        {
            // move GameObject2 to the right
            spriteMove = 0.1f;
        }
    }  
  
    // when the GameObjects collider arrange for this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to travel to the left of the screen
    void OnTriggerEnter2D(Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) col)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(col.gameObject.name + " : " + gameObject.name + " : " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        spriteMove = -0.1f;
    }
}

```

* * *
