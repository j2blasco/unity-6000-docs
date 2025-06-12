* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.CompareTo.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).CompareTo
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
public int CompareTo([GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) other); 
### Parameters
Parameter | Description  
---|---  
other | The other GlobalObjectId to compare with this instance.  
### Returns
**int** Returns an integer that represents the relative sort order positions of the current instance and the other `GlobalObjectId`. Returns a negative integer if this instance precedes `other`. Returns a positive integer if this instance follows `other`. Returns zero if this instance and `other` have the same position in the sort order. 
### Description
Compares this unique object identifier with another to determine their relative positions in the sort order.
The sort order for comparison is [GlobalObjectId.assetGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-assetGUID.html), [GlobalObjectId.targetObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetObjectId.html), [GlobalObjectId.targetPrefabId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetPrefabId.html), then [GlobalObjectId.identifierType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-identifierType.html).  
  
**Note** : To check if two instances of `GlobalObjectId` are equivalent, use [GlobalObjectId.Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.Equals.html) instead. 
* * *
