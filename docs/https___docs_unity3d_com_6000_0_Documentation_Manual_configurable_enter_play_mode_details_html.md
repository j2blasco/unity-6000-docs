* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Code and scene reload on entering Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/code-reloading-editor.html)
  * Details of disabling domain and scene reload


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html)
Enter Play mode with scene reload disabled
[](https://docs.unity3d.com/6000.0/Documentation/Manual/running-editor-code-on-launch.html)
Running project code on Editor launch
# Details of disabling domain and scene reload
## What Unity skips when domain reload and scene reload is disabled
From a high-level perspective, entering Play mode consists of the following main stages:
  * **Backup current scenes**. This only happens when the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) has been modified. Allows Unity to revert the Scenes when exiting Play mode to the state they were in before Play mode started.
  * **Domain reload**. Resets the scripting state, by reloading the scripting domain.
  * **Scene reload**. Resets the Scene state, by reloading the Scene.
  * **Update scene**. This happens twice; once without rendering, and once with rendering.


The combined tasks of domain reload and scene reload resets the scripting domain and simulates the startup behavior of your application as it would run in the Player. Unity skips these steps when you disable them in your **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings).
The following diagram provides detailed information about the exact events which Unity skips when domain reload and scene reload are disabled. Blue indicates the events Unity skips when domain reload is disabled, and green indicates the events Unity skips when scene reload is disabled.
![Event functions in the MonoBehaviour script lifecycle. Event functions skipped when domain reload is disabled are highlighted blue. Event functions skipped when scene reload is disabled are highlighted green.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/EnterPlayModeEvents.svg) Event functions in the MonoBehaviour script lifecycle. Event functions skipped when domain reload is disabled are highlighted blue. Event functions skipped when scene reload is disabled are highlighted green.
## What Unity does when scene reloading and domain reloading are both enabled
With scene reload and domain reload enabled, this is the full list of all processes and events that Unity performs when entering Play mode:
  1. The [AssemblyReloadEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents.html) `beforeAssemblyReload` event is raised.
  2. The C# domain is stopped:  
a. `OnDisable()` is called for all ScriptableObjects and MonoBehaviours.  
b. Unity waits for all async operations to finish.
  3. The state of all MonoBehaviours and ScriptableObjects is serialized.  
a. `OnBeforeSerialize()` is called.  
b. All public and private field values are serialized, except those marked with `[NonSerialized]`.
  4. Managed wrappers are disconnected from native Unity objects.
  5. The Unity Child Domain is reloaded:  
a. Mono domain unload:  
i. The `AppDomain.DomainUnload` event is raised.  
ii. The Unity Child Domain is destroyed  
1. GC and finalizers are called.  
2. Threads are terminated.  
3. All JIT info is deleted.  
b. The new Unity Child Domain is created.
  6. The assemblies are loaded:  
a. System assemblies are loaded.  
b. Unity assemblies are loaded.  
c. User assemblies are loaded.
  7. The synchronization context is initialized.
  8. The scripting state is restored.  
a. The scriptable part of all Unity objects is recreated.  
i. Constructors are called, and statics are assigned their default values.  
b. The state of all Unity objects is deserialized:  
i. The serialized states of all Unity objects are restored.  
1. The `OnAfterDeserialize` event is raised.  
ii. `OnValidate()` is called.  
iii. For **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) using the `[ExecuteInEditMode]` attribute:  
1. `OnEnable()` is called.  
2. `OnDisable()` is called.  
3. `OnDestroy()` is called.
  9. Methods with the [InitializeOnLoad](https://docs.unity3d.com/ScriptReference/InitializeOnLoadAttribute.html) and [InitializeOnLoadMethod](https://docs.unity3d.com/ScriptReference/InitializeOnLoadMethodAttribute.html) are called.
  10. The [AssemblyReloadEvent](https://docs.unity3d.com/ScriptReference/AssemblyReloadEvents.html) `afterAssemblyReload` is called.


## Additional resources
  * [Enter Play mode with domain reload disabled](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)
  * [Enter Play mode with scene reload disabled](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html)
Enter Play mode with scene reload disabled
[](https://docs.unity3d.com/6000.0/Documentation/Manual/running-editor-code-on-launch.html)
Running project code on Editor launch
