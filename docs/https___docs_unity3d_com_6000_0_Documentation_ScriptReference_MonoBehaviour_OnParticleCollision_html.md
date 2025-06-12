* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleCollision.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnParticleCollision(GameObject)
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
### Description
OnParticleCollision is called when a particle hits a Collider.
This can be used to apply damage to a GameObject when hit by particles.  
  
This message is sent to scripts attached to Particle Systems and to the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) that was hit.  
  
When [OnParticleCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleCollision.html) is invoked from a script attached to a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html), the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) parameter represents the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html). The [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) receives at most one message per Particle System that collided with it in any given frame even when the Particle System struck the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) with multiple particles in the current frame. To retrieve detailed information about all the collisions caused by the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), the [ParticlePhysicsExtensions.GetCollisionEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetCollisionEvents.html) must be used to retrieve the array of ParticleSystem.CollisionEvent.  
  
When OnParticleCollision is invoked from a script attached to a [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) parameter represents a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with an attached [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) struck by the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html). The [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) receives at most one message per [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) that is struck. As above, [ParticlePhysicsExtensions.GetCollisionEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetCollisionEvents.html) must be used to retrieve all the collision incidents on the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).  
  
Messages are only sent if you enable `Send Collision Messages` in the Inspector of the Particle System Collision module.  
  
The OnParticleCollision can be a co-routine. Simply use the yield statement in the function.
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) part;
    public List<ParticleCollisionEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleCollisionEvent.html)> collisionEvents;  
  
    void Start()
    {
        part = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        collisionEvents = new List<ParticleCollisionEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleCollisionEvent.html)>();
    }  
  
    void OnParticleCollision(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) other)
    {
        int numCollisionEvents = part.GetCollisionEvents(other, collisionEvents);  
  
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb = other.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        int i = 0;  
  
        while (i < numCollisionEvents)
        {
            if (rb)
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = collisionEvents[i].intersection;
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) force = collisionEvents[i].velocity * 10;
                rb.AddForce(force);
            }
            i++;
        }
    }
}

```

* * *
