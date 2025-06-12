* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-example-scripts.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider interactions](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions.html)
  * Example scripts for collider events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-create-trigger.html)
Create and configure a trigger collider
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)
Collision detection
# Example scripts for collider events
The following examples demonstrate ways to call events from **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) functions. They use `OnCollisionEnter` and `OnTriggerEnter` respectively, but the concepts apply to all `OnCollision` and `OnTrigger` functions.
## Example: Different events for different GameObject properties
You can configure your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to trigger different events based on the properties of the other **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider)’s associated **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), such as its name or tag. This is useful if, for example, you want to allow some colliders to produce an event, but not others.
The following example prints a different message depending on whether the other collider that has touched this collider has a tag of “Player” or “Enemy”.
```
using UnityEngine;
using System.Collections;

public class DoorObject : Monobehaviour
{
    private void OnCollisionEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            Debug.Log ("The player character has touched the door.")
        }

        if (other.CompareTag("Enemy"))
        {
            Debug.Log ("An enemy character has touched the door!")
        }
    }
}

```

## Example: Send an event message every physics update
The following example uses a trigger collider to produce a hoverpad. The trigger collider is positioned directly on top of a hoverpad GameObject, and applies a constant upward force to any GameObject within its trigger. 
```
using UnityEngine;
using System.Collections;

public class HoverPad : MonoBehaviour
{
    // define a value for the upward force calculation
    public float hoverForce = 12f;

    // whenever another collider is in contact with this trigger collider…
    void OnTriggerStay (Collider other)
    {
        // …add an upward force to the Rigidbody of the other collider.
        other.rigidbody.AddForce(Vector3.up * hoverForce, ForceMode.Acceleration) 
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-create-trigger.html)
Create and configure a trigger collider
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)
Collision detection
