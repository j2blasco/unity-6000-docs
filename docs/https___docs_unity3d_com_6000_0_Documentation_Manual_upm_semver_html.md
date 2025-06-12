* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Create custom packages](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
  * Package versioning


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)
Package manifest file
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-asmdef.html)
Assembly definition and packages
# Package versioning
Packages must follow **Semantic Versioning** (SemVer). Semantic Versioning is a strategy that allows package authors to provide information on the type of changes included in a given version, compared to the previous version, in a format that automated tools can use.
Semantic Versioning expresses versions as **MAJOR.MINOR.PATCH** , where MAJOR introduces one or more breaking changes, MINOR introduces one or more backward-compatible API changes, and PATCH only introduces bug fixes with no API changes at all.
When you begin to develop a package, start the version number at `0.1.0`. The MAJOR version number `0` is reserved for packages in their initial development phase. During initial development, package APIs change often, frequently in a breaking manner, so keep the MAJOR version number at `0` until you consider your package stable enough and ready for use in production.
After a package is officially ready for use in production, increment the MAJOR version to `1` and adhere to the following guidelines for subsequent changes:
**Increment this value:** | **Under these conditions:** | **Example:**  
---|---|---  
**MAJOR** | There is at least one breaking change and neither version of the package can be substituted for the other. A breaking change includes:  
  
• Changing the API surface (the exposed part of the API) or features in a way that risks compilation or runtime errors.  
• Removing non-API features, including removing Assets or changing an Asset’s GUID.   
• Removing or renaming assemblies and Assets (because) the compiler might fail to locate them).  
  
**Note** : When incrementing the major version, always reset the **PATCH** and **MINOR** values to `0`. | Versions 1.2.3 and 2.0.0 are not compatible and cannot be used interchangeably without risk.  
**MINOR**   
(same **MAJOR** value) | The highest **MINOR** introduces functionality in a backward-compatible way. A backward-compatible (or non-breaking) API change includes:   
  
• Changing the API surface or features without risking compilation or runtime errors.   
• Adding non-API features.   
• Adding assemblies and Assets (because new items don’t have pre-existing references).  
  
**Note** : When incrementing the minor version, always reset the **PATCH** version to `0`. | You can use Version 1.3.0 to fulfill a dependency on 1.2.0, because 1.3.0 is backward-compatible.   
  
You can’t use 1.2.0 to fulfill a dependency on 1.3.0.  
**PATCH**   
(same **MAJOR.MINOR** values) | The highest **PATCH** introduces bug fixes without changing the API at all, in a backward-compatible way. The API doesn’t change if:   
  
