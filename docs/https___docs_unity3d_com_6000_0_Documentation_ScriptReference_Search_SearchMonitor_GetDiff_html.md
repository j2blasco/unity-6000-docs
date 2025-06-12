* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetDiff.html

#  [SearchMonitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.html).GetDiff
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
public static [Search.AssetIndexChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.AssetIndexChangeSet.html) GetDiff(long timestamp, IEnumerable<string> deletedAssets, Func<string,bool> predicate); 
### Parameters
Parameter | Description  
---|---  
timestamp | Timestamp to be compared.  
deletedAssets | Any untracked deleted assets.  
predicate | Predicate used to filter the asset changeset.  
### Returns
**AssetIndexChangeSet** Changeset. 
### Description
Returns the assets that changed since a point in time.
* * *
