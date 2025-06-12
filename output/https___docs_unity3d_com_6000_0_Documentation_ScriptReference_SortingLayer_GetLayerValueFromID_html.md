* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.GetLayerValueFromID.html

#  [SortingLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.html).GetLayerValueFromID
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
public static int GetLayerValueFromID(int id); 
### Parameters
Parameter | Description  
---|---  
id | The unique value of the sorting layer as returned by any renderer's sortingLayerID property.  
### Returns
**int** The final sorting value of the layer relative to other layers. 
### Description
Returns the final sorting layer value. To determine the sorting order between the various sorting layers, use this method to retrieve the final sorting value and use CompareTo to determine the order.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int CompareLayer(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rhs, GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) lhs)
    {
        int rval = SortingLayer.GetLayerValueFromID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.GetLayerValueFromID.html)(rhs.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>().sortingLayerID);
        int lval = SortingLayer.GetLayerValueFromID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.GetLayerValueFromID.html)(lhs.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>().sortingLayerID);
        return rval.CompareTo(lval);
    }
}

```

Additional resources: [GetLayerValueFromName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.GetLayerValueFromName.html).
* * *
