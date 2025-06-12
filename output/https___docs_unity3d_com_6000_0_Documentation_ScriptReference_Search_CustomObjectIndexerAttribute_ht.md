* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute.html

# CustomObjectIndexerAttribute
class in UnityEditor.Search
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Allows a user to register a custom Indexing function for a specific type.
When you have special properties you would like to index for an asset or a Unity Object, Unity suggests Writing a custom indexer routine . The newly indexed words or properties will allow the user to search for them using the [Search Query Language](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html). The registered function must be of type: `static void MyCustomIndexer(CustomObjectIndexerTarget context, ObjectIndexer indexer);`  
  
See [ObjectIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) for the various methods you can invoke on `indexer`.  
  
The [CustomObjectIndexerTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) `context` argument can be used to access additional information about what is about to be indexed. 
```
[CustomObjectIndexer(typeof(Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)))]
internal static void MaterialShaderReferences(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) context, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
   var material = context.target as Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html);
   if (material == null)
       return;  
  
   if (material.shader)
   {
       var fullShaderName = material.shader.name.ToLowerInvariant();
       var shortShaderName = System.IO.Path.GetFileNameWithoutExtension(fullShaderName);
       indexer.AddProperty("ref", shortShaderName, context.documentIndex);
       indexer.AddProperty("ref", fullShaderName, context.documentIndex);
   }
}
```

### Properties
Property | Description  
---|---  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute-type.html) | Each time an object of a specific type is indexed, the registered function is called.  
[version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute-version.html) | Version of the custom indexer. Increment this number to have the indexer re-index the indexes.  
### Constructors
Constructor | Description  
---|---  
[CustomObjectIndexerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute-ctor.html) | Register a new Indexing function bound to the specific type.  
* * *
