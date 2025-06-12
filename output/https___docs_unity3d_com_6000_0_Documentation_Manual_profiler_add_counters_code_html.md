* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-counters-code.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Adding profiling information to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-adding-information-code.html)
  * Adding profiler counters to your code


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-markers-code.html)
Adding profiler markers to your code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-counters.html)
Visualizing profiler counters
# Adding profiler counters to your code
To add a **profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) counter, create **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to do the following:
  * [Create and define a new counter](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-counters-code.html#creating-and-defining-a-counter).
  * [Update the counter’s value](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-counters-code.html#updating-a-counters-value).


The code examples in these sections add a **Profiler counter** Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilercounter) to track the total number of particles that Unity created for every instance of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s trail effects. In these examples, the GameObject’s name is “Tank”.
## Prerequisites
Some examples use [the Profiling Core package](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest), which you must install before you start. The Unity Profiling Core package isn’t discoverable in the Package Manager UI because it’s a core package. To install the package [add it by its name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html), which is `com.unity.profiling.core`. 
## Creating and defining a counter
To create a new counter:
  1. Write a script that defines the value type of the new counter.
  2. Assign a name and a unit to this type.


**Important:** When you create a counter you must specify which **Profiler category** Identifies the workload data for a Unity subsystem (for example, Rendering, Scripting and Animation categories). Unity applies color-coding to categories to visually distinguish between the types of data in the **Profiler** window.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilercategory) your new counter belongs to. To do this, use an existing Unity category from the [`ProfilerCategory`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) class. The script in the following example uses the existing `ProfilerCategory.Scripts` category.
The Profiler counters API supports push and pull operations. You can push the value of the counter to the Profiler, or the Profiler can pull the value at the end of the frame.
If your data changes infrequently, for example once per frame, use the [`ProfilerCounter`](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest?subfolder=/api/Unity.Profiling.ProfilerCounter-1.html) API to push the counter data to the Profiler. If your data changes multiple times per frame, use the `ProfilerCounterValue` API. This makes the Profiler automatically pick up the last value at the end of the frame. 
The following example script defines the [`ProfilerCounterValue`](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest?subfolder=/api/Unity.Profiling.ProfilerCounter-1.html) `TankTrailParticleCount`, with the name `Tank Trail Particles` and a unit of [`ProfilerMarkerDataUnit.Count`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarkerDataUnit.Count.html):
```
public static class GameStats
{
   public static readonly ProfilerCategory TanksCategory = ProfilerCategory.Scripts;

   public const string TankTrailParticleCountName = "Tank Trail Particles";
   public static readonly ProfilerCounterValue<int> TankTrailParticleCount =
       new ProfilerCounterValue<int>(TanksCategory, TankTrailParticleCountName, ProfilerMarkerDataUnit.Count,
           ProfilerCounterOptions.FlushOnEndOfFrame | ProfilerCounterOptions.ResetToZeroOnFlush);
}

```

The options `FlushOnEndOfFrame` and `ResetToZeroOnFlush` automatically send the counter to the Profiler data stream and reset the Count value to zero at the end of the frame.
## Updating a counter’s value
To update the value of a counter, create a MonoBehaviour script that sets the value of a counter you have defined.
The following MonoBehaviour script counts the number of trail particles that belong to an assigned GameObject every frame in the Update function. To do this, it uses the counter called `TankTrailParticleCount`.
The following example script also creates a public property called Trail **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) (`m_TrailParticleSystem`) in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector):
```
 using UnityEngine;

 class TankMovement : MonoBehaviour
 {
    public ParticleSystem m_TrailParticleSystem;

    void Update()
    {
        GameStats.TankTrailParticleCount.Value += m_TrailParticleSystem.particleCount;
    }
 }

```

### Adding Profiler counters to a custom Profiler module
To display a Profiler counter in a custom Profiler module via code, you must create a new `ProfilerModule` script and define the module’s properties including the counters it displays, its name, and its icon. For information on how to do this refer to [Creating Profiler modules in code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-modules.html#creating-profiler-modules-code).
## Additional resources
  * [Adding profiling information to your code introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-adding-information-code-intro.html)
  * [Adding profiler markers to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-markers-code.html)
  * [Customizing Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
  * [Profiling Core package](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-markers-code.html)
Adding profiler markers to your code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-counters.html)
Visualizing profiler counters
