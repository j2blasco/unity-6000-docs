* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.Equals.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).Equals
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
public bool Equals([GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) other); 
### Parameters
Parameter | Description  
---|---  
other | The other GlobalObjectId to compare with this instance.  
### Returns
**bool** Returns `true` if the two instances of GlobalObjectId are value equivalent. Otherwise, returns `false`. 
### Description
Checks if this unique object identifier and another are equal.
This method performs a value equality check. It returns true if the values of every property on this `GlobalObjectId` match the values of the equivalent properties on the `GlobalObjectId` supplied as a parameter. Any two instances of `GlobalObjectId` that are value equivalent must by definition identify the same object.  
  
Additional resources: [GlobalObjectId.CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.CompareTo.html)
* * *
