* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.html

# AnimatorControllerLayer
class in UnityEditor.Animations
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
### Description
The Animation Layer contains a state machine that controls animations of a model or part of it.
### Properties
Property | Description  
---|---  
[avatarMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-avatarMask.html) | The AvatarMask that is used to mask the animation on the given layer.  
[blendingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-blendingMode.html) | The blending mode used by the layer. It is not taken into account for the first layer.  
[defaultWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-defaultWeight.html) | The default blending weight that the layers has. It is not taken into account for the first layer.  
[iKPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-iKPass.html) | When active, the layer will have an IK pass when evaluated. It will trigger an OnAnimatorIK callback.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-name.html) | The name of the layer.  
[stateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-stateMachine.html) | The state machine for the layer.  
[syncedLayerAffectsTiming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-syncedLayerAffectsTiming.html) | When active, the layer will take control of the duration of the Synced Layer.  
[syncedLayerIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer-syncedLayerIndex.html) | Specifies the index of the Synced Layer.  
### Public Methods
Method | Description  
---|---  
[GetOverrideBehaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.GetOverrideBehaviours.html) | Gets the override behaviour list for the state on the given layer.  
[GetOverrideMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.GetOverrideMotion.html) | Gets the override motion for the state on the given layer.  
[SetOverrideBehaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.SetOverrideBehaviours.html) | Sets the override behaviour list for the state on the given layer.  
[SetOverrideMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.SetOverrideMotion.html) | Sets the override motion for the state on the given layer.  
* * *
