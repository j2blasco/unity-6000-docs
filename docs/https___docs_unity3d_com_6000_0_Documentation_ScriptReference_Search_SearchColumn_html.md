* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html

# SearchColumn
class in UnityEditor.Search
Leave feedback
  

Implements interfaces:[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)
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
Search columns are used to display additional information in the Search Table view.
See [SearchProvider.fetchColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchColumns.html) and [SearchColumnProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnProviderAttribute.html) for some examples.
### Properties
Property | Description  
---|---  
[binder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-binder.html) | If defined, the binder delegate is used to apply contextual data to a visual element.  
[cellCreator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-cellCreator.html) | If defined, the cell creator delegate is used to customize how the search column displays its information.  
[comparer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-comparer.html) | If defined, the comparer delegate is used to sort search results based on the value displayed in that column.  
[content](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-content.html) | The content is used to display the search column label and image in its header.  
[drawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-drawer.html) | If defined, the drawer delegate is used to customize how the search column displays its information.  
[getter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-getter.html) | If defined, the getter delegate is used to customize how the search field data is extracted and transformed for display (see SearchColumn.drawer).  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-name.html) | Name of the search column.  
[options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-options.html) | Various options used to define how a search column is presented.  
[path](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-path.html) | The path can be used by the column delegates to interpret how the data can be manipulated.  
[provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-provider.html) | The provider is used to indicate which search column provider (see SearchColumn) is used to define the search column format.  
[selector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-selector.html) | The selector is used by the column delegates to fetch the search field data.  
[setter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-setter.html) | If defined, the setter delegate writes back the value to the corresponding field of the search result.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-width.html) | The column width is used to set the Search Table view column width.  
### Constructors
Constructor | Description  
---|---  
[SearchColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-ctor.html) | Creates a new search column.  
### Public Methods
Method | Description  
---|---  
[InitFunctors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.InitFunctors.html) | Initialize the column provider functors.  
### Static Methods
Method | Description  
---|---  
[Enumerate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.Enumerate.html) | Enumerate a set of columns for a variety of search items.  
* * *
