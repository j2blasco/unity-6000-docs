* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * Compile a static library as a Unity plug-in


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)
Call C/C++/C# functions from Unity C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-example.html)
Create callbacks between Unity C#, JavaScript, and C/C++/C# code
# Compile a static library as a Unity plug-in
You can compile libraries with Emscripten and use the libraries in Unity. It can be more beneficial to call functions from libraries that encapsulate C++ code rather than C++ code directly from the **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) directory. The benefits include: 
  * Your code is easier to integrate with your Web Unity project.
  * Your code can perform better than if you call functions from C++ code, especially for larger libraries.
  * You can reuse the code in various projects.


## Steps to use a static library in Unity
To compile a static library that you can use as a Unity plug-in:
  1. [Download the Emscripten SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html#download-emscripten)
  2. [Configure any existing project scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html#configure-compiler)
  3. [Update your compiler options](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html#compiler-options)
  4. [Compile and import your static library files](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html#import-c-files)
  5. [Call your static library functions from C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-library.html#call-static-libr)


### 1. Download the Emscripten SDK
You must download the Emscripten SDK that matches your version of Unity. 
To find the appropriate version of Emscripten for your Unity version, refer to [Web native plug-ins for Emscripten](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-native-plugins-with-emscripten.html). 
For download links and more information about how to install the Emscripten SDK, refer to [Download and install](https://emscripten.org/docs/getting_started/downloads.html) (Emscripten).
### 2. Configure any existing project scripts
Emscripten works as a replacement for the gcc or clang compiler. If you have existing C/C++ code, you need to make the following changes in your C++ project:
  * Use “emcc” as the C/C++ compiler
  * Use “emar” as the static linker


For more information, refer to the Emscripten documentation on [Compiling and Running Projects](https://emscripten.org/docs/compiling/index.html).
### 3. Update your compiler options
You might need to add some compiler options to your C/C++ project if your Unity project has the following **Player** settings (menu: **Edit** > **Project Settings** > **Player**). 
Property | Description  
---|---  
**Enable Exceptions** | If this property is set to **None** , add the compiler option “-fno-exceptions”.  
**Enable Native C/C++ Multithreading** | If this property is enabled, include the compiler option “-pthread”.  
**Enable WebAssembly 2023** | If this property is enabled, include the following compiler options: 
  * “-fwasm-exceptions”
  * “-sSUPPORT_LONGJMP=wasm”
  * “-mbulk-memory”
  * “-mnontrapping-fptoint”
  * “-msimd128”
  * “-msse4.2”

  
### 4. Compile and import your static library files
Compile your static library files and then import your files into your Unity project in the `Assets/Plugins` folder.
**Note** : If you don’t have a **Plugins** folder, you need to create your own. 
### 5. Call your static library functions from Unity C# scripts
You can call your static library functions from your Unity C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). The way to call the functions is the same as if you call a C or C++ function from C# scripts. For an example, refer to [Call C/C++/C# functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html).
## Additional resources
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * [Set up your JavaScript plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js.html)
  * [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
  * [Call Unity C# script functions from JavaScript](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html)
  * [Create callbacks between Unity C#, JavaScript, and C/C++/C# code](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-example.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)
Call C/C++/C# functions from Unity C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-example.html)
Create callbacks between Unity C#, JavaScript, and C/C++/C# code
