* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GetCompositedColliders.html

#  [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html).GetCompositedColliders
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
public int GetCompositedColliders(List<Collider2D> colliders); 
### Parameters
Parameter | Description  
---|---  
colliders | A list of Collider2D that are being composited.  
### Returns
**int** The number of colliders returned. 
### Description
When any [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is using any composite operation other than [Collider2D.CompositeOperation.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CompositeOperation.None.html) then it is used by this [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html).
The order of the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) returned is sorted into ascending composite order as defined by [Collider2D.compositeOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOrder.html).  
  
Additional resources: [Collider2D.compositeOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOperation.html) and [Collider2D.compositeOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOrder.html).
* * *
