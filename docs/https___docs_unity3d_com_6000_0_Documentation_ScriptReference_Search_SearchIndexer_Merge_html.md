* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Merge.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).Merge
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
public void Merge(string[] removeDocuments, [Search.SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) other, int baseScore, Action<int,SearchIndexer,int> documentIndexing); 
### Parameters
Parameter | Description  
---|---  
removeDocuments | Documents to be removed as part of the merge operation. Can be null or empty.  
other | The other index to be merged into the current one.  
baseScore | Base score to give to all the merged indexes.  
documentIndexing | Utility callback used to inject last minutes indexes before merging the indexes of a document.  
### Description
Merge a search index content into the current index.
This is especially useful to do incremental updates of an index.
* * *
