* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-intro.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
  * Introduction to assemblies in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
Organizing scripts into assemblies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
Creating assembly assets
# Introduction to assemblies in Unity
Unity provides two special asset types, Assembly Definitions and Assembly References, to help organize your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) into assemblies.
An assembly is a C# code library that contains the compiled classes and structs that are defined by your scripts and which also define references to other assemblies. Refer to [Assemblies in .NET](https://learn.microsoft.com/en-us/dotnet/standard/assembly/) for more information about assemblies in C#.
By default, Unity compiles almost all of your game scripts into a predefined assembly called `Assembly-CSharp.dll`. Unity also creates a [few smaller, specialized predefined assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compile-order-folders.html).
This arrangement works acceptably for small projects, but has some drawbacks as you add more code to your project:
  * Every time you change one script, Unity has to recompile all the other scripts, increasing overall compilation time for iterative code changes.
  * Any script can directly access types defined in any other script, which can make it more difficult to refactor and improve your code.
  * All scripts are compiled for all platforms.


By defining assemblies, you can organize your code to promote modularity and reusability. Scripts in assemblies you define are no longer added to the default assemblies and can only access scripts in your other custom assemblies.
![A conceptual illustration of organizing scripts into multiple custom assemblies as an alternative to compiling them all in the default assembly. An arrow points from the default assembly, Assembly-Csharp, to an alternative setup in which a custom Main assembly directly references two other custom assemblies called Stuff and ThirdParty. Stuff in turn references a fourth custom assembly called Library.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScriptCompilation.png) A conceptual illustration of organizing scripts into multiple custom assemblies as an alternative to compiling them all in the default assembly. An arrow points from the default assembly, Assembly-Csharp, to an alternative setup in which a custom Main assembly directly references two other custom assemblies called Stuff and ThirdParty. Stuff in turn references a fourth custom assembly called Library.
The above diagram illustrates how you might split up the code in your project into multiple assemblies. Because _Main_ references _Stuff_ and not the other way around, you know that any changes to the code in _Main_ cannot affect the code in _Stuff_. Similarly, because _Library_ doesn’t depend on any other assemblies, you can more easily reuse the code in _Library_ in another project.
## Defining assemblies
To organize your project code into assemblies, create a folder for each desired assembly and move the scripts that should belong to each assembly into the relevant folder. Then [create Assembly Definition assets](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html) to specify the assembly properties.
Unity compiles all the scripts in a folder that contains an Assembly Definition into a single assembly, using the name and other settings defined by the asset. The assembly includes any scripts in subfolders unless a subfolder has its own Assembly Definition or Assembly Reference asset. 
To include scripts from a non-child folder in an existing assembly, create an Assembly Reference asset in the non-child folder and set it to reference the Assembly Definition asset that defines the target assembly. For example, you can combine the scripts from all the Editor folders in your project in their own assembly, no matter where those folders are located.
Unity compiles assemblies in an order determined by their dependencies. You can’t specify the order in which compilation takes place.
## Finding which assembly a script belongs to
To identify which assembly a script belongs to, select the script file in the **Project** window to view its properties in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window. The assembly filename and the Assembly Definition, if one exists, are shown in the **Assembly Information** section of the **Inspector**.
## Editor folder
Unity normally compiles any scripts in folders named `Editor` into the predefined `Assembly-CSharp-Editor` assembly no matter where those scripts are located. However, if you create an Assembly Definition asset in a folder that has an Editor folder underneath it, Unity no longer puts those Editor scripts into the predefined Editor assembly. Instead, they go into the new assembly created by your Assembly Definition — where they might not belong. To manage `Editor` folders, you can create Assembly Definition or Reference assets in each `Editor` folder to place those scripts in one or more Editor assemblies. For more information, refer to [Creating an assembly for Editor code](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html#create-editor-assembly).
## Additional resources
  * [Creating assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
  * [Referencing assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html)
  * [Assembly metadata and compilation details](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html)
  * [Assembly Definition properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
  * [Assembly Definition Reference properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
Organizing scripts into assemblies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
Creating assembly assets
