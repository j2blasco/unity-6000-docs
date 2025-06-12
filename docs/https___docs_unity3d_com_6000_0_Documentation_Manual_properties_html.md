* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Adding functionality to objects at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-download-handlers.html)
Creating DownloadHandlers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html)
Property bags
# Adding functionality to objects at runtime
You can use the Unity Properties API to visit .Net objects at runtime. The Properties API is in the `Unity.Properties` namespace and it uses a [visitor design pattern](https://en.wikipedia.org/wiki/Visitor_pattern) to visit .Net objects at runtime. The visitor pattern is a design pattern that allows you to add new operations to an existing object structure without modifying the structure itself. You can build various functionalities on top of the visitor pattern, such as serialization, data migration, deep data comparisons, and data binding.
Unity Properties allows you to use visitors on any given type. You can use the Properties API to do the following:
  * Create data types compatible with the Properties API
  * Develop new property visitors and adapters for domain-specific use cases

Topic | Description  
---|---  
[Property bags](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html) | Understand the concept and performance considerations about property bags.  
[Property visitors](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html) | Understand the concept and performance considerations about property visitors.  
[Property paths](https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html) | Understand the concept and performance considerations about property paths.  
[Use `PropertyVisitor` to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-PropertyVisitor.html) | Learn how to use the `PropertyVisitor` base class to create a property visitor from an example.  
[Use low-level APIs to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html) | Learn how to use the `IPropertyBagVisitor` and `IPropertyVisitor` interfaces to create a property visitor from an example.  
## Additional resources
  * [Serialization](https://docs.unity3d.com/Packages/com.unity.serialization@latest)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-download-handlers.html)
Creating DownloadHandlers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html)
Property bags
