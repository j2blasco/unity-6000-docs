* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-intro.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * [Instantiating prefabs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
  * Introduction to instantiating prefabs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
Instantiating prefabs at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html)
Build a structure with prefabs
# Introduction to instantiating prefabs
To instantiate a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) at runtime, your code needs a reference to the prefab. To make this reference, you can create a public field of type `GameObject` in your code, then assign the prefab you want to use to this field in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
The script example below has a single public variable, `myPrefab`, which is a reference to a prefab. It creates an instance of that prefab in the `Start` method.
```
using UnityEngine;
public class InstantiationExample : MonoBehaviour 
{
    // Reference to the Prefab. Drag a Prefab into this field in the Inspector.
    public GameObject myPrefab;

    // This script will simply instantiate the Prefab when the game starts.
    void Start()
    {
        // Instantiate at position (0, 0, 0) and zero rotation.
        Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
    }
}

```

To use this example:
  1. Create a new MonoBehaviour script in your Project, and name it `InstantiationExample`.
  2. Copy and the code above and paste it into your new script, and save it.
  3. Create an empty GameObject using the menu **GameObject** > **Create Empty**.
  4. Add the script to the new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) as a component by dragging it onto the empty GameObject.
  5. [Create any Prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html), and drag it from the ****Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow)** into the **My Prefab** field in the script component.

![Dragging a Prefab from the Project window into the My Prefab field in the script component](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabDragIntoField.png) Dragging a Prefab from the Project window into the My Prefab field in the script component
When you enter Play mode, you should see your prefab instantiate at position (0, 0, 0) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
You can drag a different prefab into the **My Prefab** field in the **Inspector** window to change which prefab is instantiated, without having to change the script.
Because this first example is very simple, it may not seem to provide any advantage over just placing a prefab into the Scene yourself. However, being able to instantiate prefabs using code provides you with powerful abilities to dynamically create complex configurations of GameObjects while your game or app is running, as shown in the other examples in this section.
## Common scenarios
Instantiating prefabs at runtime is useful in the following common scenarios: 
  * Building a structure out of a single prefab by replicating it multiple times in different positions, for example in a grid or circle formation.
  * Firing a projectile prefab from a launcher. The projectile prefab could be a complex configuration containing a ****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh)**, ****Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody)**, ****Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider)**, **AudioSource** , **Dynamic Light** , and a child GameObject with its own trail ****Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem)**.
  * A vehicle, building, or character, for example a robot, breaking apart into many pieces. In this scenario, the example script deletes and replaces the complete, operational robot prefab with a wrecked robot prefab. This wrecked prefab consists of separate broken parts of the robot, each set up with Rigidbodies and Particle Systems of their own. This technique allows you to blow up a robot into many pieces, with just one line of code, which replaces the original GameObject with a wrecked prefab.


The following sections show you how to implement these scenarios.
## Additional resources
  * [Build a structure with prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html)
  * [Instantiate projectiles and explosions](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-projectiles.html)
  * [Simulate character destruction](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
Instantiating prefabs at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html)
Build a structure with prefabs
