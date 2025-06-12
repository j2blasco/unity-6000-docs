* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-marking-rules.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Managed code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html)
  * Unity linker marking rules reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-xml-formatting.html)
Link XML formatting reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
Scripting backends
# Unity linker marking rules reference
When the Unity linker performs its static analysis, it follows sets of rules to determine which parts of the CIL bytecode to mark as necessary for the build:
  * [Root marking rules](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-marking-rules.html#root-marking-rules) determine how the Unity linker identifies and preserves top-level assemblies in the build.
  * [Dependency marking rules](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-marking-rules.html#dependency-marking-rules) determine how the Unity linker identifies and preserves any code that the root assemblies depend on.


The [configured managed stripping level](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-configure.html) changes the set of rules that the Unity linker uses. The following sections describe the marking rules at each managed stripping level.
## Root marking rules
The following table describes how the Unity linker identifies the top-level types in an assembly for different assembly types and managed stripping levels:
**Assembly type** | **Root marking rules at managed stripping levels**  
---|---  
**.NET Class & Platform SDK and UnityEngine Assemblies** |  **Minimal** and **Low** : 
  * Precautionary preservations 

**Minimal** , **Low** , **Medium** and **High** : 
  * Preservations defined in any `link.xml` file 

  
**Assemblies with types referenced in a scene** |  **Minimal** and **Low** : 
  * All types and members in the assembly 

**Medium** and **High** : 
  * All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute. 
  * Preservations defined in any `link.xml` file 
  * All types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies. 

  
**All other** |  **Minimal** : 
  * All types and members in the assembly 

**Low** and **Medium** : 
  * All public types and public members of those types

**Medium** and **High** : 
  * All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute. 
  * Preservations defined in any `link.xml` file 
  * All types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies. 

  
**Test** |  **Minimal** , **Low** , **Medium** and **High** : 
  * Any methods with the `[UnityTest]` attribute and any methods annotated with an Attribute defined in the NUnit.Framework.

  
## Dependency marking rules
After the Unity linker identifies the roots in an assembly, it needs to identify any code that those roots depend on. The following table describes how the Unity linker identifies dependencies of root types in an assembly at different managed stripping levels:
**Rule target** | **Dependency marking rules at managed stripping levels**  
---|---  
**MonoBehaviour** |  **Minimal** , **Low** , **Medium** and **High** : 
  * The Unity linker marks all members of a MonoBehavior type when it marks the type 

  
**ScriptableObject** |  **Minimal** , **Low** , **Medium** and **High** : 
  * The Unity linker marks all members of a ScriptableObject type when it marks the type 

  
**Attributes** |  **Minimal** and **Low** : 
  * When the Unity linker marks an assembly, type or other code structure, it also marks all attributes of those structures. 

**Medium** and **High** : 
  * When the Unity linker marks an assembly, type or other code structure, it only marks attributes of those structures if the attribute type is also marked. 

  
**Debugging Attributes** |  **Minimal** and **Low** : 
  * When script debugging is enabled, the Unity linker marks all members that have the `[DebuggerDisplay]` attribute, even when there isn’t a code path that uses those members. 

**Medium** and **High** : 
  * The Unity linker always removes debugging attributes such as `DebuggerDisplayAttribute` and `DebuggerTypeProxyAttribute`. 

  
**.NET Facade Class Library** |  **Minimal** , **Low** , **Medium** and **High** : 
  * Removes facade assemblies since they aren’t necessary at runtime.

  
## Additional resources
  * [Managed code stripping and the Unity linker](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-linker.html)
  * [Preserving code using annotations](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-preserving.html)
  * [Link XML formatting reference](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-xml-formatting.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping-xml-formatting.html)
Link XML formatting reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
Scripting backends
