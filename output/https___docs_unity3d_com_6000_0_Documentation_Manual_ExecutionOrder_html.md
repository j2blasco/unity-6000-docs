* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Handling events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html)
  * Order of execution for event functions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html)
Event functions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html)
Inspector-configurable custom events
# Order of execution for event functions
Event functions are a set of built-in events that your MonoBehaviour **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) can optionally subscribe to by implementing the appropriate methods, often referred to as callbacks. The callbacks correspond to events in core Unity subsystems like physics, rendering, and user input, or to stages of the script’s own lifecycle such as its creation, activation, frame-dependent and frame-independent updates, and destruction. When the event occurs, Unity invokes the associated callback on your script, giving you the opportunity to implement logic in response to the event.
To the extent that Unity raises these events and calls the associated MonoBehaviour callbacks in a predetermined order, the order is documented here. It’s important to understand the execution order so you don’t try to use one callback to do work which depends on another callback that hasn’t been invoked yet. However, bear in mind that some callbacks are for events, such as those triggered by user inputs, which can occur at any time while your game is running. You should consult this page in combination with the [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) script reference (where the event callbacks are listed under **Messages**) for a complete understanding of each event’s meaning and limitations.
## Script lifecycle overview
The diagram below summarizes how Unity orders and repeats event functions over a script’s lifetime.
For more information about the various event functions, see the following sections:
  * [General principles](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#GeneralPrinciples)
  * [First Scene Load](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#FirstSceneLoad)
  * [Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#Editor)
  * [Before the first frame update](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#BeforeTheFirstFrameUpdate)
  * [In between frames](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#InBetweenFrames)
  * [Update order](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#UpdateOrder)
  * [Animation update loop](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#AnimationUpdateLoop)
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#Rendering)
  * [Coroutines](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#coroutines)
  * [When the object is destroyed](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#WhenTheObjectIsDestroyed)
  * [When quitting](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#WhenQuitting)


### Scope of the flowchart
The scope of the flowchart below is limited to the built-in event functions that you can subscribe to on any MonoBehaviour script by implementing the appropriate callbacks documented under **Messages** in the [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) scripting reference. Some additional internal methods local to the subsystems that raise the events are also shown for context.
In addition to these built-in event functions there are a number of other events you can potentially subscribe to in your scripts. Several major classes such as [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html), [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html), and [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) offer delegates that you can register your own callback methods with. Method attributes like [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) can also be used to execute methods at certain stages of the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Refer to the scripting reference for the component or subsystem you’re interested in to see what event callbacks you can subscribe to and details of their execution order.
### Script lifecycle flowchart
![Order of execution for event functions during the lifecycle of a MonoBehaviour script.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/monobehaviour_flowchart.svg) Order of execution for event functions during the lifecycle of a MonoBehaviour script.
**Note** : Some browsers do not support SVG image files. If the image above does not display properly (for example, if you cannot see any text), please try another browser, such as [Google Chrome](https://www.google.com/chrome/) or [Mozilla Firefox](https://www.mozilla.org/).
## General principles
In general, you should not rely on the order in which the same event function is invoked for different **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) — except when the order is explicitly documented or settable. If you need a more fine-grained control of the player loop, you can use the [PlayerLoop API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.html).  
You cannot specify the order in which an event function is called for different instances of the same MonoBehaviour subclass. For example, the `Update` function of one MonoBehaviour might be called before or after the `Update` function for the same MonoBehaviour on another GameObject — including its own parent or child GameObjects. 
You can specify that the event functions of one MonoBehaviour subclass should be invoked before those of a different subclass using the [Script Execution Order](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html) panel of the [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) window. For example, if you had two scripts, EngineBehaviour and SteeringBehaviour, you could set the Script Execution Order such that EngineBehaviours always update before SteeringBehaviours. If loading [multiple scenes additively](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html), the configured script execution order is applied in full one scene at a time, rather than partially across scenes, so EngineBehaviours and SteeringBehaviours would both update on one scene before they updated on the next one.
## First Scene load
These functions get called when a scene starts (once for each object in the scene). 
  * `Awake`: First lifecycle function called when a new instance of an object is created. Always called before any `Start` functions. If a GameObject is inactive during start up, `Awake` is not called until it is made active.
  * `OnEnable`: Called when the object becomes enabled and active, always after `Awake` (on the same object) and before any `Start`.


For objects that are part of a scene asset, `Awake` and `OnEnable` functions for _all_ scripts are called before `Start` and subsequent functions are called for _any_ of them. However, this can’t be enforced when you instantiate an object at runtime.
`Awake` is only guaranteed to be called before `OnEnable` in the scope of each individual object. Across multiple objects the order is not deterministic and you can’t rely on one object’s `Awake` being called before another object’s `OnEnable`. Any work that depends on `Awake` having been called for all objects in the scene should be done in `Start`.
### Before scene load and unload
Not shown in the diagram above are the [SceneManager.sceneLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html) and [SceneManager.sceneUnloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html) events which allow you to receive callbacks when a scene has loaded and unloaded respectively. Refer to the relevant scripting reference pages for details and example usage. You can expect to receive the `sceneLoaded` notification after `OnEnable` but before `Start` for all objects in the scene. Refer to [Details of disabling Domain and Scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html) for a diagram that includes scene load as part of the execution flow.
You can also use the [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) and its types [BeforeSceneLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) and [AfterSceneLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.AfterSceneLoad.html) to make your methods run before or after scene load respectively. Refer to the [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) scripting reference main page for execution order information for methods marked with these types.
## Editor
  * `Reset`: called to initialize the script’s properties when it is first attached to an object and also when the _Reset_ command is used.
  * `OnValidate`: called whenever the script’s properties are set, including when an object is deserialized, which can occur at various times, such as when you open a scene in the Editor and after a domain reload.


## Before the first frame update
  * `Start`: called before the first frame update only if the script instance is enabled.


For objects that are part of a scene asset, the `Start` function is called on all scripts before `Update` is called for any of them. However, this cannot be enforced when you instantiate an object during gameplay. For example, if you instantiate an object from another object’s `Update` function, the instantiated object’s `Start` can’t be called until `Update` runs for the first time on the original object.
## In between frames
  * `OnApplicationPause`: This is called at the end of the frame where the pause is detected, effectively between the normal frame updates. One extra frame will be issued after `OnApplicationPause` is called to allow the game to show graphics that indicate the paused state.


## Update Order
When you’re keeping track of game logic and interactions, animations, camera positions, etc., there are a few different events you can use. The common pattern is to perform most tasks inside the `Update` function, but there are also other functions you can use.
  * `FixedUpdate` happens at fixed intervals of in-game time rather than per frame. Since these updates are fixed and frame rate is variable, there may be no fixed update during a frame when frame rate is high, or multiple fixed updates per frame when frame rate is low. All physics calculations and updates occur immediately after `FixedUpdate` and because it’s frame-rate independent you don’t need to multiply values by [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) when calculating movement in a `FixedUpdate`. The interval at which fixed updates happen is defined by [Time.fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html), which can be set directly in scripts or via the ****Fixed Timestep** A customizable frame-rate-independent interval that dictates when physics calculations and FixedUpdate() events are performed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TimeManager.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FixedTimestep)** property in the Editor’s [Time settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TimeManager.html). For more information, including the time calculations used to determine whether to perform an `Update` or a `FixedUpdate`, refer to [Time](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html).
  * `Update` is called once per frame and is the main function for frame updates.
  * `LateUpdate` is called once per frame, after `Update` has finished. Any calculations performed in `Update` will have completed when `LateUpdate` begins. A common use for `LateUpdate` would be a following third-person camera. If you make your character move and turn inside `Update`, you can perform all camera movement and rotation calculations in `LateUpdate`. This will ensure that the character has moved completely before the camera tracks its position.


## Animation update loop
The following Animation loop callbacks shown in the [flowchart](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#ScriptLifecycleFlowchart) above are called on scripts that derive from [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html):
  * [MonoBehaviour.OnAnimatorMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorMove.html)
  * [MonoBehaviour.OnAnimatorIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorIK.html)


Additional animation-related event functions are called on scripts that derive from [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html):
  * [StateMachineBehaviour.OnStateMachineEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineEnter.html)
  * [StateMachineBehaviour.OnStateMachineExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineExit.html)
  * [StateMachineBehaviour.OnStateEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateEnter.html)
  * [StateMachineBehaviour.OnStateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateUpdate.html)
  * [StateMachineBehaviour.OnStateExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateExit.html)
  * [StateMachineBehaviour.OnStateMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMove.html)
  * [StateMachineBehaviour.OnStateIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateIK.html)


For the meaning and limitations of these callbacks, refer to the relevant scripting reference pages.
Other animation functions shown in the flowchart are internal to the animation system and are provided for context. These functions have associated Profiler markers so you can use the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) to see when in the frame Unity calls them. Knowing when Unity calls these functions can help you understand exactly when the Event functions you do call are executed. For a full execution order of animation functions and profiler markers, refer to [Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#animation)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker).
## Rendering
This execution order applies for the [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html) only. For details of execution order in **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) based on the [Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html), refer to the relevant sections of the documentation for the [Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html) or the [High Definition Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/rendering-execution-order.html). If you want to do work immediately prior to rendering, refer to [Application.onBeforeRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.onBeforeRender.html).
  * `OnPreCull`: Called before the camera culls the scene. Culling determines which objects are visible to the camera. `OnPreCull` is called just before culling takes place.
  * `OnBecameVisible`/`OnBecameInvisible`: Called when an object becomes visible/invisible to any camera. `OnBecameInvisible` is not shown in the flow chart above since an object may become invisible at any time.
  * `OnWillRenderObject`: Called **once** for each camera if the object is visible.
  * `OnPreRender`: Called before the camera starts rendering the scene.
  * `OnRenderObject`: Called after all regular scene rendering is done. You can use [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html) class or [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html) to draw custom geometry at this point.
  * `OnPostRender`: Called after a camera finishes rendering the scene.
  * `OnRenderImage`: Called after scene rendering is complete to allow **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) of the image, see [Post-processing Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html).
  * `OnGUI`: Called multiple times per frame in response to GUI events. The Layout and Repaint events are processed first, followed by a Layout and keyboard/mouse event for each input event.
  * `OnDrawGizmos` Used for drawing **Gizmos** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) in the **scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) for visualisation purposes.


**Note** : [OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPreCull.html), [OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPreRender.html), [OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPostRender.html), and [OnRenderImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderImage.html) are built-in Unity event functions that are called on MonoBehaviour scripts but **only if those scripts are attached to the same object as an enabled Camera component**. If you want to receive the equivalent callbacks for `OnPreCull`, `OnPreRender`, and `OnPostRender` on a MonoBehaviour attached to a **different** object, you must use the equivalent delegates (note the lowercase `on` in the names) [Camera.onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html), [Camera.onPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreRender.html), and [Camera.onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html) as shown in the code examples in the relevant pages of the scripting reference.
## Coroutines
Normal coroutine updates are run after the `Update` function returns. A coroutine is a function that can suspend its execution (`yield`) until the given YieldInstruction finishes.
Different uses of coroutines:
  * `yield` The coroutine will continue after all `Update` functions have been called on the next frame.
  * `yield WaitForSeconds` Continue after a specified time delay, after all `Update` functions have been called for the frame.
  * `yield WaitForFixedUpdate` Continue after all `FixedUpdate` has been called on all scripts. If the coroutine yielded before `FixedUpdate`, then it resumes after `FixedUpdate` in the current frame.
  * `yield WWW` Continue after a WWW download has completed.
  * `yield StartCoroutine` Chains the coroutine so that if a theoretical coroutine `coroutineA` starts another `coroutineB` with `yield StartCoroutine(coroutineB());` then `coroutineA` pauses and waits for `coroutineB` to finish before continuing. For an example, refer to [MonoBehaviour.StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html).


## When the Object is destroyed
  * `OnDestroy`: This function is called after all frame updates for the last frame of the object’s existence (the object might be destroyed in response to Object.Destroy or at the closure of a scene).


## When quitting
These functions get called on all the active objects in your scene:
  * `OnApplicationQuit`: This function is called on all game objects before the application is quit. In the editor it is called when the user stops playmode.
  * `OnDisable`: This function is called when the behaviour becomes disabled or inactive.


## Additional resources
  * [Event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html)
  * [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html)
Event functions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html)
Inspector-configurable custom events
