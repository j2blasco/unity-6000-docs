* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Adding functionality to objects at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html)
  * Property bags


[](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html)
Adding functionality to objects at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
Property visitors
# Property bags
Property bags are collections of properties for a given .Net object type that you can use to access and set data for an instance of an object of that type.
## Concept
A property bag for a given type is a companion object that enables efficient data traversal algorithms based on instances of that type. By default, Unity uses reflection to generate the property bag for a type. This reflective approach offers convenience and occurs lazily only once per type when a property bag hasn’t been registered yet.
To enhance performance, you can opt-in to code generation by tagging the type with [`[Unity.Properties.GeneratePropertyBag]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.GeneratePropertyBagAttribute.html). Additionally, to activate code generation, you must tag the assembly with [`[assembly: Unity.Properties.GeneratePropertyBagsForAssembly]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.GeneratePropertyBagsForAssemblyAttribute.html). Code-generated property bags are automatically registered when the domain is loaded.
In both the reflection and code-generation scenarios, the property bag generates properties for the following:
  * Public fields
  * Private or internal fields tagged with [`[SerializeField]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html), [`[SerializeReference]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html), or [`[CreateProperty]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.CreatePropertyAttribute.html)
  * Public, private, or internal properties tagged with [`[Unity.Properties.CreateProperty]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.CreatePropertyAttribute.html)


The property bag doesn’t generate a property for public, private, or internal fields tagged with [`[DontCreateProperty]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.DontCreatePropertyAttribute.html).
A generated property is read-only if the field is read-only or the property only has a getter.
You can also use [`[Unity.Properties.CreateProperty(ReadOnly = true)]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.DontCreatePropertyAttribute.html) to make a generated property read-only.
Creating properties in the property bag using serialization attributes for convenience is not always the preferred approach. Unity’s serialization system can only operate on fields and auto-properties, which makes it challenging to achieve validation or propagate changes effectively.
The following example combines the Unity serialization system with the Unity Properties system:
```
using UnityEngine;
using Unity.Properties;

public class MyBehaviour : MonoBehaviour
{
    // Serializations go through the field, but we don't want to create a property for it.
    [SerializeField, DontCreateProperty] 
    private int m_Value;
    
    // For the property bag, use the property instead of the field. This ensures that
    // the value stays within the appropriate bounds.
    [CreateProperty] 
    public int value
    {
        get => m_Value;
        set => m_Value = value;
    }
    
    // This is a similar example, but for an auto-property.
    [field: SerializeField, DontCreateProperty]
    [CreateProperty]
    public float floatValue { get; set; }
}

```

Unlike the Unity serialization system, the properties within a property bag don’t qualify as value types with [`[SerializeField]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html). Instead, struct types are recognized as value types, whereas class types are recognized as references.
In Unity serialization, although polymorphism is supported, you must use the [`[SerializeReference]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) attribute to explicitly opt in. Otherwise, instances are serialized as value types. It’s worth noting that [`UnityEngine.Object`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) types are an exception to this rule, as they’re automatically serialized as reference types. 
## Performance considerations
Unity Properties uses .Net reflection to create property bags and properties that are strongly typed, which can introduce performance overhead the first time you request a property bag for a given container type.
When you create properties for field members through reflection, these properties may allocate garbage in **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) builds. This allocation occurs due to the direct use of [`System.Reflection.FieldInfo`](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.fieldinfo), which leads to unavoidable boxing. 
To avoid reflection, you can code-generate property bags during compilation. However, be aware that this optimization may lead to longer compilation times. To enable code generation for an assembly, tag the assembly with [`[Unity.Properties.GeneratePropertyBagsForAssemblyAttribute]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.GeneratePropertyBagsForAssemblyAttribute.html) and tag individual types with [`[Unity.Properties.GeneratePropertyBagAttribute]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.GeneratePropertyBagAttribute.html). To enable the property bag to access internal, and private fields and properties, make the type `partial`.
## Additional resources
  * [Property visitors](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
  * [Property paths](https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html)
  * [Use `PropertyVisitor` to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-PropertyVisitor.html)
  * [Use low-level APIs to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html)
Adding functionality to objects at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
Property visitors
