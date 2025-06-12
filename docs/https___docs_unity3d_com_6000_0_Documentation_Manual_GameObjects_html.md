* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * Introduction to GameObjects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
Working with GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gameobject-fundamentals.html)
GameObject fundamentals
# Introduction to GameObjects
The **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) is the most important concept in the Unity Editor.
Every object in your game is a **GameObject** , from characters and collectible items to lights, **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and special effects. However, a GameObject can’t do anything on its own; you need to give it properties before it can become a character, an environment, or a special effect.
![Four different types of GameObject: an animated character, a light, a tree, and an audio source](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectsExamples.jpg) Four different types of GameObject: an animated character, a light, a tree, and an audio source
**GameObjects** are the fundamental objects in Unity that represent characters, props and scenery. They do not accomplish much in themselves but they act as containers for **Components** A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component), which implement the functionality.
To give a GameObject the properties it needs to become a light, or a tree, or a camera, you need to add [components](https://docs.unity3d.com/6000.0/Documentation/Manual/Components.html) to it. Depending on what kind of object you want to create, you add different combinations of components to a GameObject.
Unity has lots of different built-in component types, and you can also make your own components using the [Unity Scripting API](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingComponents.html).
For example, a Light object is created by attaching a [Light](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) component to a GameObject.
![A simple Light GameObject with several Components](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectLightExample1.png) A simple Light GameObject with several Components
A solid cube object has a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Filter and **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component, to draw the surface of the cube, and a Box **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) component to represent the object’s solid volume in terms of physics.
![A simple Cube GameObject with several Components](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectCubeExample1.png) A simple Cube GameObject with several Components
## Details
A GameObject always has a [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) component attached (to represent position and orientation) and it is not possible to remove this. The other components that give the object its functionality can be added from the editor’s **Component** menu or from a script. There are also many useful pre-constructed objects (primitive shapes, Cameras, etc) available on the **GameObject > 3D Object** menu, see [Primitive Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html).
Because GameObjects are an important part of Unity, there is a lot of manual content with extensive detail about them. See the following sections for more information on using GameObjects in Unity:
  * [Transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)
  * [Introduction to components](https://docs.unity3d.com/6000.0/Documentation/Manual/Components.html)
  * [Using Components](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)
  * [Primitive and placeholder objects](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)
  * [Creating components with scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingComponents.html)
  * [Deactivating GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/DeactivatingGameObjects.html)
  * [Tags](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)A reference word which you can assign to one or more GameObjects to help you identify GameObjects for scripting purposes. For example, you might define and “Edible” Tag for any item the player can eat in your game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tag)
  * [Static GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html)
  * [Saving your work](https://docs.unity3d.com/6000.0/Documentation/Manual/Saving.html)


You can find out more about controlling GameObjects from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) on the [GameObject scripting reference page](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
* * *
  * 2017–08–01 Page amended 


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
Working with GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gameobject-fundamentals.html)
GameObject fundamentals
