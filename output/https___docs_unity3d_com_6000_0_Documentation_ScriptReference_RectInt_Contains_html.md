* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.Contains.html

#  [RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html).Contains
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
public bool Contains([Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) position); 
### Parameters
Parameter | Description  
---|---  
position | Position to check.  
### Returns
**bool** Whether the position is within the [RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html). 
### Description
Returns true if the given position is within the [RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html).
A point is considered to lie within the RectInt if its coordinates are greater than or equal to the RectInt's min coordinates, and less than the RectInt's max coordinates.
* * *
