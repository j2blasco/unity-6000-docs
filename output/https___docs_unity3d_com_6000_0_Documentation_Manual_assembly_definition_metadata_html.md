* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
  * Assembly metadata and compilation details


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html)
Conditionally including assemblies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
Assembly Definition properties reference
# Assembly metadata and compilation details
You can define additional metadata for your assemblies and retrieve information on the assemblies included in a project build.
## Setting assembly attributes
You can use assembly attributes to set metadata properties for your assemblies. By convention, assembly attribute statements are typically put in a file named `AssemblyInfo.cs`.
For example, the following assembly attributes specify a few [.NET assembly metadata values], an `[InternalsVisibleTo]` attribute, which can be useful for testing, and the Unity-defined [Preserve attribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PreserveAttribute.html) that affects how unused code is removed from an assembly when you build your project:
```
[assembly: System.Reflection.AssemblyCompany("Bee Corp.")]
[assembly: System.Reflection.AssemblyTitle("Bee's Assembly")]
[assembly: System.Reflection.AssemblyCopyright("Copyright 2020.")]
[assembly: System.Runtime.CompilerServices.InternalsVisibleTo("UnitTestAssembly")]
[assembly: UnityEngine.Scripting.Preserve]

```

## Getting assembly information in build scripts
Use the [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html) class to retrieve information about all assemblies built by Unity for a project, including those created based on Assembly Definition assets.
For example, the following script uses the `CompilationPipeline` class to list all the current Player assemblies in a project:
```
using UnityEditor;
using UnityEditor.Compilation;
public static class AssemblyLister
{
    [MenuItem("Tools/List Player Assemblies in Console")]
    public static void PrintAssemblyNames()
    {
        UnityEngine.Debug.Log("== Player Assemblies ==");
        Assembly[] playerAssemblies =
            CompilationPipeline.GetAssemblies(AssembliesType.Player);

        foreach (var assembly in playerAssemblies)
        {
            UnityEngine.Debug.Log(assembly.name);
        }
    }
}

```

## Additional resources
  * [Creating assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
  * [Referencing assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html)
  * [Assembly Definition properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
  * [Assembly Definition Reference properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html)
Conditionally including assemblies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
Assembly Definition properties reference
