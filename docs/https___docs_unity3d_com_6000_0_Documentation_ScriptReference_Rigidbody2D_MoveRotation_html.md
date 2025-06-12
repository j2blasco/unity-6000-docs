* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).MoveRotation
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
public void MoveRotation(float angle); 
### Parameters
Parameter | Description  
---|---  
angle | The new rotation angle for the Rigidbody object.  
### Description
Rotates the Rigidbody to `angle` (given in degrees).
Rotates the Rigidbody to the specified `angle` by calculating the appropriate angular velocity required to rotate the Rigidbody to that angle during the next physics update. During the move, [angularDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularDamping.html) won't affect the body. This causes the object to rapidly move from the existing angle to the specified `angle`.  
  
Because this feature allows a Rigidbody to be rotated rapidly to the specified `angle`, any colliders attached to the Rigidbody will react as expected i.e. they will produce collisions and/or triggers. This also means that if the colliders produce a collision then it will affect the Rigidbody movement and potentially stop it from reaching the specified `angle` during the next physics update. If the Rigidbody is kinematic then any collisions won't affect the Rigidbody itself and will only affect any other dynamic colliders.  
  
[Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) components have a fixed limit on how fast they can rotate therefore attempting to rotate large angles over short time-scales can result in the Rigidbody not reaching the specified `angle` during the next physics update. It is recommended that you use this for relatively small rotational movements only.  
  
It is important to understand that the actual rotation change will only occur during the next physics update therefore calling this method repeatedly without waiting for the next physics update will result in the last call being used. For this reason, it is recommended that it is called during the FixedUpdate callback.
```
// MoveRotation
// The sprite is set a rotation speed.  
  
using UnityEngine;
using System.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex;  
  
    private Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb2D;
    private Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) mySprite;
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sr;
    private float revSpeed = 50.0f;  
  
    void Awake()
    {
        sr = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        rb2D = gameObject.AddComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
    }  
  
    void Start()
    {
        mySprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(tex, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0.0f, 0.0f, tex.width, tex.height), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.5f, 0.5f), 100.0f);
        transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(3.0f, 3.0f, 3.0f);
        rb2D.gravityScale = 0.0f;
        sr.sprite = mySprite;
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        rb2D.MoveRotation(rb2D.rotation + revSpeed * Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html));
    }
}

```

* * *
## Declaration
public void MoveRotation([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
rotation | Full 3D rotation used to extract only the z-axis rotation.  
### Description
An overload of MoveRotation that allows a full 3D rotation as an argument.
The z-axis rotation is extracted from the given [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) `rotation` and used as a target angle to move the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) to. It is important to understand that the full 3D rotation isn't used because the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) only has a single degree of rotational freedom around the z-axis.
* * *
