* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessGameObjectWithAnimatedUserProperties.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessGameObjectWithAnimatedUserProperties(GameObject, EditorCurveBinding[])
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
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject with animated custom properties.  
bindings | The animation curves bound to the custom properties.  
### Description
This function is called when the animation curves for a custom property are finished importing.
It is called for every GameObject with an animated custom property. Each animated property has an animation curve that is represented by an [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html). This lets you dynamically add components to a GameObject and retarget the EditorCurveBindings to any animatable property.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyAllPostprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPostprocessGameObjectWithAnimatedUserProperties(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, EditorCurveBinding[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html)[] bindings)
    {
        // add a particle emitter to every game object that has a custom property called "particleAmount"
        // then map the animation to the emission rate
        for (int i = 0; i < bindings.Length; i++)
        {
            if (bindings[i].propertyName == "particlesAmount")
            {
                ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) emitter = go.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
                var emission = emitter.emission;
                emission.rateOverTimeMultiplier = 0;  
  
                bindings[i].propertyName = "EmissionModule.rateOverTime.scalar";
                bindings[i].path = AnimationUtility.CalculateTransformPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.CalculateTransformPath.html)(go.transform, go.transform.root);
                bindings[i].type = typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html));
            }
        }
    }
}

```

* * *
