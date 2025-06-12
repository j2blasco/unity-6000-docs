* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.NameToRenderingLayer.html

#  [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html).NameToRenderingLayer
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
public static int NameToRenderingLayer(string layerName); 
### Parameters
Parameter | Description  
---|---  
layerName | Provide a rendering layer name.  
### Returns
**int** Returns -1 if not found. 
### Description
Given a rendering layer name, returns the rendering layer index as defined in the [Tags and Layers manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints the name of the rendering layer 1  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(RenderingLayerMask.NameToRenderingLayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.NameToRenderingLayer.html)("Default"));
    }
}

```

* * *
