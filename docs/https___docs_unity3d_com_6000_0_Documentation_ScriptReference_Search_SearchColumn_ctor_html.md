* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-ctor.html

# SearchColumn Constructor
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
## Declaration
public SearchColumn(string path, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [Search.SearchColumnFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnFlags.html) options); 
## Declaration
public SearchColumn(string path, string selector, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [Search.SearchColumnFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnFlags.html) options); 
## Declaration
public SearchColumn(string path, string selector, string provider, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [Search.SearchColumnFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnFlags.html) options); 
### Parameters
Parameter | Description  
---|---  
path | Serialization path of the column.  
content | Content to render the column header.  
options | Column flags.  
selector | Selector used to fetch the field data of a search item. See [SearchSelectorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelectorAttribute.html).  
provider | Column provider used to manage the column. See [SearchColumnProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnProviderAttribute.html).  
### Description
Creates a new search column.
* * *
