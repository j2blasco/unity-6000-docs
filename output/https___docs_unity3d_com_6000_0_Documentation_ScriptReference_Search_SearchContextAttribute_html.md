* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute.html

# SearchContextAttribute
class in UnityEngine.Search
/
Inherits from:[PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
This attribute can be attached to a component object field in order to have the ObjectField use the advanced Object Picker.
```
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:mesh is:nested mesh", "asset")]
public UnityEngine.Object assetMesh;
```

### Properties
Property | Description  
---|---  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-flags.html) | Search view flags used to open the Object Picker in various states.  
[instantiableProviders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-instantiableProviders.html) | Search provider concrete types that will be instantiated and assigned to the Object Picker search context.  
[providerIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-providerIds.html) | A list of Search Provider IDs that will be used to create the search context.  
[query](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-query.html) | Initial search query used to open the Object Picker window.  
### Constructors
Constructor | Description  
---|---  
[SearchContextAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-ctor.html) | Search context constructor used to add some search context to an object field.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
