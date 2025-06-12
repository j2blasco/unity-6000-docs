* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * Organizing scripts into assemblies


[](https://docs.unity3d.com/6000.0/Documentation/Manual/test-conditional-compilation.html)
Test conditional compilation
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-intro.html)
Introduction to assemblies in Unity
# Organizing scripts into assemblies
Assemblies are individual units of compiled code that group types and resources together. Organizing **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) into assemblies has important advantages, especially as your codebase grows.
Assemblies help you think clearly about the architecture of your code and about managing dependencies. By exercising fine-grained control over references, you can reduce unnecessary recompilation time and make your code easier to debug.
**Topic** | **Description**  
---|---  
[Introduction to assemblies in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-intro.html) | Understand the fundamentals of how assemblies work in Unity and why using them to organize your scripts is beneficial.  
[Creating assembly assets](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html) | Create various kinds of assembly assets to customize your assemblies.  
[Referencing assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html) | Set up references between assemblies, override the default references and understand the limitations Unity places on references.  
[Conditionally including assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html) | Use scripting symbols to conditionally include or exclude assemblies from compilation.  
[Assembly metadata and compilation details](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html) | Define metadata for your assemblies.  
[Assembly Definition properties reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html) | Inspector-editable properties of assembly defintion assets and their meaning.  
[Assembly Definition Reference properties reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html) | Inspector-editable properties of assembly defintion reference assets and their meaning.  
[Assembly Definition file format reference](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html) | Assembly definition file format reference.  
## Additional resources
  * [Special folders and script compilation order](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compile-order-folders.html)
  * [Scripting backends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/test-conditional-compilation.html)
Test conditional compilation
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-intro.html)
Introduction to assemblies in Unity
