* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Code and scene reload on entering Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/code-reloading-editor.html)
  * Enter Play mode with scene reload disabled


[](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)
Enter Play mode with domain reload disabled
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html)
Details of disabling domain and scene reload
# Enter Play mode with scene reload disabled
Scene reload on entering Play mode is enabled by default. This means that when you enter Play mode, Unity destroys all existing **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and reloads the scene from disk. As your project gets more complex, the time between pressing the Play button and the scene fully loading in the Editor increases.
When you disable scene reloading, the process takes less time. Instead of reloading the scene from disk, Unity only resets the scene’s modified contents. Unity still calls the same [event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) (such as `OnEnable`, `OnDisable` and `OnDestroy`) as if the scene were freshly loaded.
## Effects of disabling scene reload when entering Play mode
When you [disable scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html#configure-play-mode), the time it takes to start your application in the Editor is no longer representative of the startup time in the built version. If you want to debug or profile exactly what happens during your project’s startup, you should enable scene reloading to more accurately represent the true loading time and processes that happen in the built version of your application.
Otherwise, disabling scene reload should have minimal effects on your project. However, because scene reloading is closely connected to domain reload, there are a few important differences:
  * Unity doesn’t recreate existing objects or call constructors, which means non-serialized fields keep the values assigned to them during Play mode on returning to Edit mode. This applies for fields of all script types, including MonoBehaviours, ScriptableObjects, and your own custom C# types. For detailed information on what is and isn’t serialized in different contexts, refer to [Serialization rules](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html). 
    * **Note** : `private` fields are not serialized as part of the regular build pipeline but **are** serialized as part of the Editor’s [hot reloading of scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html#hot-reload). This is why `private` fields you modify in Play mode might reset to their original values on exiting Play mode even when scene and domain reload on enter Play mode are disabled.
  * Unity converts null `private` and `internal` fields of array and `List` type to an empty array or `List` object during domain reload and they stay non-null for runtime (non-Editor) **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
  * Scripts decorated with [`[ExecuteInEditMode]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html) or [`[ExecuteAlways]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteAlways.html) don’t receive `OnDestroy` or `Awake` calls. While in Edit mode, these scripts might modify their own fields or those of other runtime scripts. To mitigate this, you can initialize any affected fields in an `OnEnable` callback with code inside a condition that checks the value of [`EditorApplication.isPlaying`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.isPlaying.html). For an example of this and more context on the importance of separating Play mode and Edit mode code, refer to the [`[ExecuteAlways]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteAlways.html) API description.


For more details on the events skipped with scene reload disabled, refer to [Details of disabling domain and scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html).
## Additional resources
  * [Configuring code reload on entering Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html)
  * [Enter Play mode with domain reload disabled](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)
  * [Details of disabling domain and scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)
Enter Play mode with domain reload disabled
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html)
Details of disabling domain and scene reload
