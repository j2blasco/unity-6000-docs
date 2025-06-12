* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SetRotation.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).SetRotation
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
public void SetRotation(float angle); 
### Parameters
Parameter | Description  
---|---  
angle | The rotation of the Rigidbody (in degrees).  
### Description
Sets the rotation of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) to `angle` (given in degrees).
Additional resources: [Rigidbody2D.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-rotation.html) and [Rigidbody2D.MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html).
```
using UnityEngine;  
  
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) rigidBody2D every frame.
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rigidBody2D;
    public float rotation = 0.0f;  
  
    void Start()
    {
        rigidBody2D = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        rigidBody2D.SetRotation(rotation);  
  
        rotation += 1.0f;
    }
}

```

* * *
## Declaration
public void SetRotation([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
rotation | Full 3D rotation used to extract only the z-axis rotation.  
### Description
Sets the rotation of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) to the z-axis rotation extracted from the full 3D `rotation`.
The z-axis rotation is extracted from the given [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) `rotation` and used as the rotation for [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). It is important to understand that the full 3D rotation isn't used because the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) only has a single degree of rotational freedom around the z-axis.
```
using UnityEngine;  
  
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) rigidBody2D every frame.
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rigidBody2D;
    public float rotation = 0.0f;  
  
    void Start()
    {
        rigidBody2D = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var quaternionRotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(0f, 0f, rotation);
        rigidBody2D.SetRotation(rotation);  
  
        rotation += 1.0f;
    }
}

```

* * *
