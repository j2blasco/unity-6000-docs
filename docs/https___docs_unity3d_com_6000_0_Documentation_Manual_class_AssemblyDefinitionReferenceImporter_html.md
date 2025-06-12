* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
  * Assembly Definition Reference properties reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
Assembly Definition properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)
Assembly Definition File Format reference
# Assembly Definition Reference properties reference
An Assembly Definition Reference is an asset that defines a reference to an Assembly Definition. Create an Assembly Definition Reference asset in a folder to include the **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) in that folder in the referenced Assembly Definition (rather than creating a new assembly). Scripts in child folders are also included, unless they have their own Assembly Definition or Assembly Definition Reference asset.
![An Assembly Definition Reference asset in the Inspector.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/asmdef-17.png) An Assembly Definition Reference asset in the Inspector. Property | Description  
---|---  
Use GUID | This setting controls how Unity serializes the reference to the Assembly Definition asset. When you enable this property, Unity saves the reference as the asset’s GUID, instead of the Assembly Definition name. It’s good practice to use the GUID instead of the name, because it means you can make changes to the name of an Assembly Definition asset without having to update other Assembly Definitions and References that reference it.  
Assembly Definition | The referenced Assembly Definition asset.  
See [Creating an Assembly Definition Reference asset](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
AssemblyDefinitionReferenceImporter
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
Assembly Definition properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)
Assembly Definition File Format reference
