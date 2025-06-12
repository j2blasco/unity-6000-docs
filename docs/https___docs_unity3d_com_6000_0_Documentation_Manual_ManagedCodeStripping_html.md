* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ManagedCodeStripping.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * Managed code stripping


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)
Assembly Definition File Format reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-linker.html)
Managed code stripping and the Unity linker
# Managed code stripping
During the build process, Unity removes unused or unreachable code through a process called managed code stripping, which can significantly decrease your application’s final size. Managed code stripping removes code from managed assemblies, including assemblies built from the C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) in your project, assemblies that are part of packages and plugins, and assemblies in .NET Framework.
Unity uses a tool called the Unity linker to perform a static analysis of the code in your project’s assemblies. The static analysis identifies any classes, portions of classes, functions, or portions of functions that can’t be reached during execution. This analysis only includes code that exists at build time because code generated at runtime doesn’t exist when Unity performs the static analysis.
You can configure the level of code stripping Unity performs for your project in the Unity Editor. You can also provide annotations in the form of attributes or a special XML configuration file to instruct the Unity linker about which parts of your code base to preserve.
**Topic** | **Description**  
---|---  
[Managed code stripping and the Unity linker](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-linker.html) | Understand how the Unity linker analyzes and marks elements of your code before stripping.  
[Configure managed code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-configure.html) | Configure managed code stripping in the Unity Editor and understand what Unity does at each stripping level.  
[Preserving code using annotations](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-preserving.html) | Use annotations in the form of C# attributes or a `link.xml` file to specify which parts of your code the Unity linker should not strip.  
[Link XML formatting reference](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-xml-formatting.html) | Understand how to format a `link.xml` file, including supported XML elements and attributes and examples of their usage.  
[Unity linker marking rules reference](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-marking-rules.html) | Understand the marking rules the Unity linker applies at each managed stripping level to determine which parts of your code assemblies to strip.  
## Additional resources
  * [Scripting backends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)
Assembly Definition File Format reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-linker.html)
Managed code stripping and the Unity linker
