* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html

# PropertyVisitor
class in Unity.Properties
/
Implemented in:[UnityEngine.PropertiesModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PropertiesModule.html)
Leave feedback
  

Implements interfaces:[ICollectionPropertyVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.ICollectionPropertyVisitor.html), [IDictionaryPropertyBagVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IDictionaryPropertyBagVisitor.html), [IDictionaryPropertyVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IDictionaryPropertyVisitor.html), [IListPropertyBagVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IListPropertyBagVisitor.html), [IListPropertyVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IListPropertyVisitor.html), [IPropertyBagVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyBagVisitor.html), [IPropertyVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyVisitor.html), [ISetPropertyVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.ISetPropertyVisitor.html)
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
Base class for implementing algorithms using properties. This is an abstract class. 
### Public Methods
Method | Description  
---|---  
[AddAdapter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.AddAdapter.html) |  Adds an adapter to the visitor.   
[RemoveAdapter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.RemoveAdapter.html) |  Removes an adapter from the visitor.   
### Protected Methods
Method | Description  
---|---  
[IsExcluded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.IsExcluded.html) |  Called before visiting each property to determine if the property should be visited.   
[VisitCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitCollection.html) |  Called when visiting any non-specialized collection property.   
[VisitDictionary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitDictionary.html) |  Called when visiting a specialized dictionary property.   
[VisitList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitList.html) |  Called when visiting a specialized list property.   
[VisitProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitProperty.html) |  Called when visiting any leaf property with no specialized handling.   
[VisitSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitSet.html) |  Called when visiting a specialized set property.   
* * *
