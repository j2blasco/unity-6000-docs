* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.SkipEntry.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).SkipEntry
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
public bool SkipEntry(string document, bool checkRoots); 
### Parameters
Parameter | Description  
---|---  
document | Path of a document.  
checkRoots | Check Roots.  
### Returns
**bool** Returns true if the document doesn't need to be indexed. 
### Description
Called when the index is built to see if a specified document needs to be indexed. See [SearchIndexer.skipEntryHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-skipEntryHandler.html).
* * *
