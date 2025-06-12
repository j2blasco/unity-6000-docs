* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-layer.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).layer
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
layer; 
### Description
Integer identifying the layer the GameObject is assigned to.
This is the standard integer value which identifies the layer, not the [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html). You can use layers for selective rendering from cameras or to ignore Raycasts. Unity generates 32 layers, identified by standard integers from 0 to 31, and reserves some layers for its own systems. Refer to [ Create functional layers in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/create-layers.html) for a list of predefined layers and how to create your own new ones.  
  
To convert this `layer` identifier to a [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html), refer to [ Set a layerMask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html). To obtain the `string` name of the layer from this `layer` identifier, use [LayerMask.LayerToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html). Refer to [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) in the Manual for a comprehensive guide to using layers. 
```
// Put the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the ignore raycast layer (2)  
  
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Awake()
    {
        //gameObject.layer uses only integers, but we can turn a layer name into a layer integer using LayerMask.NameToLayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.NameToLayer.html)()
        int LayerIgnoreRaycast = LayerMask.NameToLayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.NameToLayer.html)("Ignore Raycast");
        gameObject.layer = LayerIgnoreRaycast;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Current layer: " + gameObject.layer);
    }
}

```

Additional resources: [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html)
* * *
