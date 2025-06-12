* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.NameToLayer.html

#  [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html).NameToLayer
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
public static int NameToLayer(string layerName); 
### Description
Given a layer name, returns the layer index as defined by either a Builtin or a User Layer in the [Tags and Layers manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).
Returns -1 if not found.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(LayerMask.NameToLayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.NameToLayer.html)("TransparentFX"));
    }
}

```

* * *
