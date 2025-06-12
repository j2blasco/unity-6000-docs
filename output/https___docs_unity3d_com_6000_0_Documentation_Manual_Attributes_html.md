* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Attributes.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Unity attributes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/null-reference-exception.html)
Null references
[](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
Compilation and code reload 
# Unity attributes
[Attributes](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/) in C# are metadata markers that can be placed above a class, property, or method declaration to indicate special behaviour. 
There are many attributes defined in the .NET libraries and Unity also provides a number of custom, Unity-specific attributes. For example, you can add the `HideInInspector` attribute above a property declaration to prevent the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) from showing the property, even if it is public. Attributes are specified in square brackets above the declaration as follows:
```
[HideInInspector]
public float strength;

```

For the full list of `UnityEngine` attributes, refer to the list under **UnityEngine > Attributes** in the Scripting API reference, which begins with [AddComponentMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html).
For the full list of `UnityEditor` attributes, refer to the list under **UnityEditor > Attributes** in the Scripting API reference, which begins with [AssetPostprocessorStaticVariableIgnoreAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessorStaticVariableIgnoreAttribute.html).
**Note:** Do not use the .NET [ThreadStatic](http://msdn.microsoft.com/en-us/library/system.threadstaticattribute.aspx) attribute as this causes a crash if you add it to a Unity script.
## Additional resources
  * [Unity Learn: attributes](https://learn.unity.com/tutorial/attributes)
  * [Inspecting scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html)
  * [Script serialization rules](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/null-reference-exception.html)
Null references
[](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
Compilation and code reload 
