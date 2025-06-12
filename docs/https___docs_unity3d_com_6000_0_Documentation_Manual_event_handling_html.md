* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Handling events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/time-capture-frame-rate.html)
Capturing frame rate
[](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html)
Event functions
# Handling events
Events are an important concept in Unity projects. For example, user inputs, **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) between characters, and stages of the physics or rendering loops are all things a game typically needs to respond to. In addition to the standard .NET APIs for [handling and raising events in C#](https://learn.microsoft.com/en-us/dotnet/standard/events/), Unity provides a range of Unity-specific APIs for events.
**Topic** | **Description**  
---|---  
[Event functions (predefined callbacks)](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) | Event functions are a set of built-in callbacks which you can implement on your MonoBehaviour-derived **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to respond to core Engine events related to physics, rendering, input, **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) loading and object lifecycles.  
[Execution order of event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html) | Understand the execution order of Unity’s built-in event functions so you can respond to events and update the state of your game in the right order.  
[Inspector-configurable custom events](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html) | Create your own custom events for which you can configure persistent (lasting between Edit mode and Play mode) callbacks in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.  
[Optimizing per-frame updates with an update manager](https://docs.unity3d.com/6000.0/Documentation/Manual/events-per-frame-optimization.html) | Create an update manager to handle many per-frame updates.  
## Additional resources
  * [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html)
  * [UGUI event system](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/EventSystem.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/time-capture-frame-rate.html)
Capturing frame rate
[](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html)
Event functions
