* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-projectiles.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * [Instantiating prefabs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
  * Instantiate projectiles and explosions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html)
Build a structure with prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)
Replace a character with a ragdoll or wreck
# Instantiate projectiles and explosions
In this example a `Launcher` **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) instantiates a projectile **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) when the player presses the fire button. The prefab contains a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody), and a **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider), so it can fly through the air and detect when a **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) occurs.
The projectile collides with something and instantiates an explosion prefab. The explosion prefab contains a **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) effect and a script that applies a force to surrounding GameObjects.
In the same way as the [Block example](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html), you can instantiate the projectile in just one line of code, no matter how complex the projectile prefab is. After instantiating the prefab, you can also modify any properties of the instantiated GameObject. For example, you can set the velocity of the projectile’s Rigidbody.
As well as being easier to use, you can modify the prefab later on without touching the code. So if your projectile is a rocket, later on you could add a Particle System to it to make it leave a cloud trail. After you do this, all your instantiated rockets have particle trails.
This script shows how to launch a projectile using the `Instantiate` method.
```
using UnityEngine;
public class FireProjectile : MonoBehaviour
{
    public Rigidbody projectile;
    public float speed = 4;
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            Rigidbody p = Instantiate(projectile, transform.position, transform.rotation);
            p.velocity = transform.forward * speed;
        }
    }
}

```

In the code, the prefab variable type is a Rigidbody rather than a GameObject. This has two useful effects:
  1. Only GameObjects that have a Rigidbody component can be assigned to this variable. This is useful because it helps make sure you’re assigning the correct GameObject to the variable.
  2. The `Instantiate` method returns a reference to the Rigidbody component on the new instance. This is useful because it makes it simple to set the velocity of the Rigidbody immediately after instantiating it.


When making a public prefab variable, the variable type can be a GameObject, or it can be any valid Component type (either a built-in Unity component or one of your own MonoBehaviour scripts).
For GameObject type variables, you can assign any GameObject to the variable, and the `Instantiate` function returns a reference to the new GameObject instance.
For component type variables (such as Rigidbody, Collider, and Light), you can only assign GameObjects of that component type to the variable, and the `Instantiate` function returns a reference to that specific component on the new GameObject instance.
The following script (placed on the projectile prefab) performs the action of instantiating the explosion at the projectile’s current position and removing the projectile GameObject when the projectile collides with something.
```
using UnityEngine;
public class Projectile : MonoBehaviour
{
   public GameObject explosion;
   void OnCollisionEnter()
   {
       Instantiate(explosion,transform.position,transform.rotation);
       Destroy(gameObject);
   }
}

```
![An example of projectile Prefabs being instantiated, and replaced with explosion Prefabs when they impact](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsProjectileAndExplosion.gif) An example of projectile Prefabs being instantiated, and replaced with explosion Prefabs when they impact
Notice in the image above, which shows the **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) running in Play mode, the instantiated GameObjects appear in the Hierarchy, with **(Clone)** appended to the name.
## Additional resources
  * [Build a structure with prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html)
  * [Replace a character with a ragdoll or wreck](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html)
Build a structure with prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)
Replace a character with a ragdoll or wreck
