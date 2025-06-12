* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html

#  [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html).GetMask
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
public static int GetMask(params string[] layerNames); 
### Parameters
Parameter | Description  
---|---  
layerNames | List of layer names to convert to a layer mask.  
### Returns
**int** The layer mask created from the `layerNames`. 
### Description
Given a set of layer names as defined by either a Builtin or a User Layer in the [Tags and Layers manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html), returns the equivalent layer mask for all of them.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(LayerMask.GetMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html)("UserLayerA", "UserLayerB"));
    }
}

```

**Note:** Suppose `UserLayerA` and `UserLayerB` are the tenth and eleventh layers. These will have a User Layer values of 10 and 11. To obtain their layer mask value their names can be passed into [GetMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html). The argument can either be a list of their names or an array of strings storing their names. In this case the return value will be 2^10 + 2^11 = 3072.
* * *
