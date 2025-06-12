* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.AssetIndexChangeSet-ctor.html

# AssetIndexChangeSet Constructor
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
public AssetIndexChangeSet(string[] updated, string[] removed); 
## Declaration
public AssetIndexChangeSet(IEnumerable<string> updated, IEnumerable<string> removed, IEnumerable<string> moved, Func<string,bool> predicate); 
## Declaration
public AssetIndexChangeSet(IEnumerable<string> updated, IEnumerable<string> removed, Func<string,bool> predicate); 
### Parameters
Parameter | Description  
---|---  
updated | Assets that were updated.  
removed | Assets that were deleted.  
moved | Existing assets that were moved.  
predicate | Predicate used to exclude any updated, removed or moved assets from the change set.  
### Description
Create a search asset index changeset.
* * *
