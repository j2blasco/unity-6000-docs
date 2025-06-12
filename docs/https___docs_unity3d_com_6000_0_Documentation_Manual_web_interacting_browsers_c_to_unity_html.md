* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * Call C/C++/C# functions from Unity C# scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html)
Call Unity C# script functions from JavaScript
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html)
Compile a static library as a Unity plug-in
# Call C/C++/C# functions from Unity C# scripts
You can call functions from your C, C++, or C# **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) in your Unity projects. 
Unity uses Emscripten to compile your sources into WebAssembly from C/C++/C# code, so you can write plug-ins in C/C++/C# code and call these functions from your Unity C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). 
To call functions from your JavaScript plug-ins instead, refer to [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html). 
## Import your C/C++/C# plug-in into your Unity project
To allow your Unity project to call functions from your C/C++/C# plug-in code, you need to import your plug-in into your Unity project. 
Place your JavaScript plug-in files in any folder, such as `Assets/JSPlugins`. 
## Example C++ code that you can use in Unity
If you use C++ (.cpp) to implement the plug-in, you must declare the functions with C linkage (`extern “C”`) to avoid name mangling issues. The following code is an example C++ plug-in with simple functions that you can call in your Unity project. 
```
#include <stdio.h>

extern "C" void Hello ()
{
    printf("Hello, world!\n");
}

extern "C" int AddNumbers (int x, int y)
{
    return x + y;
}

```

**Note** : Unity uses the Emscripten version 2.0.19 toolchain.
Use the following Unity C# code in your Unity project to call the C++ functions. 
```
using UnityEngine;
using System.Runtime.InteropServices;

public class NewBehaviourScript : MonoBehaviour {

    [DllImport("__Internal")]
    private static extern void Hello();

    [DllImport("__Internal")]
    private static extern int AddNumbers(int x, int y);

    void Start() {
        Hello();
        
        int result = AddNumbers(5, 7);
        Debug.Log(result);  
    }
}

```

## Additional resources
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * [Set up your JavaScript plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js.html)
  * [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
  * [Call Unity C# script functions from JavaScript](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html)
  * [Create callbacks between Unity C#, JavaScript, and C/C++/C# code](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-example.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html)
Call Unity C# script functions from JavaScript
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html)
Compile a static library as a Unity plug-in
