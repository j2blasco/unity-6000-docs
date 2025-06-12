* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-InternalProfiler.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * [Optimize performance for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-performance.html)
  * Measure performance with the built-in profiler


[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-iOS-Optimization.html)
Optimize for mobile
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-playerSizeOptimization.html)
Optimize the size of the iOS Player
# Measure performance with the built-in profiler
**Note:** The internal profiler is deprecated and will be retired in a future version of Unity. Use the [Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html) instead (menu: **Window** > **Analysis** > **Profiler**) Refer to [Collecting performance data on an iOS device](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-profile-device.html) for more information on how to profile iOS devices.
Unity contains a built-in **profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) for iOS to provide insight on how the application is running. Every 30 frames, the built-in profiler emits console messages from the application running on the device to help determine if it’s CPU or GPU-bound. If your application is CPU-bound, you can determine whether script code or garbage collection is causing the bottleneck.
Here’s an example of the built-in profiler’s output:
```
iPhone Unity internal profiler stats
frametime>     min: 32.5   max: 34.1   avg: 33.3
cpu-player>    min:  2.2   max:  4.4   avg:  3.7
batches>       min:   3    max:   3    avg:   3
draw calls>    min:   3    max:   3    avg:   3
tris>          min:  1704  max:  1704  avg:  1704
verts>         min:  5088  max:  5088  avg:  5088
dynamic batching> batched draw calls:   0 batches:   0 tris:     0 verts:     0
static batching>  batched draw calls:   0 batches:   0 tris:     0 verts:     0
player-detail> physx:  0.0 animation:  0.0 culling  0.0 skinning:  0.0 batching:  0.0 render:  0.0 fixed-update-count: 0 .. 0
scripting-scripts>  update:  0.0   fixedUpdate:  0.0 coroutines:  0.0 
scripting-memory>   information not available on non-development player configuration

```

All times are measured in milliseconds per frame. You can check the minimum, maximum, and average times over the last thirty frames.
## General CPU activity
**Property** | **Function**  
---|---  
**cpu-player** | Displays the time your app spends executing code inside the Unity engine and executing **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) on the CPU.  
**cpu-ogles-drv** (Android only) | Displays the time spent executing OpenGL ES driver code on the CPU. These driver stats can be affected by several factors, including the number of draw calls, number of internal rendering state changes, rendering pipeline setup, and number of processed vertices.  
**cpu-present** (Android only) | The amount of time spent executing the `presentRenderbuffer` command in OpenGL ES.  
**frametime** | Represents the overall time of an app frame. Note that iOS hardware is locked at a 60Hz refresh rate, so this property will always return a time that’s a multiple of 16.7ms (1000ms/60Hz = 16.7ms).  
## Rendering statistics
**Property** | **Function**  
---|---  
**tris #** | Total number of triangles sent for rendering.  
**verts #** | Total number of vertices sent for rendering. Keep this number under 10000 if your application uses only static geometry. If your application uses many instances of skinned geometry, this number should be much lower.  
**dynamic/static batching** | Number of draw-calls, triangles, and vertices that the engine automatically batched. Comparing these numbers with draw-call and triangle totals can give you an idea how well is your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) prepared for batching. Share as many materials as possible among your objects to improve batching.  
## Detailed Unity Player statistics
The **player-detail** section provides a detailed breakdown of what’s happening inside the engine:
**Property** | **Function**  
---|---  
**physx** | Time spent on physics.  
**animation** | Time spent animating bones.  
**culling** | Time spent culling objects outside the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) frustum.  
**skinning** The process of binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed with an external tool, such as Blender or Autodesk Maya. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skinning) | Time spent applying animations to skinned meshes.  
**batching** | Time spent batching geometry. Batching dynamic geometry is considerably more resource-intensive than batching static geometry.  
**render** | Time spent rendering visible objects.  
**fixed-update-count** | Minimum and maximum number of FixedUpdates executed during this frame. Too many FixedUpdates will deteriorate performance considerably.  
## Detailed script statistics
The **scripting-scripts** section provides a detailed breakdown of the time spent executing code in the Mono runtime:
**Property** | **Function**  
---|---  
**update** | Total time spent executing all `Update()` methods in scripts.  
**fixedUpdate** | Total time spent executing all `FixedUpdate()` methods in scripts.  
**coroutines** | Time spent inside script coroutines.  
## Detailed statistics on memory allocated by scripts
The **scripting-memory** section gives you an idea of how memory is managed by the Mono garbage collector:
**Property** : |  **Function** :  
---|---  
**allocated heap** | Total amount of memory available for allocations. A garbage collection triggers if the heap doesn’t have enough memory left for a given allocation. If this doesn’t free enough memory, the allocated heap will grow in size.  
**used heap** | The portion of the **allocated heap** which is currently used up by objects. Every time you create a new class instance (not a struct), this number grows until the next garbage collection.  
**max number of collections** | Number of garbage collection passes during the last 30 frames.  
**collection total duration** | Total time (in milliseconds) of all garbage collection passes that happened during the last 30 frames.  
## Configuration
On iOS, the internal profiler is disabled by default. To enable it, use either of the following processes.
### Xcode project
To enable the internal profiler from inside the Xcode project, use the following steps:
  1. Open the Unity-generated Xcode project,
  2. Select the `InternalProfiler.h` file.
  3. Update the following line from:

```
#define ENABLE_INTERNAL_PROFILER 0

```

to
```
#define ENABLE_INTERNAL_PROFILER 1

```

### Player settings
To enable the internal profiler in Unity, use the following steps:
  1. In the main menu, go to **Edit** > **Project Settings** > **Player Settings** > **iOS**.
  2. In the **Debugging and crash reporting** section, enable **Enable Internal Profiler (Deprecated)**.


**Note** : Ensure that the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** option is enabled in the **Platform Settings** section of the ****Build Profiles** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)** window when you build your application.
## Display the console
To display the output console, in Xcode select **View** > **Debug Area** > **Activate Console** and then run your project. Unity outputs statistics to the console window every 30 frames.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-iOS-Optimization.html)
Optimize for mobile
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-playerSizeOptimization.html)
Optimize the size of the iOS Player
