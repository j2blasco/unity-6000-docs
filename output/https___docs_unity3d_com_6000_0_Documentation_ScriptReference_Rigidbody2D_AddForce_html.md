* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForce.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).AddForce
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
public void AddForce([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) force, [ForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html) mode = ForceMode2D.Force); 
### Parameters
Parameter | Description  
---|---  
force | Components of the force in the X and Y axes.  
mode | The method used to apply the specified force.  
### Description
Apply a force to the rigidbody.
The force is specified as two separate components in the X and Y directions (there is no Z direction in 2D physics). The object will be accelerated by the force according to the law _force = mass x acceleration_ - the larger the mass, the greater the force required to accelerate to a given speed.  
  
If you don’t specify a ForceMode2D the default will be used. The default in this case is ForceMode2D.Force which adds force over time, using mass.  
  
To use the example scripts below, drag and drop your chosen script onto a Sprite in the Hierarchy. Make sure that the Sprite has a Rigidbody2D component.  
  
Additional resources: [AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForceAtPosition.html), [AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddTorque.html), [mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-mass.html), [linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html), [AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForce.html), [ForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html).
```
// The sprite will fall under its weight.  After a short time the
// sprite will start its upwards travel due to the thrust force that
// is added in the opposite direction.  
  
using UnityEngine;
using System.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex;  
  
    private Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb2D;
    private Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) mySprite;
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) sr;
    private float thrust = 1f;  
  
    void Awake()
    {
        sr = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        rb2D = gameObject.AddComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
    }  
  
    void Start()
    {
        mySprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(tex, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0.0f, 0.0f, 128.0f, 128.0f), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.5f, 0.5f), 100.0f);  
  
        sr.color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.5f, 1.0f);
        sr.sprite = mySprite;
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, -2.0f, 0.0f);
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        rb2D.AddForce(transform.up * thrust);
        // Alternatively, specify the force mode, which is ForceMode2D.Force[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Force.html) by default
        rb2D.AddForce(transform.up * thrust, ForceMode2D.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Impulse.html));
    }
}

```

* * *
