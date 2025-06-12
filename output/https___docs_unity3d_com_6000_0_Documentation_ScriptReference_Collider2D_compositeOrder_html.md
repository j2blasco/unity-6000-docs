* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOrder.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).compositeOrder
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
compositeOrder; 
### Description
The composite operation order to be used when a [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html) is used.
When this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is using any composite operation other than [Collider2D.CompositeOperation.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CompositeOperation.None.html), the composite operation uses the previous composite operation results on the [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html) as the input and applies this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) geometry using its selected [Collider2D.compositeOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOperation.html).  
  
The composite order is a simple integer value that is first sorted into ascending order by the [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html) before it applies the composite operations with the lowest value being executed first in order up to the highest values. When the composite order values are identical, the order is undefined. When using only [Collider2D.CompositeOperation.Merge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CompositeOperation.Merge.html) operations, this order is irrelevant to the final result.  
  
Using this order, it is possible to control which previous [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are also using the [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html) are affected by this composite operation.  
  
**NOTE:** After sorting the composite order for all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), the first composite operation of [Collider2D.CompositeOperation.Merge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CompositeOperation.Merge.html) will always used, independent of that [Collider2D.compositeOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOperation.html) property setting. This is due to the fact that the first operation has no input geometry for the operation to complete and only the merge (OR) composite operation results in any geometry!  
  
Additional resources: [CompositeOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CompositeOperation.html), [Collider2D.compositeOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOperation.html) and [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html).
* * *
