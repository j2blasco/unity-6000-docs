* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/events-per-frame-optimization.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Handling events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html)
  * Optimizing per-frame updates with an update manager


[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html)
Inspector-configurable custom events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/coroutines.html)
Splitting tasks across frames
# Optimizing per-frame updates with an update manager
Internally, Unity tracks lists of objects interested in its callbacks, such as `Update`, `FixedUpdate` and `LateUpdate`. Unity maintains these lists as intrusive linked lists to ensure that list updates happen in constant time. MonoBehaviour instances are added to or removed from these lists when they are enabled or disabled, respectively.
While it’s convenient to add the appropriate callbacks to the MonoBehaviour instances that require them, this becomes more inefficient as the number of callbacks grows. There is a small but significant overhead to invoking managed-code callbacks from native code. This results both in degraded frame times when invoking large numbers of [per-frame methods](https://docs.unity3d.com/6000.0/Documentation/Manual/time-per-frame-updates.html), and in degraded instantiation times when [instantiating prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html) that contain large numbers of MonoBehaviours. The instantiation overhead is due to the performance overhead of invoking `Awake` and `OnEnable` callbacks on each component in a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab).
When the number of MonoBehaviour instances with per-frame callbacks grows into the hundreds or thousands, it’s advantageous to remove these callbacks and instead have MonoBehaviours (or even standard C# objects) attach to a global update manager singleton. This update manager singleton can then distribute `Update`, `LateUpdate`, and other callbacks to interested objects. This has the additional benefit of allowing code to unsubscribe from callbacks when they otherwise no-op, thereby reducing the number of functions that must be called each frame.
The greatest saving is usually realized by eliminating callbacks which rarely execute. Consider the following pseudo-code:
```
void Update() {
    if(!someVeryRareCondition) { return; }
// … some operation …
}

```

If there are large numbers of MonoBehaviours with `Update` callbacks similar to the previous, then a significant amount of the time consumed running `Update` callbacks is spent switching between native and managed code domains for MonoBehaviour execution that then exit immediately. If these classes instead subscribe to a global Update Manager only while `someVeryRareCondition` is true, and unsubscribe thereafter, then less time is spent both on switching code domains and evaluating the rare condition.
## Additional resources
  * [Event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html)
  * [Execution order of event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html)
Inspector-configurable custom events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/coroutines.html)
Splitting tasks across frames
