* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/macOSIL2CPPScriptingBackend.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/AppleMac.html)
  * [Developing for macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/macosdevelopment.html)
  * Use IL2CPP with macOS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-macos.html)
Deep linking for macOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-delivery.html)
Building and delivering for macOS
# Use IL2CPP with macOS
Describes the use of **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) for macOS applications using Intermediate Language To C++ (./scripting-backends-il2cpp).
IL2CPP is a fully supported scripting back end that you can use as an alternative to Mono when building projects for macOS Player. 
When you use IL2CPP to build a project, Unity converts Intermediate Language (IL) code from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and assemblies to C++ before creating a native binary. Refer to [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) for more information. 
## C++ source code plug-ins for IL2CPP
You can add C++ (.cpp) code files directly into a Unity Project when using the [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html) scripting back end. These C++ files act as plug-ins within the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). If you configure the C++ files to be compatible with macOS Player, Unity compiles them together with C++ code that gets generated from managed assemblies. Refer to [Import and configure plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html) for more information on plug-in configuration.
Generated C++ code links the functions together, removing the need for a separate Dynamic Link Library (DLL). Instead of using the DLL name, use the `"__Internal"` keyword to make the C++ linker responsible for resolving functions rather than loading them at runtime. For example:
```
[DllImport("__Internal")]
private static extern int
CountLettersInString([MarshalAs(UnmanagedType.LPWStr)]string str);

```

You can define this kind of function in NativeFunctions.cpp as follows:
```
extern "C" __declspec(dllexport) int __stdcall CountLettersInString(wchar_t* str)
{
    int length = 0;
    while (*str++ != nullptr)
        length++;
    return length;
}

```

When the linker resolves the function call, errors in the function declaration on the managed side result in a linker error rather than a runtime error. This means that no dynamic loading needs to happen during runtime, with the function called directly from C#. This decreases the performance overhead of a `P/Invoke` call.
## Additional resources
  * [Import and configure plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-macos.html)
Deep linking for macOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-delivery.html)
Building and delivering for macOS
