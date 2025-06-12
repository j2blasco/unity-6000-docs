* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.Contains.html

#  [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html).Contains
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
public bool Contains([Vector3Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html) position); 
### Parameters
Parameter | Description  
---|---  
position | Point to check.  
### Returns
**bool** Is `point` contained in the bounding box? 
### Description
Is `point` contained in the bounding box?
A point is contained in the bounding box if its x, y and z components are greater or equal to [BoundsInt.xMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-xMin.html), [BoundsInt.yMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-yMin.html) and [BoundsInt.zMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-zMin.html) respectively, and less than [BoundsInt.xMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-xMax.html), [BoundsInt.yMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-yMax.html) and [BoundsInt.zMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-zMax.html) respectively.
* * *
