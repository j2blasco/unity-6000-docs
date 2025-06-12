* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext.html

# SceneSearchContext
class in UnityEditor.SearchService
Leave feedback
  

Implements interfaces:[ISearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html)
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
A search context implementation for Scene search engines. All methods that are called on a Scene search engine, and expect a [ISearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html), receive an object of this type.
### Properties
Property | Description  
---|---  
[engineScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext-engineScope.html) | An enum that identifies the scope of the current search. This property is automatically set to SearchService.Scene.EngineScope.  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext-guid.html) | A unique identifier for this search context.  
[requiredTypeNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext-requiredTypeNames.html) | An IEnumerable of strings that contains the type name constraints for this search.  
[requiredTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext-requiredTypes.html) | An IEnumerable of types that contains the type constraints for this search.  
[rootProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext-rootProperty.html) | The root HierarchyProperty on which the search is started.  
* * *
