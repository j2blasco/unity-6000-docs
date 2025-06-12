* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnTriggerEnter(Collider)
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
other | A [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) involved in this collision.  
### Description
When a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) collides with another [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), Unity calls OnTriggerEnter.
OnTriggerEnter happens on the FixedUpdate function when two GameObjects collide. The Colliders involved are not always at the point of initial contact.  
  
Both GameObjects must contain a [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component. At least one of the colliders must be a trigger collider and at least one must be a physics body collider. For more information refer to [Interaction between collider types](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-interaction.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float speed = 2f;  
  
    //Moves this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) 2 units a second in the forward direction
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.Translate(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * speed);
    }  
  
    //Upon collision with another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) will reverse direction
    private void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        speed = speed * -1;
    }
}

```

* * *
