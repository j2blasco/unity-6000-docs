* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [GameObject fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/gameobject-fundamentals.html)
  * The GameObject class


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gameobject-fundamentals.html)
GameObject fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)
Transforms
# The GameObject class
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html "Go to GameObject page in the Scripting Reference")
Unity’s **GameObject** class represents anything that can exist in a ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)**. GameObjects are the building blocks for scenes in Unity and act as a container for functional components which determine how the GameObject looks and what it does.
The [GameObject class](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) class provides a collection of methods which allow you to work with GameObjects in your code. These include methods for finding, making connections, and sending messages between GameObjects, adding or removing components attached to the GameObject, and setting values relating to their status within the scene.
For a complete reference of every member of the GameObject class, refer to the [GameObject script reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
For information on using GameObjects in the Scene and Hierarchy in the Unity Editor, refer to [Introduction to GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html).
## Scene status properties
All GameObjects share a set of controls at the top of the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) relating to the GameObject’s status within the scene, and these can be controlled via the GameObject’s scripting API.
![A typical GameObject viewed in the Inspector. In this case, a directional light. The Scene status properties are outlined in red.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectSceneStatusProperties.png) A typical GameObject viewed in the Inspector. In this case, a directional light. The Scene status properties are outlined in red.
## Active status
![The Active status of a GameObject](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GOInspectorActiveSetting.png) The Active status of a GameObject
GameObjects are active by default, but can be deactivated, which turns off all components attached to the GameObject. This generally means it will become invisible, and not receive any of the normal callbacks or events such as [`Update`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) or [`FixedUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html).
The GameObject’s **active** status is represented by the checkbox to the left of the GameObject’s name. You can control this using [`GameObject.SetActive`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetActive.html).
You can also use [`GameObject.activeSelf`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) to read the current active state of a GameObject. Use [`GameObject.activeInHierarchy`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html) to read whether the GameObject is actually active in the scene. [`GameObject.activeInHierarchy`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html) is necessary because whether a GameObject is actually active is determined by its own active state and the active state of all its parents. If any of its parents aren’t active, then it’s not active despite its own active setting.
## Static status
![The Static status of a GameObject](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GOInspectorStaticSetting.png) The Static status of a GameObject
Some of Unity’s systems, such as **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination), Occlusion, Batching, Navigation, and **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), rely on the static status of a GameObject. You can control which of Unity’s systems consider the GameObject to be **static** by using [`GameObjectUtility.SetStaticEditorFlags`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html). For more information, refer to [Static GameObjects](https://docs.unity3d.com/Manual/StaticObjects.html).
## Tags and Layers
![The Tag and Layer fields of a GameObject](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GOInspectorTagsAndLayers.png) The Tag and Layer fields of a GameObject
**Tags** provide a way of marking and identifying types of GameObject in your scene and **Layers** provide a similar but distinct way of including or excluding groups of GameObjects from certain built-in actions, such as [rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) or [physics collisions](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html).
For more information about how to use Tags and Layers in the editor, refer to the main user manual pages for [Tags](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)A reference word which you can assign to one or more GameObjects to help you identify GameObjects for scripting purposes. For example, you might define and “Edible” Tag for any item the player can eat in your game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tag) and [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer).
You can modify tag and layer values via script using the [`GameObject.tag`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-tag.html) and [`GameObject.layer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-layer.html) properties. You can also check a GameObject’s tag efficiently by using the [`CompareTag`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CompareTag.html) method, which includes validation of whether the tag exists, and doesn’t cause any memory allocation.
## Add and remove components
You can add or remove components at runtime, which can be useful for procedurally creating GameObjects, or modifying how a GameObject behaves. Note, you can also [`enable` or `disable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) script components, and some types of built-in component, via script without destroying them.
The best way to add a component at runtime is to use [`AddComponent<Type>`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.AddComponent.html), specifying the type of component within angle brackets as shown. To remove a component, you must use [`Object.Destroy`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) method on the component itself.
## Access components
The simplest case is where a script on a GameObject needs to access another Component attached to the same GameObject (remember, other scripts attached to a GameObject are also Components themselves). To do this, the first step is to get a reference to the Component instance you want to work with. This is done with the [GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) method. Typically, you want to assign the Component object to a variable, which is done in using the following code. In this example the script is getting a reference to a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) component on the same GameObject:
```
void Start ()
{
    Rigidbody rb = GetComponent<Rigidbody>();
}

```

Once you have a reference to a Component instance, you can set the values of its properties much as you would in the Inspector:
```
void Start ()
{
    Rigidbody rb = GetComponent<Rigidbody>();

    // Change the mass of the object's Rigidbody.
    rb.mass = 10f;
}

```

You can also call methods on the Component reference, for example:
```
void Start ()
{
    Rigidbody rb = GetComponent<Rigidbody>();

    // Add a force to the Rigidbody.
    rb.AddForce(Vector3.up * 10f);
}

```

Note: you can have multiple custom **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) attached to the same GameObject. If you need to access one script from another, you can use GetComponent as usual and just use the name of the script class (or the file name) to specify the Component type you want.
If you attempt to retrieve a Component type that hasn’t actually been added to the GameObject then GetComponent will return null. You will get a null reference error at runtime if you try to change any values on a null object.
## Access components on other GameObjects
Although they sometimes operate in isolation, it’s common for scripts to keep track of other GameObjects, or more commonly, components on other GameObjects. For example, in a cooking game, a chef might need to know the position of the stove. Unity provides different ways to retrieve other objects, each appropriate to certain situations.
### Link to GameObjects with variables in the Inspector
The most straightforward way to find a related GameObject is to add a public GameObject variable to the script:
```
public class Chef : MonoBehaviour
{
    public GameObject stove;

    // Other variables and functions...
}

```

This variable will be visible in the Inspector, as a **GameObject field**.
You can now drag an object from the scene or Hierarchy panel onto this variable to assign it.
![Dragging a Prefab from the Project window into a GameObject field in the Inspector window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabDragIntoField.png) Dragging a Prefab from the Project window into a GameObject field in the Inspector window
The GetComponent function and Component access variables are available for this object as with any other, so you can use code like the following:
```
public class Chef : MonoBehaviour {

    public GameObject stove;

    void Start() {
        // Start the chef 2 units in front of the stove.
        transform.position = stove.transform.position + Vector3.forward * 2f;
    }
}

```

Additionally, if you declare a public variable of a Component type in your script, you can drag any GameObject that has that Component attached onto it. This accesses the Component directly rather than the GameObject itself.
```
public Transform playerTransform;

```

Linking objects together with variables is most useful when you are dealing with individual objects that have permanent connections. You can use an array variable to link several objects of the same type, but the connections must still be made in the Unity editor rather than at runtime. It’s often convenient to locate objects at runtime and Unity provides two basic ways to do this, as described below.
### Find child GameObjects
Sometimes, a game Scene makes use of multiple GameObjects of the same type, such as collectibles, waypoints, and obstacles. These might need to be tracked by a particular script that supervises or reacts to them (for example, all waypoints might need to be available to a pathfinding script). Using variables to link these GameObjects is a possibility but it makes the design process tedious if each new waypoint has to be dragged to a variable on a script. Likewise, if a waypoint is deleted, then it’s a nuisance to have to remove the variable reference to the missing GameObject. In cases like this, it is often better to manage a set of GameObjects by making them all children of one parent GameObject. The child GameObjects can be retrieved using the parent’s **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) (because all GameObjects implicitly have a Transform):
```
using UnityEngine;

public class WaypointManager : MonoBehaviour {
    public Transform[] waypoints;

    void Start()
    {
        waypoints = new Transform[transform.childCount];
        int i = 0;

        foreach (Transform t in transform)
        {
            waypoints[i++] = t;
        }
    }
}

```

You can also locate a specific child object by name using the [Transform.Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Find.html) method:
```
transform.Find("Frying Pan");

```

This can be useful when a GameObject has a child GameObject that can be added and removed during gameplay. A tool or utensil that can be picked up and put down during gameplay is a good example of this.
## Send and broadcast messages
While editing your project you can set up references between GameObjects in the Inspector. However, sometimes it’s impossible to set these up in advance (for example, finding the nearest item to a character in your game, or making references to GameObjects that were instantiated after the Scene loaded). In these cases, you can find references and send messages between GameObjects at runtime.
[`BroadcastMessage`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.BroadcastMessage.html) allows you to send out a call to a named method, without being specific about where that method should be implemented. You can use it to call a named method on every MonoBehaviour on a particular GameObject or any of its children. You can optionally choose to enforce that there must be at least one receiver (or an error is generated).
[`SendMessage`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SendMessage.html) is a little more specific, and only sends the call to a named method on the GameObject itself, and not its children.
[`SendMessageUpwards`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SendMessageUpwards.html) is similar, but sends out the call to a named method on the GameObject and all its _parents_.
## Find GameObjects by Name or Tag
It’s always possible to locate GameObjects anywhere in the Scene hierarchy as long as you have some information to identify them. Individual objects can be retrieved by name using the [GameObject.Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html) function:
```
GameObject player;

void Start()
{
    player = GameObject.Find("MainHeroCharacter");
}

```

An object or a collection of objects can also be located by their tag using the [GameObject.FindWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html) and [GameObject.FindGameObjectsWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindGameObjectsWithTag.html) methods.
For example, in a cooking game with one chef character, and multiple stoves in the kitchen (each tagged “Stove”):
```
GameObject chef;
GameObject[] stoves;

void Start()
{
    chef = GameObject.FindWithTag("Chef");
    stoves = GameObject.FindGameObjectsWithTag("Stove");
}

```

## Create and destroy GameObjects
You can create and destroy GameObjects while your project is running. In Unity, a GameObject can be created using the [Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) method which makes a new copy of an existing object.
For a full description and examples of how to instantiate GameObjects, see [Instantiating Prefabs at Runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html).
The [Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) method destroys an object after the frame update has finished or optionally after a short time delay:
```
void OnCollisionEnter(Collision otherObj) {
    if (otherObj.gameObject.tag == "Garbage can") {
        Destroy(gameObject, 0.5f);
    }
}


```

Note that the Destroy function can destroy individual components and not affect the GameObject itself. A common mistake is to write `this` and assume it destroys the GameObject the script is attached to:
```
Destroy(this);

```

`this` represents the script, and not the GameObject. It will actually just destroy the script component that calls it and leave the GameObject intact but with the script component removed.
## Primitives
The GameObject class offers script-based alternatives to the options available in Unity’s GameObject menu that allows you to create [primitive objects](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html).
To create instances of Unity’s built-in primitives, use [GameObject.CreatePrimitive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html), which instantiates a primitive of the type that you specify. The available primitive types are [Sphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html), [Capsule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Capsule.html), [Cylinder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cylinder.html), [Cube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html), [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html) and [Quad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Quad.html)A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad).
![The Primitive shapes available in Unitys GameObject menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AllPrimitives.png) The Primitive shapes available in Unity’s GameObject menu
## Additional resources
  * [Introduction to GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)
  * [GameObject API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gameobject-fundamentals.html)
GameObject fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)
Transforms
