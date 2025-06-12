* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/create-compound-collider.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Compound colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders.html)
  * Create a compound collider


[](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders-introduction.html)
Introduction to compound colliders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surfaces.html)
Collider surfaces
# Create a compound collider
A compound **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) is a collection of collider GameObjects on the same parent **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). For details on when and why you might use a compound collider, see [Introduction to compound colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders-introduction.html). 
A compound collider is made up of a parent GameObject which has a Rigidbody component, and child GameObjects that have colliders. 
## Plan a compound collider
Before you build your compound collider, think about what you want to use the collider for, and how you want to arrange the colliders.
  * If you only need the collider to provide collisions, and not any **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) or trigger events, you can arrange colliders in any arrangement, including overlaps, as long as you have covered all of the space that should act as a collider at run time.
  * If you need the collider to call collision or trigger events, you need to arrange your compound collider in such a way that ensures there are no overlaps. You can also plan to implement [Tags](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)A reference word which you can assign to one or more GameObjects to help you identify GameObjects for scripting purposes. For example, you might define and “Edible” Tag for any item the player can eat in your game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tag) and Layers(Layers) to ensure that only specific colliders call collision and trigger events.
  * If you need to detect exactly which part of the item is involved in a collision, separate the item regions by collider. For example, on a treasure chest that opens when a player touches the front of it, you might have one collider on the front and one on the back.
  * If another collider needs to slide along your compound collider (for example, a character sliding across ice), try to have just one collider along that surface, to reduce jittering during transitions from one collider contact to another.


There is no one perfect way to arrange a compound collider; the efficiency always depends on the shape, the desired behavior, and the other elements in your project. For this reason, you should always run tests against your compound collider to check that it behaves as expected, and you should use the [Physics Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerPhysics.html) to test different arrangements and configurations for computational efficiency.
## Build a compound collider
  1. Create or choose the parent GameObject. In most cases, this is the GameObject that contains the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) and **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer).
  2. Add a Rigidbody to the parent GameObject, and configure it as needed for your project (see [Introduction to rigid body physics](https://docs.unity3d.com/6000.0/Documentation/Manual/RigidbodiesOverview.html)).
  3. Create an empty GameObject as a child of the parent GameObject. 
    1. Right-click on the parent GameObject, and select **Create Empty GameObject**.
  4. Add a collider to the new empty GameObject. 
    1. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, select **Add Component**.
    2. Choose a collider shape. You can use any collider shape on a compound collider. In most cases, you should aim to choose the simplest shape that can most accurately represent the collider you are building.
  5. Position the new collider. 
    1. Use the [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) or the [positioning shortcuts](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html) to position the collider.
  6. Test and observe the Rigidbody’s behavior. Changes to collider configuration can change the Rigidbody’s **center of mass** Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CenterofMass), which can result in some unexpected behavior.
  7. Repeat steps 4–6 for as many colliders as you need.


If you need to apply the same compound collider to multiple GameObjects, you can duplicate the parent GameObject or use [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab). 
## Automatically generate compound colliders
Several third-party tools are available on the [Asset Store](https://assetstore.unity.com/)A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) that can automatically generate a compound collider based on the Mesh of the GameObject. These tools are useful and can save time, but their output still requires testing and might require some adjustment to be fully efficient. You should apply the same level of testing to them as you would to a collider that you have built manually.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders-introduction.html)
Introduction to compound colliders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surfaces.html)
Collider surfaces
