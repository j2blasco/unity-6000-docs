* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
  * Serialization rules


[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
Script serialization
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html)
Custom serialization
# Serialization rules
Serializers in Unity are specifically designed to operate efficiently at runtime. Because of this, serialization in Unity behaves differently to serialization in other programming environments. Serializers in Unity work directly on the **fields** of your C# classes rather than their properties, so Unity only serializes your fields if they meet certain conditions. The following section outlines how to use field serialization in Unity.
To use field serialization you must ensure that the field:
  * Is `public`, or has a [SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html) attribute 
    * **Note** : In some cases `private` fields are serialized, refer to [Hot reloading](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html#hot-reload)
  * Is not `static`
  * Is not `const`
  * Is not `readonly`
  * Has a field type that can be serialized: 
    * Primitive data types (int, float, double, bool, string, etc.)
    * Enum types (32 bits or smaller)
    * Fixed-size buffers
    * Unity built-in types, for example, Vector2, Vector3, Rect, Matrix4x4, Color, AnimationCurve
    * Custom structs with the Serializable attribute
    * References to objects that derive from [UnityEngine.Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
    * Custom classes with the Serializable attribute. (Refer to [Serialization of custom classes](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html#CustomClasses)).
    * An array of a field type mentioned above
    * A `List<T>` of a field type mentioned above


**Note** : Unity doesn’t support serialization of multilevel types (multidimensional arrays, jagged arrays, dictionaries, and nested container types). If you want to serialize these, you have two options:
  * Wrap the nested type in a class or struct
  * Use serialization callbacks, by implementing [ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html), to perform [custom serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html).


##  Serialization of custom classes
For Unity to serialize a custom class, you must ensure the class:
  * Has the [Serializable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serializable.html) attribute
  * Is not static.


When you assign an instance of a `UnityEngine.Object`-derived class to a field and Unity saves that field, Unity serializes the field as a reference to that instance. Unity serializes the instance itself independently, so it isn’t duplicated when multiple fields are assigned to the instance. But for custom classes which don’t derive from `UnityEngine.Object`, Unity includes the state of the instance directly in the serialized data of the MonoBehaviour or ScriptableObject that references them. There are two ways that this can happen: **inline** and by **`[SerializeReference]`**.
  * **Inline serialization** : By default, Unity serializes custom classes inline by value when you don’t specify `[SerializeReference]` on the field that references the class. This means that if you store a reference to an instance of a custom class in several different fields, they become separate objects when serialized. Then, when Unity deserializes the fields, they contain different distinct objects with identical data.
  * **`[SerializeReference]`serialization** : If you do specify `[SerializeReference]`, Unity establishes the object as a managed reference. The host object still stores the objects directly in its serialized data, but in a dedicated registry section.


`[SerializeReference]` adds some overhead but supports the following cases:
  * Fields can be null. Inline serialization can’t represent null, instead, it replaces null with an inline object that has unassigned fields.
  * Multiple references to the same object. If you store a reference to an instance of a custom class in several different fields without using `[SerializeReference]`, then they become separate objects when serialized.
  * Graphs and cyclical data (for example, an object that has a reference back to itself). Inline class serialization doesn’t support null or shared references, so any cycle in data can lead to unexpected results, such as strange **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) behavior, console errors or infinite loops.
  * Polymorphism. If you create a class that derives from a parent class and assign it to a field that uses the parent class as its type, without `[SerializeReference]` Unity only serializes the fields that belong to the parent class. When Unity deserializes the class instance, it instantiates the parent class instead of the derived class.
  * When a data structure requires a stable identifier to point to a specific object without hard-coding the object’s array position or searching the entire array. Refer to [Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html).


**Note** : Inline serialization is more efficient, and you should use it unless you specifically need one of the features that `[SerializeReference]` supports. For full details on how to use `[SerializeReference]`, refer to the [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) documentation.
## Serialization of properties
Unity doesn’t normally serialize properties except in the following situations:
  * If a property has an explicit backing field, Unity serializes it according to regular serialization rules. For example:

```
public int MyInt
{
get => m_backing;
private set => m_backing = value;
}
[SerializeField] private int m_backing;

```

  * Unity serializes properties with auto-generated fields during hot reloading only.

```
public int MyInt { get; set; }

```

If you don’t want Unity to serialize a property with auto-generated fields, use the `[field: NonSerialized]` attribute.
## Additional resources
  * [Custom serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html)
  * [How Unity uses serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html)
  * [JSONSerialization](https://docs.unity3d.com/6000.0/Documentation/Manual/json-serialization.html)
  * [Serialization best practices](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-best-practices.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
Script serialization
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html)
Custom serialization
