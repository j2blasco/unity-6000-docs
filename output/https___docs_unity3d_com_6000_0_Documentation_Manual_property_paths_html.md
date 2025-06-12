* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Adding functionality to objects at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html)
  * Property paths


[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
Property visitors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-propertyvisitor.html)
Use PropertyVisitor to create a property visitor
# Property paths
Property paths are strings that describe the location of a property within a container object.
## Concept
You can use property paths to get or set the data of an object at a specific path or accept a visitor on a sub-property of an object.
Property paths are constructed from strings and resolve a specific property instance from a root object. For example, the path `foo.bar.baz[12]` resolves the 13th element of the `baz` list container within the `bar` container, which is nested inside the `foo` container.
To create and manipulate property paths, use the [`Unity.Properties.PropertyPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) class.
You can use property paths to do the following:
  * Get or set the data of an object at a specific path
  * Accept a visitor on a sub-property of an object


## Performance considerations
[`Unity.Properties.PropertyPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) is an **immutable** You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Immutable) struct type. When you construct a property path from a string, allocations occur for sub-string extraction.
The following table lists the allocation behaviors when a property path is constructed from a string:
String | Length | Allocations | Allocations reason  
---|---|---|---  
`"Path"` | 1 | 0 | Use the string as-is.  
`"Path.To"` | 2 | 2 | Split the string into two parts.  
`"Path.To[2]"` | 3 | 3 | Split the string into two parts and extract the index.  
`"Path.To[2].My"` | 4 | 4 |   
`"Path.To[2].My.Value"` | 5 | 6 | Allocate an array for the additional parts.  
The following table lists the allocation behaviors when a property path is constructed from parts:
String | Length | Allocations | Allocations reason  
---|---|---|---  
`PropertyPath.FromName("Path")` | 1 | 0 |   
`PropertyPath.AppendName(previous, "To")` | 2 | 0 |   
`PropertyPath.AppendIndex(previous, 2)` | 3 | 0 |   
`PropertyPath.AppendName(previous, "My")` | 4 | 0 |   
`PropertyPath.AppendName(previous, "Value")` | 5 | 1 | Allocate an array for the additional parts.  
To optimize performance and avoid allocating memory:
  * Initialize and cache property paths during initialization routines.
  * Combine or append property path parts instead of constructing it from a string, up to four parts.


## Additional resources
  * [Property bags](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html)
  * [Property visitors](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
  * [Use `PropertyVisitor` to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-PropertyVisitor.html)
  * [Use low-level APIs to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
Property visitors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-propertyvisitor.html)
Use PropertyVisitor to create a property visitor