• The API surface is identical and the features remain unchanged.   
• The changes don’t alter the public API. | Versions 1.3.0 and 1.3.1 should be interchangeable because they have the same API, even though 1.3.1 contains a bug fix not present in 1.3.0.  
Following these versioning practices allows the Package Manager to automatically solve conflicts (when possible), or upgrade packages to newer, backward-compatible versions.
The following sections describe scenarios to help you determine how these rules affect various package elements:
  * [General assets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#general) (such as Audio, Textures, and Models).
  * [Assembly definitions (_.asmdef_ files) and precompiled assemblies (managed _.dll_ files)](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asmdefs)
  * [Package manifest files](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#manifests) (_package.json_)
  * [Obsolete APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#obsolete)


In addition to these scenarios, there is another factor that can affect some changes that would normally require only a MINOR or PATCH version increase: whether the [Auto Referenced](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#autoref) property is enabled or disabled.
## Automatic referencing
One of the properties you can set for your [assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html) is the **Auto Referenced** property, which controls whether Unity automatically references the file during compilation. When this property is enabled, some changes that would normally require only a MINOR or PATCH version increase now become breaking changes.
When you **disable** auto-referencing, if you make any change that results in a new assembly being available, you are introducing a backward-compatible change to the API. Backward-compatible API changes, such as [adding platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-addPlatform), [disabling Unity Test References](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-testRefs), [adding a new _.asmdef_](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-newAsmdefs), or [removing Define Constraints](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-defCns), only require a **MINOR** increase.
However, when you **enable** auto-referencing, that newly-added assembly is implicitly added to the references of various other assemblies. Since those cases can lead to compilation errors in those other assemblies, so it requires a **MAJOR** increase.
Another common case occurs when you add or change versions for a package dependency. Most of the time, [changing the package dependency](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#mani-dep) only requires a **PATCH** increase. However, the new package version might contain an assembly with the **Auto Referenced** property **enabled** , which becomes a breaking change, and therefore requires a **MAJOR** increase.
To avoid problems like these, always try to avoid putting a third-party DLL file into an unrelated package (such as including _Newtonsoft.Json.dll_ in a SaveGameManager package).
## Assets
A project can reference any asset that is visible to the Asset Database. The Asset Database tracks these assets uniquely using the GUIDs defined in their _.meta_ files.
When you introduce one of these changes to the public API, this requires a new **MAJOR** release, because they are **breaking changes** :
**Scenario:** | **Why these are breaking changes:**  
---|---  
Removing an Asset that is visible to the Asset Database | If you remove an Asset, this might break references in user Projects or other packages.  
Changing the GUID of an Asset | If you change an Asset GUID, the Asset Database understands this as removing the original Asset and then adding a new (identical) Asset. This results in a broken reference, because the original GUID no longer points to the Asset, so the Asset Database cannot resolve the reference.  
## Assemblies
[Assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html) (_.asmdef_) define a group of **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) which the Unity Editor’s compilation pipeline turns into separate managed assemblies (_.dll_). These _.asmdef_ assets include properties that drive the resulting assembly’s properties. This includes:
  * Importer settings, such as included and excluded platforms
  * Compilation-related properties, such as output assembly names and references fed to the compiler to build the assembly.


Most properties have an impact on the consumers of the assembly, so changing any of these properties constitutes a change to the package’s public API. Other properties have no impact on the consumers of the assembly, so changing any of these is not considered changing the package API.
**Warning** : The **Auto Referenced** property is a special case, because many of the changes that would normally [not change the API at all](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-none) or would [change the API in a backward-compatible way](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-bcomp) could cause compilation errors, depending on whether or not it is enabled. For more information, see [Automatic referencing](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#autoref).
Unity can either pre-compile assemblies, or compile them from scripts and an assembly definition. Therefore, anything that applies to assembly definitions generally also applies to precompiled assemblies.
This section details changes in assembly definitions and precompiled assemblies, and the impact on the package version:
  * [Breaking changes](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-break) (allowed in new MAJOR releases only)
  * [Backwards-compatible API changes](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-bcomp) (allowed in new MAJOR or MINOR releases)
  * [Backwards-compatible changes](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#asm-none) that do not alter the API (allowed in new MAJOR, MINOR or PATCH releases)


### MAJOR only: breaking changes
When you introduce a **breaking change** to the public API, this requires a new **MAJOR** release, because it might cause compilation and runtime errors. These scenarios all remove or hide an assembly from any other assemblies that reference it. When an assembly using a type defined in a referenced assembly is compiled, if the compiler cannot find that other assembly, that results in compilation errors. For more information about working with assemblies and assembly definitions, see [Assembly Definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html).
Note that the following applies to both run-time and Editor assemblies that packages consume and use. It doesn’t apply to test assemblies, because packages do not normally consume them, so they are not part of a package’s API.
**Scenario:** | **Why the compiler can’t find the referenced assembly:**  
---|---  
Removing an assembly definition or a precompiled assembly | Removing an assembly definition file prevents the compilation pipeline from generating the corresponding assembly.   
  
**Note** : As of 2019.1, missing references are allowed to support the “optional reference” use case, but renaming an assembly that Unity needs to compile an assembly definition causes compilation errors. Likewise, if compiled code needs a type from an assembly, renaming that assembly can result in run-time errors such as `TypeLoadException`.  
Changing an assembly name (either in the _.asmdef_ file or renaming the _.dll_ file) | Changing the assembly name is equivalent to removing the assembly and then adding a new one with a different name. This means Unity considers the original assembly to be missing, even though the API still contains the same assembly code under another name.  
Adding a [define constraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.DefineConstraints.html) to an _.asmdef_ | If you add a define constraint, Unity skips compiling the assembly whenever the define constraint is not met. This creates cases where the assembly is missing, even though it was previously available.  
[Removing platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html#create-platform-specific) | If you remove support for a specific platform, Unity no longer imports the assembly on that platform, which is equivalent to removing the assembly.   
  
You can remove a platform by enabling one of these properties:  
• **includePlatforms** , which breaks compatibility with all unlisted platforms  
• **excludePlatforms** , which adds entries to it  
Moving public APIs from one assembly to another | When you move publicly accessible code from Assembly A to Assembly B, any assembly that references A but not B fails to compile.  
  
For assembly definitions, if you move scripts around, you might be moving public APIs to a different assembly.  
Changing the **Auto Referenced** property | When you _disable_ the **Auto Referenced** property, you can no longer use the public API of this assembly without an explicit reference:  
  
• For precompiled assemblies, disabling this property prevents Unity from implicitly adding the precompiled assembly as a reference to assembly definitions and project-compiled assemblies.  
• For assembly definitions, disabling this property prevents Unity from implicitly adding the resulting assembly as a reference to project-compiled assemblies.  
  
When you _enable_ the **Auto Referenced** property, it potentially introduces conflicts with other changes to the API, properties, or dependencies. For more information, see the [Automatic referencing](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#autoref) section.  
Enabling the **Unity References → Test Assemblies** property in assembly definitions | Enabling the **Unity References → Test Assemblies** property marks this assembly as a test assembly, and Unity doesn’t normally include it in builds (or compile it in some cases). When this happens, any assembly referencing the missing assembly fails to locate it, unless it is also a test assembly.  
### MAJOR, MINOR: non-breaking API changes
The following changes are **backward-compatible** , or non-breaking, API changes. These scenarios all add an assembly, unlike breaking changes which remove an assembly. Since adding an assembly increases the API surface (the exposed part of the API), it is considered an API change. However, there are no existing references, so adding a new assembly won’t affect other assemblies created with an earlier API.
Backward-compatible changes require at least a new **MINOR** release. If you are including other updates that are breaking changes, then these can also be part of the new **MAJOR** release.
**Warning** : These changes are only backward-compatible if the **Auto Referenced** property is disabled. When the **Auto Referenced** property is enabled, the changes listed in this table might result in breaking changes. For more information, see the [Automatic referencing](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#autoref) section.
**Scenario** | **Why these changes don’t break compilation**  
---|---  
Removing a [define constraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.DefineConstraints.html) to an .asmdef | Removing a define constraint means that the compilation and scripting pipelines no longer skip this assembly. Because Unity always builds that assembly, the compiler can always resolve references to it, regardless of whether or not that define constraint is met.  
Adding platforms | Adding platforms has no effect on existing platform support, so it is backwards-compatible. This is an API change because it increases the API surface.  
  
You can add platforms by modifying these properties:  
• Add entries to the **includePlatforms** property.  
• Remove the **includePlatforms** property completely. This is equivalent to adding all platforms that were not already in the **includePlatforms** property.  
• Remove entries from the **excludePlatforms** property.  
Creating an assembly definition with new scripts (not previously under a different _.asmdef_ file) | Adding a new assembly increases the API surface (the exposed part of the API) without altering any existing implementations.  
Disabling the **Unity References → Test Assemblies** property in assembly definition files | Disabling the **Unity References → Test Assemblies** property marks this assembly as a regular assembly, so Unity no longer treats it differently from any assembly definition. This is an API change because it increases the API surface.  
### MAJOR, MINOR, PATCH: no API changes
The following changes do not affect the public API and are allowed in **PATCH** releases. The changes in these scenarios don’t alter the public API because they don’t affect the API surface (the exposed part of the API) and don’t change anything for other consumers.
Changes that don’t alter the public API require at least a new **PATCH** release. If you are including other updates that introduce either breaking or non-breaking changes, then you can also include them in **MAJOR** or **MINOR** releases.
**Scenario** | **Why these changes don’t impact other consumers**  
---|---  
Changing the list of referenced assemblies and assembly definitions in _.asmdef_ files | An assembly that references another assembly does not automatically reference that other assembly’s own references, but has to explicitly list them. Therefore, changing references in an assembly definition or assembly does not impact other consumers.  
Changing the **Allow unsafe code** property in assembly definitions | This property controls whether the compiler is allowed to compile code that has the **unsafe** modifier. Changing that flag on its own does not alter the public API.  
Changing the **Override References** property in assembly definitions | This property controls how Unity invokes the compiler for this assembly, and has no effect on consumers of the resulting assembly. Changing that flag on its own does not alter the public API.  
## Package manifest files
The [package manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packagemanifest) file (`package.json`) specifies the name, version, package dependencies, and other metadata about the package itself.
This section details changes in package manifest files, and the impact on the package version:
  * [Name changes](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#mani-name) (not allowed)
  * [Changes in dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#mani-dep) (the context determines the minimum version change)
  * [Other changes](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#mani-other) (allowed in new MAJOR, MINOR or PATCH releases)


### Name changes (not allowed)
Changing the **name** property is the equivalent of removing one package and adding a new package with a different name, and it is not supported. You cannot rename a package by trying to release an update: you have to release it as an entirely new package. Name changes aren’t allowed because existing projects and packages cannot interpret the names as synonyms.
### Dependency changes
Changing a dependency in a project does not in itself require a different MAJOR or MINOR version, unless it is part of an API change or if the [Auto Referenced](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#autoref) property is enabled.
This section provides examples of dependency changes and the contexts in which they apply (assuming that the [Auto Referenced](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html#autoref) property is disabled and there is no API change other than what each case describes):
**Dependency change** | **Context** | **Minimum version change**  
---|---|---  
Adding a new dependency | • Uses the new package without changing functional behavior, and doesn’t change the API surface. | PATCH  
| • Uses the new package to introduce new behavior, without modifying the API surface.  
• Creates new APIs that expose types defined in the new package. | MINOR  
| • Uses the new package to change existing behavior in a way that is not backwards-compatible, without modifying the API surface.  
• Modifies existing APIs in a way that is not backwards-compatible to expose types defined in the new package. | MAJOR  
Removing a dependency | • Removes the package without changing functional behavior, and doesn’t change the API surface. | PATCH  
| • Removing the package results in a change in existing behavior in a way that is not backwards-compatible, without changing the API surface.  
• Removes APIs that expose types defined in that dependency. | MAJOR  
Changing a dependency | • Uses the modified package without changing functional behavior, and doesn’t change the API surface. | PATCH  
| • Uses the modified package to introduce new behavior, without modifying the API surface.  
• Creates new APIs that expose types defined in the modified package. | MINOR  
| • Uses the modified package to change existing behavior in a way that is not backwards-compatible, without modifying the API surface.  
• Changes existing APIs in a way that is not backwards-compatible to expose types defined in the modified package.  
• Exposes some types in APIs that are changed in a non-backward-compatible way in the modified package.  
• Exposes some types in APIs that are no longer defined in the modified package. | MAJOR  
### MAJOR, MINOR or PATCH: other changes
You can change package manifest attributes that have no special effect on the Package Manager, the build pipeline, the scripting pipeline or the Asset Database in any release version. This includes changing the **description** , the **category** , the **keywords** , or the **displayName**.
If you change these fields, that might indicate that your changes involve more than just bug fixes. Always consider whether other changes in the new version actually mandate a new MINOR or MAJOR release rather than a PATCH release.
**Note** : Changes to the **unity** or **unityRelease** properties in a package’s manifest always require either a MINOR or MAJOR release. Although the properties do not affect the package API itself, increasing the Unity version excludes a package version from working on previous Unity editors and might break a dependent project or package. Decreasing the Unity version makes the package available to older Unity editors.
## Deprecated and obsolete APIs
When you want to remove some functionality from your API, first release at least one MINOR version containing the deprecation. This warns users about the impending removal, so they can transition to the new API smoothly. Then you can remove the functionality in a new MAJOR release.
If another developer marks a package obsolete with a warning and you enabled **Warnings as Errors** in your project, the obsolete package might technically break your project, even though it is not a true break because the code still works as it did previously.
In this case, you can choose how you want to fix the warning-as-error (in descending order of typical desirability):
  * Change your code so you no longer use the API.
  * Wrap your code that uses the API in `#pragma warning` directives to silence the warning.
  * Disable warnings **CS0612 (Obsolete)** and **CS0618 (Obsolete with a message)**.
  * Disable **Warnings as Errors** in your project.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)
Package manifest file
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-asmdef.html)
Assembly definition and packages
