* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)
  * Native plug-ins


[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html)
Managed plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html)
Building plug-ins for desktop platforms
# Native plug-ins
Unity supports native **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), which are libraries of native code you can write in languages such as C, C++, and Objective-C. Plug-ins allow the code you write in C# to call functions from these libraries. This feature allows Unity to integrate with middleware libraries or existing C/C++ code.
The **native plug-in** A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in) provides a simple C interface, which the C# script then exposes to your other **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). Unity can also call functions that the native plug-in exports when certain low-level rendering events happen (for example, when you create a graphics device). For more information, refer to [Low-level native plug-in interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).
For an example of a native plug-in, refer to [Native Renderer Plugin](https://github.com/Unity-Technologies/NativeRenderingPlugin).
## Using a native plug-in
To use a native plug-in:
  1. Write functions in a C-based language to access the features you need.
  2. Compile them into a library.
  3. In Unity, create a C# script that calls functions in the native library.


You build native plug-ins with native code compilers on the target platform. Because plug-in functions use a C-based call interface, you must declare the functions with C linkage to avoid name mangling issues.
For platform-specific information on native plug-ins, refer to the relevant section under [Platform development](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html).
## Example
A simple native library with a single function might have code that looks like this:
`float ExamplePluginFunction () { return 5.0F; }`
To access this code from within Unity, use the following C# script:
```
using UnityEngine;
using System.Runtime.InteropServices;

class ExampleScript : MonoBehaviour {
    #if UNITY_IPHONE
    // On iOS plugins are statically linked into
    // the executable, so we have to use __Internal as the
    // library name.
    [DllImport ("__Internal")]
    #else
    // Other platforms load plugins dynamically, so pass the
    // name of the plugin's dynamic library.
    [DllImport ("PluginName")]   
    #endif
    private static extern float ExamplePluginFunction ();

    void Awake () {
        // Calls the ExamplePluginFunction inside the plugin
        // And prints 5 to the console
        print (ExamplePluginFunction ());
       }
    }

```

## Additional resources
  * [Low-level native plug-in interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html)
  * [Mono Interop with native libraries](https://www.mono-project.com/docs/advanced/pinvoke/)
  * [P-invoke documentation on MSDN](https://docs.microsoft.com/en-us/dotnet/framework/interop/marshaling-data-with-platform-invoke?redirectedfrom=MSDN)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html)
Managed plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html)
Building plug-ins for desktop platforms
