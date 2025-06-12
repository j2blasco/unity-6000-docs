* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).OnTriggerEnter(Collider)
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
other | The other [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) involved in this collision.  
### Description
Called when a Collider with the [Collider.isTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-isTrigger.html) property overlaps another Collider.
OnTriggerEnter is invoked when two GameObjects with a Collider component touch or overlap, and one of the Collider components has the [Collider.isTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-isTrigger.html) property enabled. A trigger Collider doesn't register collisions with an incoming Rigidbody and doesn't collide with any other GameObjects that have Colliders on them. The events are invoked during simulation, which happens after all FixedUpdate methods are called, or within the scope of [Physics.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html), if you're using manual physics simulation.  
  
Any Collider on a GameObject that has a Rigidbody component, or on a child of a GameObject with a Rigidbody component can create OnTrigger events.  
  
To use the following code sample, create a primitive [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), and attach a [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) and [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component to it. Enable Collider.isTrigger and Rigidbody.isKinematic. This GameObject will travel forward, until it collides with another GameObject. When a collision occurs, the direction immediately reverses.
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
