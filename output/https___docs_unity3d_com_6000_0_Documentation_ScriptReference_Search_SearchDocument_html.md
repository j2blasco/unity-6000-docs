* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument.html

# SearchDocument
struct in UnityEditor.Search
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
Represents a searchable document that has been indexed.
### Properties
Property | Description  
---|---  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument-id.html) | Document unique ID in the search index.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument-name.html) | Readable name of the document.  
[score](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument-score.html) | Document base relevance score.  
[source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument-source.html) | Original source from which the document was indexed. The source is usually the container asset, i.e. prefab, Unity scene or the imported asset itself.  
[valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument-valid.html) | If true the document is considered valid.  
### Constructors
Constructor | Description  
---|---  
[SearchDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument-ctor.html) | Create a new SearchDocument.  
### Public Methods
Method | Description  
---|---  
[CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument.CompareTo.html) | Compare this document against another document.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument.Equals.html) | Compare this document against another document.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument.ToString.html) | Returns the document ID string.  
* * *
