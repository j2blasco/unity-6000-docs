* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * Profiler markers reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-command-line-arguments.html)
Profiler command line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-counters-reference.html)
Profiler counters reference
# Profiler markers reference
Unity’s code is instrumented with [profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-adding-information-code-intro.html#profiler-markers)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker) that give you insight into what takes up time in your application. The following tables contain a list of some of the in-built markers.
  * [Main thread base markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#main-thread)
  * [Script update markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#script-update)
  * [Rendering and VSync markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#rendering)
  * [Back end scripting markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#backend)
  * [Multithreading markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#multithreading)
  * [Physics markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#physics)
  * [Animation markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#animation)
  * [Performance warnings](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#warnings)


## Main thread base markers
The main thread base markers provide a clear separation between the time spent on your application and time spent on Unity Editor and **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) activities. You can also use these markers with the [`ProfilerRecorder`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) API to get the timing of a frame on the main thread, or the [`FrameTimingManager`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.html) API for high level frame stats at runtime.
You can also use the rendering **profiler counters** Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilercounter) CPU Main Thread Frame Time, CPU Render Thread Frame Time, and CPU Total Frame Time to get high-level timings of the CPU usage of your application. For more information, refer to [Rendering profiler counters reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-counters-reference.html#rendering).
**Marker** | **Description**  
---|---  
**PlayerLoop** | Contains any samples that originate from your application’s main loop. If you [target the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html) instead of Play mode while the Player is running within the Editor in active Play mode, PlayerLoop samples nest under the EditorLoop.  
**EditorLoop**  
 _(Editor only marker)_ | Contains any samples that originate from the Editor’s main loop. This is only present while you [profile a player in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html). When you [target Play mode with the Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html), EditorLoop samples indicate the amount of time spent rendering and running the Editor that contains the Player.  
  
For more information, refer to [Play mode and Edit mode samples](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html).  
**Profiler.CollectEditorStats**  
 _(Editor only marker)_ | Contains any samples that relate to collecting statistics for different active Profiler modules.  
  
Samples nested under the `Profiler.CollectGlobalStats` marker indicate how much overhead the Player has when it collects the statistics of a particular module. All other child samples only reflect their effect in the Editor.  
  
To remove the overhead that a particular module has, close the module’s chart, or call `Profiler.SetAreaEnabled`.  
  
**Note:** [Custom Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html) that use built-in counters enable the built-in counter’s area, even if the module it belongs is disabled. To prevent the Profiler from collecting these statistics and creating collection overhead, make sure that both the built-in Profiler module and your custom Profiler module are disabled.  
## Script update markers
Unless you’re using the [job system](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system.html), most of your scripting code is nested underneath the following markers. For information on job system samples, refer to the [Multi threading markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html#multithreading) section of this page.
For further details on Unity’s Update Loop, refer to the documentation on [Order of execution of event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html). You can insert your own callbacks into the [Player Loop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.html) using [`PlayerLoop.SetPlayerLoop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.SetPlayerLoop.html). If you insert callbacks directly into the main loop, your script update samples appear on their own. If you insert callbacks as a subsystem, the samples appear under the respective main PlayerLoopSystem marker.
**Marker** | **Description**  
---|---  
**BehaviourUpdate** | Contains all samples of [`MonoBehaviour.Update`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) methods.  
**CoroutinesDelayedCalls** | Contains all samples of [coroutines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine..html) after their first yield.  
**FixedBehaviourUpdate** | Contains all samples of [`Monobehaviour.FixedUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) methods.  
**PreLateUpdate.ScriptRunBehaviourLateUpdate** | Contains all samples of [`Monobehaviour.LateUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html) methods.  
**Update.ScriptRunBehaviourUpdate** | Contains all samples of [`MonoBehaviour.Update`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) and [coroutines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html).  
## Rendering and VSync markers
These markers contain the samples where the CPU spends time processing data for the GPU, or where it might be waiting for the GPU to finish. If the [GPU Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html) isn’t available, or it adds too much overhead, the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) in the Profiler module details pane doesn’t display this information. The samples under these markers can give you a good idea of whether your application is CPU-bound or GPU-bound.
**Marker** | **Description**  
---|---  
**WaitForTargetFPS** | Indicates how much time your application spent waiting for the targeted FPS that [`Application.targetFrameRate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) specifies.  
  
If the sample is a subsample of Gfx.WaitForPresentOnGfxThread, it represents the amount of time that your application spent waiting for the GPU. For example, this could be time that the GPU spent waiting for the next VSync, if that is configured in [QualitySettings.vSyncCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-vSyncCount.html), or if vSync is enforced on your target platform. However, samples with this marker are also emitted if the GPU hasn’t finished computing the frame.  
  
To determine what is causing samples with this marker to use a lot of time, switch to the [Timeline view in the CPU Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html). In this view, you can check what happened on the render thread and how much time passed between this sample ending in the current frame and the same sample ending in surrounding frames.  
  
If the duration is larger than your application’s frame time should be (based on the targeted frame rate or vSync) your frames are taking too long to render or compute. If that’s the case, investigate the render thread and see how much time it spent on Gfx.PresentFrame over other work it did to prepare and issue commands to the GPU. If the render thread spent a large amount of time in Gfx.PresentFrame, your rendering work is GPU-bound. If the render thread’s time was spent preparing commands, your application is CPU-bound.  
  
To find out what to focus on, if your application is GPU bound, profile the GPU work with the Unity Profiler or a platform profiler. For more information, see the User manual documentation on how to [optimize graphics performance](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance.html).  
  
**Note:** The Editor doesn’t VSync on the GPU and instead uses WaitForTargetFPS to simulate the delay for VSync. Some platforms, in particular Android and iOS, enforce VSync or have a default frame rate cap of 30 or 60.  
**Gfx.PresentFrame** | Represents the time your application spent waiting for the GPU to render and present the frame, which includes waiting for VSync.  
  
Samples with the WaitForTargetFPS marker on the main thread show how much time is spent waiting for VSync.  
**Gfx.ProcessCommands** | Contains all processing of the rendering commands on the render thread. Your application might have spent some of this processing time waiting for **VSync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VSync) or new commands from the main thread, which you can see from its child sample Gfx.WaitForPresentOnGfxThread.  
**Gfx.WaitForCommands** | Indicates that the render thread was ready for new commands. If you see this marker, it might indicate a bottleneck on the main thread.  
`<GraphicsAPIName>.WaitForLastPresent` for example:  
**GfxDeviceD3D11.WaitForLastPresent**  
**GfxDeviceD3D12.WaitForLastPresent**  
**GfxDeviceMetal.WaitForLastPresent** | Samples with this marker appear when the main thread waited for the GPU to flip the frame number to the screen (`Time.frameCount - QualitySettings.maxQueuedFrames + 1`). This means that if QualitySettings.maxQueuedFrames is greater than one, this time is spent waiting for the GPU to flip a frame that your application requested to render in a previous main thread frame.  
  
For more details on this sample and an overview of Unity’s Frame Pipeline, see [Unity’s blog post on fixing Delta Time](https://unity.com/blog/engine-platform/fixing-time-deltatime-in-unity-2020-2-for-smoother-gameplay).  
**Gfx.WaitForPresentOnGfxThread** | Indicates that the main thread was ready to start rendering the next frame, but the render thread didn’t finish waiting for the GPU to present the frame. This might indicate that your application is GPU-bound. To check what the render thread is simultaneously spending time on, check the CPU Profiler module’s [Timeline view](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-introduction.html#timeline-view).   
  
If the render thread spends time in Camera.Render, your application is CPU-bound and might be spending too much time sending draw calls or textures to the GPU.  
  
If the render thread spends time in `Gfx.PresentFrame`, your application is GPU-bound, or it might be waiting for VSync on the GPU. A `WaitForTargetFPS` sub-sample of `Gfx.WaitForPresentOnGfxThread` represents the portion of the Present phase that your application spent waiting for VSync. The Present phase is the portion of time between Unity instructing the graphics API to swap the buffers, to the time that this operation completed.  
**Gfx.WaitForRenderThread** | Indicates that the main thread was waiting for the render thread to process all the commands in its command stream. Samples with this marker only appear in multithreaded rendering.  
## Back end scripting markers
The samples highlight Mono or **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) **scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend) activities and are useful for troubleshooting issues with garbage collection and allocation.
**Marker** | **Description**  
---|---  
**GC.Alloc** | Represents an allocation in the managed heap that contains managed allocations that are subject to automatic garbage collection. To reduce the time your application spends on automatic garbage collection, you should minimize these types of samples.  
**GC.Collect** | Represents samples that relate to garbage collection. Whenever Unity needs to perform garbage collection, it stops running your program code and only resumes normal execution when the garbage collector has finished all its work. **Note:** If you have enabled [Incremental Garbage Collection](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-incremental-garbage-collection.html) the garbage collector might not finish its work in a single frame.  
  
This interruption might cause delays in the execution of your application that last anywhere from less than one millisecond to hundreds of milliseconds. This depends on how much memory the garbage collector needs to process and the platform your application is running on. For more information, see the documentation on [Understanding automatic memory management](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html).  
**Mono.JIT**  
 _Mono-only_ | Contains samples that relate to just-in-time compilation of a scripting method. When a function is executed for the first time, Mono compiles it and Mono.JIT represents this compilation overhead.  
**UnsafeUtility.Malloc** | Contains samples that call UnsafeUtility.Malloc to allocate unmanaged memory. While the Garbage Collector does not track this memory, allocating memory might have a significant performance impact which is shown with this sample. To investigate the source of this call, you can enable [Call Stack](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html)A list of methods that were called at run time, organized as a last-in-first-out stack.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#callstack) recording for this marker in the Profiler window.  
## Multithreading markers
These markers contain samples that don’t measure the CPU cycles consumed, but instead highlight information that relates to thread synchronization and the job system. When you see these samples, use the CPU Profiler module’s [Timeline view](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) to check what’s happening on other threads at the same time.
**Marker** | **Description**  
---|---  
**Idle** | Contains samples that indicate the length of time that a Worker Thread is inactive for. A worker thread is inactive any time that the job system doesn’t use it, and it goes into wait mode, where it waits on the semaphore.  
  
Small gaps between Idle samples usually happen when the Job System wakes them up, for example, to schedule new jobs. Longer gaps might indicate that a native job that hasn’t been instrumented is running on the thread.  
**JobHandle.Complete** | Contains samples that indicate when a sync point on a job happened. Sync points might have a performance impact on your application and might interfere with the execution of multi-threaded job code. To make it easier to find where exactly the sync point happened, enable [Call Stack](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) recording for this sample. In the CPU Profiler module’s **Timeline** view you can enable [Flow Events](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) to identify which jobs finished at this point.  
**Semaphore.WaitForSignal** | Contains a sample that depicts a synchronization point on a thread. To find the thread it’s waiting for, check the Timeline view for samples that ended shortly before this one.  
**WaitForJobGroupID** | A Sync Fence on a JobHandle was triggered. This might lead to [work stealing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html), which happens when a worker finishes its work and then looks at other workers’ jobs to complete. These display as job samples executed under this marker. Jobs that were stolen aren’t necessarily the jobs that were being waited for.  
## Physics markers
The following table outlines some high-level physics Profiler markers. [`FixedUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) calls all these measurements.
**Marker** | **Description**  
---|---  
**Physics.FetchResults** | Contains samples that collect the results of the physics simulation from the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine), such as contact streams, trigger overlaps, and **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) breakage events.  
**Physics.Interpolation** | Contains samples that measure the execution time of the `Physics.Interpolation` method. This method manages the interpolation of positions and rotations for all the physics objects in your application.  
**Physics.Processing** | Contains samples that spent time waiting on the main thread until the physics simulation completed across all threads. If your application spends a lot of time in `Physics.Processing` but only has a few physics related **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), it might indicate that worker threads picked up other systems tasks due to job stealing and reported as physics. This is because while waiting, the main thread picks up jobs from the high priority queue.  
**Physics.ProcessingCloth** | Contains samples that measure the execution time of the `Physics.ProcessingCloth` method. This method processes all cloth physics jobs. Expand this sample to display the low-level detail of the work done internally in the physics system.  
**Physics.ProcessReports** | Contains samples that correspond to time spent forwarding physics data to scripts via callbacks such as [`OnTriggerEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter.html). **Note:** These samples don’t compute the data required because they have already been prepared during `FetchResults`.  
  
There are four distinct stages:  

  * **Physics.Contacts** : Contains samples that measure the execution time of `Physics.Contacts`. This processes [`OnCollisionEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html), [`OnCollisionExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionExit.html), and [`OnCollisionStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionStay.html) events.
  * **Physics.JointBreaks** : Contains samples that measure the execution time of `Physics.JointBreaks`. This processes updates and messages related to broken joints.
  * **Physics.TriggerEnterExits** : Contains samples that measure the execution time of `Physics.TriggerEnterExits`. This processes [`OnTriggerEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter.html) and [`OnTriggerExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerExit.html) events.
  * **Physics.TriggerStays** : Contains samples that measure the execution time of `Physics.TriggerStays`. This processes [`OnTriggerStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerStay.html) events.

  
**Physics.Simulate** | Contains samples that measure the amount of time spent working on the pre-requisites for the [`Physics.Simulate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html) method. This method instructs the physics system to run its simulation, which updates the state of the current physics.  
**Physics.UpdateBodies** | Contains samples that update all the physics bodies’ positions and rotations. For each GameObject that has a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) component, samples with this marker read the pose from the physics system and write it to the Transform.  
**Physics.UpdateCloth** | Contains samples that measure the execution time of the `Physics.UpdateCloth` method. This method processes updates that relate to cloth and their Skinned Meshes.  
For more information about script lifecycles and general samples within a script lifecycle, refer to [Order of execution for event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html#UpdateOrder).
## Animation markers
The following tables contain markers from the [Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html). For general information on Animation system performance, refer to the [Mecanim Performance and and Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimPeformanceandOptimization.html) page.
### PreLateUpdate.DirectorUpdateAnimationBegin stage
In this stage, every Animator that’s active and enabled is processed. Active Animators are processed regardless of Culling Mode and visibility. 
Markers that start with `Director.` can also cover **Playables** An API that provides a way to create tools, effects or other gameplay mechanisms by organizing and evaluating data sources in a tree-like structure known as the PlayableGraph. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Playables) and Timeline.
**Marker** | **Description**  
---|---  
**Director.PrepareFrame** | Set up, schedule, and await `Director.PrepareFrameJob` jobs. These jobs evaluate the **state machines** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine) for all active **Animator components** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent).  
**Director.PrepareFrameJob _(job)_** | Evaluate the state machine of a single active Animator. The amount of time taken to process an Animator grows with the complexity of its state machine (i.e. the number of states, transitions, properties, and layers).  
  
Evaluation of state machines with [`StateMachineBehaviours`](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html) that implement [`OnStateMachineEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineEnter.html) or [`OnStateMachineExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineExit.html) listeners will be constrained to the main thread.  
**Animators.PrepareFirstPass** | Prepare for the next processing steps.  
**Animators.ProcessGraphJob** | Build, schedule, and await the results of `Animator.ProcessGraph` jobs.  
**Animators.ProcessGraph _(job)_** | Evaluate all properties across all connected AnimationClips.  
  
Calculate the root motion displacements by blending the root motion properties from all clips together.  
  
Collect new animation events for the current [`deltaTime`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html).  
  
When evaluating AnimationClips’ properties, the curve segments are cached locally between frames to avoid reading from the AnimationClips’ memory more than necessary.  
**Animators.FireAnimationEventsAndBehaviours** | Fire all **animation events** Allows you to add data to an imported clip which determines when certain actions should occur in time with the animation. For example, for an animated character you might want to add events to walk and run cycles to indicate when the footstep sounds should play. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEventsOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationEvent) messages on [`StateMachineBehaviours`](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html) and MonoBehaviours, except [`OnStateMachineEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineEnter.html) or [`OnStateMachineExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineExit.html) listeners which have already been fired in `Director.PrepareFrameJob`.  
**Animators.ApplyOnAnimatorMove** | Apply **root motion** Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootMotion) and trigger the [`OnAnimatorMove`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorMove.html) message on MonoBehaviours.  
### PreLateUpdate.DirectorUpdateAnimationEnd
In this stage, only Animators with the Culling Mode `Always Update` and visible Animators with the Culling Mode `UpdateTransform` or `Cull Completely` get processed. Animators with `Cull Completely` that were moved out of frame by the Root Motion don’t participate in this phase. Neither do Animators that were disabled by user code triggered by StateMachineBehaviours and AnimationEvents
**Marker** | **Function**  
---|---  
**Animators.PrepareSecondPass** | Set up the next processing steps. This includes filtering out Animators based on their Culling Mode and visibility status.  
**Animators.SortWriteJob** | The Transform system only allows a single thread to modify a Transform Hierarchy at a time. To accommodate this constraint, `Animators.SortWriteJob` groups `Animators.WriteTransforms` jobs by their [Transform.root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-root.html).  
  
For the best performance, avoid having multiple Animators in the same transform hierarchy to increase the granularity at which jobs can be scheduled and parallelized.  
**Animators.ProcessAnimationsJob** | Build, schedule, and await the results of `Animators.ProcessAnimations` jobs.  
**Animator.ProcessAnimations (_job_)** | Blend all properties on current active AnimationClips for a single Animator, except for root motion. Apply them to the internal avatar representation.  
  
The length of this marker scales with animation and blending complexity.  
**OnAnimatorIK** | Sets up animation IK. This is called once for each **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) layer with IK pass enabled.  
**Animators.WriteJob** | Build, schedule, and await the results of `Animator.WriteTransform` jobs. These jobs write transform poses from Animation **avatars** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) to the related GameObject transform hierarchy.  
**Animators.WriteTransforms _(job)_** | Writes all animated transforms to the scene from worker threads.  
**Animator.WriteProperties** | Write any animated property that is not a transform pose to the target object.  
## Performance warnings
The CPU Profiler detects some common performance issues and warns you about them. These appear in the Warning column of the [CPU Profiler module’s Hierarchy](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-introduction.html#hierarchy-views) view in the module details pane.
The Profiler detects some specific calls to avoid in performance-critical contexts. It displays the warnings with the reasons the operations are affecting performance as follows:
**Warning** | **Description**  
---|---  
**Animation.DestroyAnimationClip**  
**Animation.AddClip**  
**Animation.RemoveClip**  
**Animation.Clone**  
**Animation.Deactivate** | Indicates that RebuildInternalState has been triggered. RebuildInternalState is an operation that goes through the list of curves for each clip in the Animation component, and then rebinds each curve to a value on a component, on a GameObject.  
  
This is a resource-intensive operation, so you should avoid calling these methods at runtime as much as possible.  
**AssetBundle.asset/allAssets** | Indicates that Unity called the AssetBundleRequest.assets/allAssets API while the AssetBundle loading was not complete (AssetBundleRequest.isDone is false). This causes a stall on the main thread and waits for the loading operation to complete.  
**AsyncUploadManager.AsyncBufferResized**  
**AsyncUploadManager.AsyncBufferDelete** | Indicates that the internal buffer for uploading data to the GPU is resized because it’s not big enough. This resizing is slow and causes spikes in CPU activity.  
  
You can avoid this warning if you can spare the memory to allocate a larger size up front.  
  
You can use **Async Upload Buffer Size** setting in [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) to set the default size.  
  
The `AsyncUploadManager.AsyncBufferResized` marker indicates the newly allocated size which you can use as a guide for the default buffer size.  
**Rigidbody.SetKinematic** | Recreate non-convex MeshCollider for Rigidbody.  
## Additional resources
  * [Play mode and Editor samples](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html)
  * [CPU performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu.html)
  * [Adding profiling information to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-adding-information-code.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-command-line-arguments.html)
Profiler command line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-counters-reference.html)
Profiler counters reference
