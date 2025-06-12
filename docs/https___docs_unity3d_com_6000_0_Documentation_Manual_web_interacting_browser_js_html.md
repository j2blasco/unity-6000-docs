* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * Set up your JavaScript plug-in


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-code-example.html)
Code examples: Call JavaScript and C/C++/C# functions in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
Call JavaScript functions from Unity C# scripts
# Set up your JavaScript plug-in
You can call functions from your JavaScript plug-ins in your Unity projects. Unity supports two JavaScript **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) file types that let you add JavaScript code to your Unity project:
  * .jslib
  * .jspre


**Note** : Unity currently supports [ECMAScript 5 (ES5) syntax](https://www.w3schools.com/js/js_es5.asp) in .jslib and .jspre files. [ES6 syntax](https://www.w3schools.com/js/js_es6.asp) isn’t yet supported.
If you want to call functions from C++ plug-ins instead, refer to [Call C/C++/C# functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html).
## Import your JavaScript files into your Unity project
The recommended way to use browser JavaScript in your project is to add your JavaScript sources (.jspre and .jslib files) to your project, and then use those functions or libraries directly in your Unity C# script code.
Place your JavaScript plug-in files in any folder, such as `Assets/JSPlugins`.
## Call functions from the .jslib file type
You can call functions from your .jslib plug-in files in your Unity C# or native **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
The .jslib file type uses the `--js-library` Emscripten module. For more information, refer to the Emscripten documentation about the [–js-library Emscripten option](https://emscripten.org/docs/tools_reference/emcc.html#emcc-js-library).
The following code shows an example of a .jslib plug-in file with the ideal syntax that defines some functions (`Hello` and `HelloString`).
```
mergeInto(LibraryManager.library, {

  Hello: function () {
    window.alert("Hello, world!");
  },

  HelloString: function (str) {
    window.alert(UTF8ToString(str));
  },
});

```

You can then call these functions in your Unity C# code:
```
using UnityEngine;
using System.Runtime.InteropServices;

public class NewBehaviourScript : MonoBehaviour {

    [DllImport("__Internal")]
    private static extern void Hello();

    [DllImport("__Internal")]
    private static extern void HelloString(string str);

    void Start() {
        Hello();
        HelloString("This is a string.");
    }
}

```

For a full example of code interactions between Unity C# and JavaScript functions, refer to [Code examples: Call JavaScript and C/C++/C# functions in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-code-example.html).
For more information about interactions between Unity C# and JavaScript, refer to [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html#example-unity-code).
## Include JavaScript libraries with the .jspre file type
Use the .jspre plug-in file type to include existing JavaScript libraries in your JavaScript code. You can’t use Unity code to interact with the .jspre files, but you can use them in the .jslib code.
The .jspre file type uses the `--pre-js` Emscripten option. For more information, refer to the Emscripten documentation about the [–pre-js Emscripten option](https://emscripten.org/docs/tools_reference/emcc.html#emcc-pre-js).
During the build process, Emscripten creates the `*.framework.js` file and copies the contents of the .jspre file into the start of the `*.framework.js` file. This process is useful because all the code is combined into one file so it’s easier to manage the files and the code benefits from Emscripten optimizations.
## Additional resources
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
  * [Call Unity C# script functions from JavaScript](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html)
  * [Call C/C++/C# functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)
  * [Create callbacks between Unity C#, JavaScript, and C/C++/C# code](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-example.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-code-example.html)
Code examples: Call JavaScript and C/C++/C# functions in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
Call JavaScript functions from Unity C# scripts
