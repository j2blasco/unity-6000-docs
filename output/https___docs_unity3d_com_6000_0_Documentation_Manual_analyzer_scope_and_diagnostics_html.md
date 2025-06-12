* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/analyzer-scope-and-diagnostics.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Debugging and diagnostics](https://docs.unity3d.com/6000.0/Documentation/Manual/debugging-and-diagnostics.html)
  * [Roslyn analyzers and source generators](https://docs.unity3d.com/6000.0/Documentation/Manual/roslyn-analyzers.html)
  * Analyzer scope and diagnostics


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ruleset-files.html)
Create rule set files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
Optimization
# Analyzer scope and diagnostics
## Analyzer scope
You can limit the scope of analyzers in your project by using assembly definitions, so that they only analyze certain portions of your code.
Unity applies analyzers to all assemblies in your project’s Assets folder, or in any subfolder whose parent folder doesn’t contain an [assembly definition file](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html). If an analyzer is in a folder that contains an assembly definition, or a subfolder of such a folder, the analyzer only applies to the assembly generated from that assembly definition, and to any other assembly that references it.
This means, for example, that a [package](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)A container that stores various types of features and assets for Unity, including Editor or Runtime tools and libraries, Asset collections, and project templates. Packages are self-contained units that the Unity Package Manager can share across Unity projects. Most of the time these are called _packages_ , but occasionally they are called **Unity Package Manager (UPM) packages**. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Package) can supply analyzers that only analyze code related to the package, which can help package users to use the package API correctly.
## Report analyzer diagnostics
To view information such as the total execution time of your analyzers and source generators or the relative execution times of each analyzer or source generator, go to **Preferences** > **Diagnostic Switches** and enable **EnableDomainReloadTimings**. When enabled, the information is displayed in the console window.
## Additional resources
  * [Special folders and script compilation order](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compile-order-folders.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ruleset-files.html)
Create rule set files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
Optimization
