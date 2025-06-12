* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Debugging and diagnostics](https://docs.unity3d.com/6000.0/Documentation/Manual/debugging-and-diagnostics.html)
  * The Debug class


[](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html)
Debug C# code in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html)
Log files reference
# The Debug class
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html "Go to Debug page in the Scripting Reference")
The Debug class allows you to visualize information in the Unity Editor that might help you understand or investigate what is going on in your project while it’s running. For example, you can use it to print messages into the Console window, draw visualization lines in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view and Game view, and pause Play mode in the Editor from script.
This page provides an overview of the Debug class and its common uses when scripting with it. For an exhaustive reference of every member of the Debug class, refer to the [Debug script reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).
## Logging errors, warnings and messages
Unity sometimes logs errors, warnings, and messages to the Console window. The `Debug` class provides you with the ability to do exactly the same from your own code, as shown in the following example:
```
Debug.Log("This is a log message.");
Debug.LogWarning("This is a warning message!");
Debug.LogError("This is an error message!");

```

The three types (error, warning, and message) each have their own icon type in the Console window.
![The Console window displays the three types of debug message: a regular log with a white exclamation icon, a warning with a yellow exclamation icon, and an error with a red exclamation icon.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ConsoleShowingMessageWarningAndError.png) The Console window displays the three types of debug message: a regular log with a white exclamation icon, a warning with a yellow exclamation icon, and an error with a red exclamation icon.
Everything that is written to the Console Window (by Unity, or your own code) is also written to a [Log File](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html).
If **Error Pause** is enabled in the Console, any errors written to the Console via the `Debug` class cause Play mode to pause.
You can also provide a second optional parameter to these log methods to indicate that the message is associated with a particular **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), like the following:
```
using UnityEngine;

public class DebugExample : MonoBehaviour
{    void Start()
    {
        Debug.LogWarning("I come in peace!", this.gameObject);
    }
}

```

The benefit of this is that when you click the message in the console, the GameObject you associated with that message is highlighted in the Hierarchy, allowing you to identify which GameObject the message related to. In the following image, selecting the `I come in peace!` warning message highlights the **Alien (8)** GameObject.
![The Console window displays I come in peace! as a warning-level log message.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ConsoleMessageWithContextGameObject.png) The Console window displays “I come in peace!” as a warning-level log message.
## Using the Debug class
The `Debug` class has two methods for drawing lines in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) and Game view. These are [`DrawLine`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html) and [`DrawRay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html).
In this example, a script has been added to every Sphere GameObject in the scene, which uses `Debug.DrawLine` to indicate its vertical distance from the plane where Y equals zero. Note that the last parameter in this example is the duration in seconds that the line stays visible in the Editor.
```
using UnityEngine;

public class DebugLineExample : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        float height = transform.position.y;
        Debug.DrawLine(transform.position, transform.position - Vector3.up * height, Color.magenta, 4);
    }
}

```

And the result in the Scene view looks like this:
![The Scene view displays a group of spheres, each with a magenta line indicating its distance from the plane where Y equals zero.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/DebugDrawLineExampleInScene.png) The Scene view displays a group of spheres, each with a magenta line indicating its distance from the plane where Y equals zero.
### Excluding Debug code from non-development builds
The [`UnityEngine.Debug`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) logging APIs aren’t stripped from [release builds](https://docs.unity3d.com/6000.0/Documentation/Manual/build-types.html), and write to log files if called. You can prevent this by using `#if` directives or a conditional attribute to make compilation of `Debug` calls dependent on a scripting symbol that’s only defined in **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild).
The following example uses a conditional attribute with a scripting symbol called `ENABLE_LOGS` that is only defined in development builds:
```

    public static class Logger {

        [Conditional("ENABLE_LOGS")]
        public static void Debug(string logMsg) {
            UnityEngine.Debug.Log(logMsg);
        }
    }

```

For more information, refer to [Conditional compilation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).
## Additional resources
  * [Console window](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Consolewindow)
  * [Log files](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html)
Debug C# code in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html)
Log files reference
