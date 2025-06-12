* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * Object-oriented development


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-garbage-collection.html)
Garbage collection
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html)
Managing time and frame rate
# Object-oriented development
Traditional Unity projects are object-oriented in two related ways:
  * They embrace the object-oriented programming philosophy, which is grounded in the concept of objects, their properties and functions, and the relations between these objects.
  * The original architecture of Unity projects uses an object-based model with types derived from `UnityEngine.Object`. In this model, **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) are composed of GameObjects which in turn interact with and are controlled by objects of other types.


An alternative to object-oriented development is data-oriented development, which is both a programming philosophy and a set of technologies that help you implement those principles. The data-oriented approach offers strong performance advantages at scale but can be more challenging for inexperienced developers to learn.
Object-oriented and data-oriented development are not mutually exclusive and you can combine elements from both. For information on data-oriented development, refer to [Unity’s Data-Oriented Technology Stack](https://unity.com/dots).
**Topic** | **Description**  
---|---  
[Managing time and frame rate](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html) | Understand how Unity measures time so you can manage the rate at which time passes in your application and ensure values update according to the appropriate time scale.  
[Handling events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html) | Make your application responsive to events such as user input, object **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision), and physics and rendering updates.  
[Splitting tasks across frames](https://docs.unity3d.com/6000.0/Documentation/Manual/Coroutines.html) | Split the execution of a task synchronously across multiple scenes with coroutines. This can be useful for tasks that should progress gradually over several frames, such as a fade out effect.  
[Interacting with web servers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html) | Use the UnityWebRequest system to allow your application to interact with a web server via HTTP.  
[Adding functionality to objects at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html) | Use the Unity Properties API to implement a visitor design pattern and add new operations to .NET objects at runtime.  
[Moving objects with vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html) | Use vectors to move objects in a specific direction and magnitude in 2, 3, and 4 dimensions.  
[Using common math functions](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html) | Use common math functions, including trigonometric, logarithmic, and other functions in your application.  
[Using randomness](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Random.html) | Generate commonly required types of random values.  
[Null references](https://docs.unity3d.com/6000.0/Documentation/Manual/null-reference-exception.html) | Understand and diagnose null reference exceptions in Unity projects.  
[Unity attributes](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-attributes.html) | Use Unity-specific C# attributes to define special behavior for your code.  
## Additional resources
  * [Unity’s Data-Oriented Technology Stack](https://unity.com/dots)
  * [GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-garbage-collection.html)
Garbage collection
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html)
Managing time and frame rate
