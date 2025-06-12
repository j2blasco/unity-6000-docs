* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/running-editor-code-on-launch.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * Running project code on Editor launch


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html)
Details of disabling domain and scene reload
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
Script serialization
# Running project code on Editor launch
Sometimes it can be useful to make parts of your Edit mode project code run immediately when the Unity Editor launches without requiring any user action. You can do this by applying the [InitializeOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html) attribute to a class which has a static constructor. A static constructor is a function with the same name as the class, declared `static` and without a return type or parameters. For more information, refer to [Static constructors](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-constructors) in the Microsoft C# documentation.
```
using UnityEngine;
using UnityEditor;

[InitializeOnLoad]
public class Startup {
    static Startup()
    {
        Debug.Log("Up and running");
    }
}


```

A static constructor is always guaranteed to be called before any static function or instance of the class is used, but the `InitializeOnLoad` attribute ensures it’s called when the Editor launches. Static constructors with this attribute are called when **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) in the project are recompiled, also known as a [domain reload](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html). This happens when:
  * Unity first loads your project.
  * Unity detects modifications to scripts, if **Auto Refresh** is enabled in the Asset Pipeline section of the [Preferences window](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html).
  * Entering Play Mode, if Domain Reload is enabled in your [Play Mode configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html).


An example use of the initialize on load functionality is setting up a regular callback which could be thought of as a sort of “frame update” for the Editor application. The [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html) class has a delegate called [update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) which is called many times per second while the Editor is running. The following code example defines a small custom class decorated with `[InitializeOnLoad]` and assigns a member method to the `EditorApplication.update` delegate so that it runs and begins printing `Updating` to the console on Editor launch:
```
using UnityEditor;
using UnityEngine;

// InitializeOnLoad ensures this code runs on Editor launch
[InitializeOnLoad]
class MyClass
{
    // Define a static constructor in which we assign the custom Update method to the delegate
    static MyClass ()
    {
        EditorApplication.update += Update;
    }

    // Define a method with the required signature that performs work we want to do on launch
    static void Update ()
    {
        Debug.Log("Updating");
    }
}


```

## Additional resources
  * [Configurable Enter Play Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html)
  * [Domain Reloading](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)
  * [InitializeOnLoadAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html)
Details of disabling domain and scene reload
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
Script serialization
