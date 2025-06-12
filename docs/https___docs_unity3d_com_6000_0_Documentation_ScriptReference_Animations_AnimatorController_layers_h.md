* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController-layers.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).layers
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
layers; 
### Description
The layers in the controller.
It's important to note that the [AnimatorControllerLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.html) are returned as a copy. The array should be set back into the property when changed.
```
class ControllerModifier
{
    UnityEditor.Animations.AnimatorController controller;  
  
    public void ModifyLayers(int layerIndex, string newName)
    {
        UnityEditor.Animations.AnimatorControllerLayer[] layers = controller.layers;
        layers[layerIndex].name = newName;
        controller.layers = layers;
    }
}

```

* * *
