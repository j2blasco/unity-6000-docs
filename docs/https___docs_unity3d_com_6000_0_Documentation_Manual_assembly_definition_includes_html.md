* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
  * Conditionally including assemblies


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html)
Referencing assemblies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html)
Assembly metadata and compilation details
# Conditionally including assemblies
You can use preprocessor symbols to control whether an assembly is compiled and included in builds of your application (including Play mode in the Editor). You can specify which symbols must be defined for an assembly to be used with the **Define Constraints** list in the Assembly Definition options:
  1. Select the Assembly Definition for the assembly to view its properties in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  2. In the **Define Constraints** section, click the **+** button to add a new symbol to the list of constraints.
![The Inspector window displays the Define Constraints section of the Assembly Definition assets properties.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/asmdef-7.png) The Inspector window displays the Define Constraints section of the Assembly Definition asset’s properties.
  3. Enter the symbol name.
You can negate the symbol by putting an exclamation point in front of the name. For example, the constraint, `!UNITY_WEBGL` would include the assembly when `UNITY_WEBGL` was NOT defined.
  4. Click **Apply**.


You can use the following symbols as constraints:
  * Symbols defined in the [Scripting Define Symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html) setting, which you can find in the **Player** section of your **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings). Note that the **Scripting Define Symbols** apply to the currently active platform in your project [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile). To define a symbol for multiple platforms, you must switch to each platform and modify the **Scripting Define Symbols** field individually.
  * Symbols defined by Unity. Refer to [Unity scripting symbol reference](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-symbol-reference.html).
  * Symbols defined using the [Version Defines](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-includes.html#define-symbols) section of the Assembly Definition asset.


Symbols defined in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) are not considered when determining if a constraint has been satisfied.
For more information, refer to [Define Constraints](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#define-constraints).
## Defining symbols based on Unity and project package versions
If you need to compile different code in an assembly according to whether a project uses specific versions of Unity or of a package, you can add entries to the **Version Defines** list. This list specifies rules for when a symbol should be defined. For version numbers, you can specify a logical expression that evaluates to a specific version or a range of versions.
To conditionally define a symbol:
  1. Select the Assembly Definition asset for the assembly to view its properties in the **Inspector**.
  2. In the **Version Defines** section, click the **+** button to add an entry to the list.
  3. Set the properties:
     * **Resource** : choose **Unity** or the package or module that must be installed in order for this symbol to be defined
     * **Define** : the symbol name
     * **Expression** : an expression that evaluates to a specific version or a range of versions. See [Version Define Expressions] for the rules.
The **Expression outcome** shows which versions the expression evaluates to. If the outcome displays, **Invalid** , then expression syntax is incorrect.
The following example defines the symbol `USE_TIMELINE_1_3` if the project uses Timeline 1.3 and `USE_NEW_APIS` if the project is opened in Unity 2021.2.0a7 or later:
![The Inspector window displays the Version Defines section of the Assembly Definition assets properties.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/asmdef-8.png) The Inspector window displays the Version Defines section of the Assembly Definition asset’s properties.
  4. Click **Apply**.


Symbols defined in the Assembly Definition are only in scope for the scripts in the assembly created for that definition.
Note that you can use the symbols defined using the **Version Defines** list as **Define Constraints**. Thus you could specify that an assembly should only be used when specific versions of a given package are also installed in the project.
### Version Define expressions
You can use expressions to specify an exact version or a range of versions. A **Version Define** expression uses mathematical range notation. 
A square bracket, “[]” designates that the range includes the endpoint:
> `[1.3,3.4.1]` evaluates to `1.3.0 <= x <= 3.4.1`
A parenthesis “()” designates that the range excludes the endpoint: 
> `(1.3.0,3.4)` evaluates to `1.3.0 < x < 3.4.0`
You can mix both range types in a single expression:
> `[1.1,3.4)` evaluates to `1.1.0 <= x < 3.4.0`
> `(0.2.4,5.6.2-preview.2]` evaluates to `0.2.4 < x <= 5.6.2.-preview.2`
You can use a single version designator in square brackets to designate an exact version:
> `[2.4.5]` evaluates to `x = 2.4.5`
As a shortcut, you can enter a single version without range brackets to indicate that the expression includes that version or later:
> `2.1.0-preview.7` evaluates to `x >= 2.1.0-preview.7`
**Note:** No spaces are allowed in an expression. No wildcard characters are supported.
### Unity version numbers
Current versions of Unity (and all versions that support Assembly Definitions) use a version designator with three parts: MAJOR.MINOR.REVISION, for example, `2017.4.25f1`, `2018.4.29f1`, and `2019.4.7f1`.
  * The MAJOR version is four digits representing the release year for Unity `2022.x.z` and earlier, or the major technical version from Unity 6 (6000.x.z) onwards.
  * The MINOR version is the target release quarter, such as 1, 2, 3, or 4.
  * The REVISION designator has three parts of its own, with the format: RRzNN, where: 
    * RR is a one or two digit revision number
    * z is a letter designating the release type: 
      * a = alpha release
      * b = beta release
      * f = a normal public release
      * c = China release version (equivalent to f)
      * p = patch release
      * x = experimental release
    * NN is one or two digit incremental number


Release type designators are compared as follows: 
> `a < b < f = c < p < x`
In other words, an alpha release is considered earlier than a beta, which is earlier than a normal (f) or China (c) release. A patch release is always later than a normal or China release with the same revision number and an experimental release is later than any other release type. Note that experimental releases do not use an incremental number at the end.
Unity version numbers are allowed to have a suffix after the REVISION component, such as `2019.3.0f11-Sunflower`. Any suffixes are ignored for the purpose of comparing versions.
As an example, the following expression includes any 2017 or 2018 version of Unity, but not any version in 2019 or later:
```
[2017,2019)

```

### Package and module version numbers
Package and module version designators have four parts, following the [Semantic Versioning](https://semver.org/) format: MAJOR.MINOR.PATCH-LABEL. The first three parts are always numbers, but the label is a string. Unity packages in preview use the string, `preview` or `preview.n`, where `n > 0`. For more information on package version numbers, refer to [Versioning](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html).
For example, the following expression includes all versions of a package with MAJOR.MINOR versions between 3.2 and 6.1 (inclusive):
```
[3.2,6.1]

```

## Additional resources
  * [Creating assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html)
  * [Referencing assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html)
  * [Assembly metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html)
  * [Assembly Definition properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
  * [Assembly Definition Reference properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-referencing.html)
Referencing assemblies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-metadata.html)
Assembly metadata and compilation details
