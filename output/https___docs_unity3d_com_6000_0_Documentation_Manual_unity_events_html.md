* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Handling events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html)
  * Inspector-configurable custom events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html)
Order of execution for event functions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/events-per-frame-optimization.html)
Optimizing per-frame updates with an update manager
# Inspector-configurable custom events
Unity provides the [UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) API as a Unity-specific alternative to standard C# [events and delegates](https://learn.microsoft.com/en-us/dotnet/standard/events/). The main advantage of Unity events over standard C# events is that Unity events are serializable, meaning you can configure them in the [Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html).
A `UnityEvent` can be added to any `MonoBehaviour` and is executed at runtime like a standard C# delegate. When a `UnityEvent` is declared in a `MonoBehaviour` it appears in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window where you can define callbacks that persist between Edit time and runtime.
Unity events have similar limitations to standard C# delegates:
  * They hold references to the target object, which stops the target object being garbage collected.
  * If you have a managed (C#) `UnityEngine.Object` as the target and the unmanaged (C++) counterpart object has been destroyed, the callback will not be invoked. Refer to [Null references](https://docs.unity3d.com/6000.0/Documentation/Manual/null-reference-exception.html) for more context.


## Configure Unity events
### Prerequisites
  * Create a MonoBehaviour script which includes `using UnityEngine.Events`
  * Declare at least one field of type `UnityEvent`


### Configure callbacks in the Inspector window:
  1. Select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with the script component that contains your declared `UnityEvent` field(s).
  2. Click the + button under the name of an event to add a slot for a callback.
  3. Select the [UnityEngine.Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html) you want to receive the callback. You can use the object selector or drag and drop an object into the field.
  4. Select the function you want to be called when the event happens. The dropdown selector is populated with filtered lists of [appropriate methods](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-events.html#static-dynamic-calls) available on the GameObject and its components.
  5. Repeat steps 1–4 as required to add additional callbacks for the same event.

![Configuring callbacks for events called Trigger Entered and Trigger Exited in the Inspector window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/unityevents-inspector.png) Configuring callbacks for events called Trigger Entered and Trigger Exited in the Inspector window
### Static and dynamic calls
When configuring a `UnityEvent` in the **Inspector** window there are two types of function calls that are supported:
  * **Static** calls are entirely preconfigured at authoring time, with their target and parameter values defined in the Inspector window. When the callback is invoked, the target function is invoked with the parameter values defined in the Inspector. This is appropriate for values that won’t vary at runtime, for example when you want to decrement a health value by a set amount every time a particular **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) occurs. Statically bound functions appear under **Static Parameters** in the function selection list.
  * **Dynamic** calls are invoked programatically from your code, with parameters matching the type of `UnityEvent` being invoked. This is appropriate for values that vary at runtime, for example a `float` representing a variable amount of damage that a character sustains on each attack. The UI filters the callbacks and only shows the dynamic functions with signatures that are valid for the type of `UnityEvent`. For example, if you have a `UnityEvent<string>`, the function selector lists any functions that accept a `string` parameter under the **Dynamic string** header.

![Choosing between static or dynamic functions whose signatures match the event type in the Inspector window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/unityevents-dynamic-static.png) Choosing between static or dynamic functions whose signatures match the event type in the Inspector window
## Generic support in UnityEvent
By default a `UnityEvent` in a `Monobehaviour` binds dynamically to a `void` function. But you can create a `UnityEvent` with up to four generic type parameters as shown in the following example:
```
using UnityEngine;
using UnityEngine.Events;

public class GenericTest : MonoBehaviour
{
    public UnityEvent<int, int, bool, string> myEvent;
    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        if (myEvent == null)
        {
            myEvent = new UnityEvent<int, int, bool, string>();
        }
        myEvent.AddListener(Ping);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.anyKeyDown && myEvent != null)
        {
            myEvent.Invoke(5, 6, true, "Hello");
        }
    }

    void Ping(int i, int j, bool print, string text)
    {
        if (print)
        {
            Debug.Log("Ping: " + text + i + j);
        }
    }
}

```

## Additional resources
  * [Set up doors, triggers, etc. with drag-and-drop events](https://youtu.be/tmmvhxQcbJk)
  * [UnityEvent API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html)
Order of execution for event functions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/events-per-frame-optimization.html)
Optimizing per-frame updates with an update manager
