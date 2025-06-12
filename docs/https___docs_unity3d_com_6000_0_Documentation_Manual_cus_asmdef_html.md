* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/cus-asmdef.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Create custom packages](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
  * Assembly definition and packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html)
Package versioning
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-legal.html)
Custom package legal requirements
# Assembly definition and packages
You must associate **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) inside a package to an assembly definition file (`.asmdef`). Assembly definition files are the Unity equivalent to a C# project in the .NET ecosystem. You must set explicit references in the assembly definition file to other assemblies (whether in the same package or in external packages). Refer to [Assembly Definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html) for more details.
Use these conventions for naming and storing your assembly definition files to ensure that the compiled assembly filenames follow the [.NET Framework Design Guidelines](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/):
  * Store Editor-specific code under a root editor assembly definition file:
`Editor/<company-name>.<package-name>.Editor.asmdef`
  * Store runtime-specific code under a root runtime assembly definition file:
`Runtime/<company-name>.<package-name>.asmdef`
  * Configure related test assemblies for your editor and runtime scripts:
`Tests/Editor/<company-name>.<package-name>.Editor.Tests.asmdef`
`Tests/Runtime/<company-name>.<package-name>.Tests.asmdef`


To get a more general view of a recommended package folder layout, refer to [Package layout](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-layout.html).
## Example file
In this example, the assembly definition file uses references to its own assemblies, and an assembly that’s part of a package dependency ([HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest)):
```
{
    "name": "MyCompany.MyPackageName",
    "references": [
        "MyCompany.MyPackageName.Tools",
        "MyCompany.MyPackageName.Planes",
        "Unity.RenderPipelines.HighDefinition.Runtime"
    ],
    "includePlatforms": [],
    "excludePlatforms": [],
    "allowUnsafeCode": false,
    "overrideReferences": false,
    "precompiledReferences": [],
    "autoReferenced": true,
    "defineConstraints": [],
    "versionDefines": [
        {
            "name": "com.unity.render-pipelines.high-definition",
            "expression": "7.1.0",
            "define": "HDRP_7_1_0_OR_NEWER"
        },
        {
            "name": "com.unity.modules.particlesystem",
            "expression": "1.0.0",
            "define": "USING_PARTICLE_SYSTEM"
        }
    ],
    "noEngineReferences": false
}

```

For details about the structure of an assembly definition file, refer to [Assembly Definition File Format](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html).
## Additional resources
  * [Assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html)
Package versioning
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-legal.html)
Custom package legal requirements
