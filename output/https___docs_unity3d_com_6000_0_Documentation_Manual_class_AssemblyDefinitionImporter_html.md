* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
  * Assembly Definition properties reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html)
Assembly metadata and compilation details
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
Assembly Definition Reference properties reference
# Assembly Definition properties reference
Click on an Assembly Definition Asset to set the properties for an assembly in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
Assembly Definition properties are divided into the following sections:
  * [Name and General](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#name)
  * [Define Constraints](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#define-constraints)
  * [Assembly Definition References](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#asmdef-references)
  * [Assembly References](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#assembly-references)
  * [Platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#platforms)
  * [Version Defines](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#version-defines)


## Name and General
![The Name and General sections of configurable properties in the Assembly Definition importer Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/name-and-general.png) The Name and General sections of configurable properties in the Assembly Definition importer Inspector window. **Property:** | **Description:**  
---|---  
**Name** | The name for the assembly (without a file extension). Assembly names must be unique across the Project. Consider using a reverse-DNS naming style to reduce the chance of name conflicts, especially if you want to use the assembly in more than one Project.  
  
**Note** : Unity uses the name you assign to the Assembly Definition asset as the default value of the Name field, but you can change the name as needed. However, if you reference an Assembly Definition by its name rather than its GUID, changing the name will break the reference.  
**Allow ‘unsafe’ Code** | Enable the Allow ‘unsafe’ Code option if you have used the C# `unsafe` keyword in a script within the assembly. When you enable this setting, Unity passes the /unsafe option to the C# compiler when it compiles the assembly.  
**Auto Referenced** | Specify whether the predefined assemblies should reference this Project assembly. When you disable the Auto Reference option, Unity does not automatically reference the assembly during compilation. This has no effect on whether Unity includes it in the build.  
**No Engine References** | When you enable this property, Unity does not add references to UnityEditor or UnityEngine when it compiles the assembly.  
**Override References** | Enable the Override References setting to manually specify which precompiled assemblies this assembly depends upon. When you enable Override References, the Inspector shows the Assembly References section, which you can use to specify the references.  
  
A precompiled assembly is a library compiled outside your Unity Project. By default, assemblies you define in your Project reference all the precompiled assemblies you add to the Project, which matches how the predefined assemblies reference all precompiled assemblies. When you enable Override References, this assembly only references the precompiled assemblies you add under Assembly References.  
  
**Note** : To prevent Project assemblies from automatically referencing a precompiled assembly, you can disable its Auto Referenced option. See Plugin Inspector for more information.  
**Root Namespace** | The default namespace for ****scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts)** in this assembly definition. If you use either [Rider] or [Visual Studio] as your code editor, they automatically add this namespace to any new scripts you create in this assembly definition.  
For more information, refer to [Creating an Assembly Definition asset](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html#create-asmdef).
## Define Constraints
![A list of preprocessor symbols configured in the Define Constraints section of the Assembly Definition importer Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/define-constraints.png) A list of preprocessor symbols configured in the Define Constraints section of the Assembly Definition importer Inspector window.
Define constraints specify the compiler #define directives that must be defined for Unity to compile or reference an assembly.
Unity only compiles and references a Project assembly if all of the Define Constraints are satisfied. Constraints work like the #if preprocessor directive in C#, but on the assembly level instead of the script level. Define all the symbols in the Define Constraints setting for the constraints to be satisfied.
To specify that a symbol must be undefined, prefix it with a negating ! (bang) symbol. For example, if you specify the following symbols as the Define Constraints:
  * `!ENABLE_IL2CPP`
  * `UNITY_2018_3_OR_NEWER`


The constraints are satisfied when the symbol `ENABLE_IL2CPP` is not defined and the symbol `UNITY_2018_3_OR_NEWER` is defined. The result is that Unity only compiles and references this assembly on non-IL2CPP scripting runtimes for Unity 2018.3 or newer.
You can use the || (OR) operator to specify that at least one of the constraints must be present in order for the constraints to be satisfied. For example:
  * `UNITY_IOS || UNITY_EDITOR_OSX`
  * `UNITY_2019_3_OR_NEWER`
  * `!UNITY_ANDROID`


The constraints are satisfied when either `UNITY_IOS` or `UNITY_EDITOR_OSX` and `UNITY_2019_3_OR_NEWER` are defined and `UNITY_ANDROID` is not defined. Individual lines are analogous to performing a logical AND operation between the constraints in them. The above example is equivalent to:
`(UNITY_IOS OR UNITY_EDITOR_OSX) AND (UNITY_2019_3_OR_NEWER) AND (NOT UNITY_ANDROID)`
You can use any of Unity’s built-in #define directives, symbols defined in a global compiler response (.rsp) file, and any symbols defined in the Project’s Scripting Define Symbols Player setting. For more information, refer to [Platform dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html), including a list of the built-in symbols.
**Note** : The Scripting Define Symbols settings are platform-specific. If you use this setting to define whether Unity should use an assembly, make sure that you define the necessary symbols on all the relevant platforms.
For more information, refer to [Conditionally including an assembly](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html).
### Invalid or incompatible constraints
Unity marks each constraint with an indicator based on the currently defined settings (for example, the following set of three constraints indicates that the first symbol is currently defined while the other two are not). Since each individual constraint must be true for the overall constraint to be satisfied, the Editor marks the entire Define Constraints section as currently incompatible or invalid.
![Invalid or incompatible constraints flagged in the Define Constraints section of the Assembly Definition importer Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/invalid-constraints.png) Invalid or incompatible constraints flagged in the Define Constraints section of the Assembly Definition importer Inspector window.
To satisfy the constraints in this example, you could change the ****Scripting Backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend)** to ****IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP)** for the second constraint (in **Player Settings**) and remove the invalid characters from the third constraint. However, what often matters is how the constraints are evaluated when you build the project, not how the constraints appear in the Unity Editor (for example, you might have an assembly that you only want to include in builds that use the IL2CPP backend, but not on other builds that use the Mono backend).
## Assembly Definition References
![A list of configured references in the Assembly Definition References section of the Assembly Definition importer Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/assembly-definition-ref.png) A list of configured references in the Assembly Definition References section of the Assembly Definition importer Inspector window. **Property:** | **Description:**  
---|---  
**Assembly Definition References** | Specify references to other assemblies that you have created using Assembly Definition assets. Unity uses these references to compile the assembly and also define the **dependencies** between assemblies.  
**Use GUIDs** | This setting controls how Unity serializes references to other Assembly Definition assets. When you enable this property, Unity saves the reference as the asset’s GUID, instead of the Assembly Definition name. It’s good practice to use the GUID instead of the name, because it means you can make changes to the name of an Assembly Definition asset without having to update other Assembly Definition files that reference it.  
For more information, refer to [Creating an Assembly Definition asset](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html#create-asmdef).
## Assembly References
![The Assembly References section of the Assembly Definition importer Inspector window with configured references to Newtonsoft JSON and NUnit libraries.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/assembly-ref.png) The Assembly References section of the Assembly Definition importer Inspector window with configured references to Newtonsoft JSON and NUnit libraries.
The Assembly References section only appears when you enable the **Override References** property (in the [General] section). Use this area to specify any references to precompiled assemblies on which this assembly depends.
For more information, refer to [Referencing a precompiled, plugin assembly](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html#reference-precompiled-assembly).
## Platforms
![The Platforms section of the Assembly Definition importer Inspector window with Any Platform, iOS, macOS, and tvOS platforms selected.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/platforms.png) The Platforms section of the Assembly Definition importer Inspector window with Any Platform, iOS, macOS, and tvOS platforms selected.
Set the platform compatibility of the assembly. Unity only compiles or references this assembly on the included (or not excluded) platforms.
For more information, refer to [Creating a platform-specific assembly](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html#create-platform-specific).
## Version Defines
![The Version Defines section of the Assembly Definition importer Inspector window, with defines configured for specific versions of the Unity Test Framework and VS Code packages.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/version-defines.png) The Version Defines section of the Assembly Definition importer Inspector window, with defines configured for specific versions of the Unity Test Framework and VS Code packages.
Specify which symbols to define according to the versions of the packages and modules in a project.
**Property:** | **Description:**  
---|---  
**Resource** | A package or module  
**Define** | The symbol to define when an applicable version of the Resource is also present in this Unity Project.  
**Expression** | An expression defining a version or range of versions. For more information, refer to [Version Defines](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#version-defines).  
**Expression outcome** | The Expression evaluated as a logical statement, where “x” is the version checked. If the Expression outcome says, Invalid, then the Expression is malformed.  
For more information, refer to [Defining symbols based on project packages](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html#define-symbols).
## Additional resources
  * [Creating assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
  * [Referencing assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html)
  * [Assembly Definition Reference properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html)
Assembly metadata and compilation details
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
Assembly Definition Reference properties reference
