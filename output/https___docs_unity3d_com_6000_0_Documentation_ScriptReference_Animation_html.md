* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html

# Animation
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html "Go to Animation Component in the Manual")
### Description
The animation component is used to play back animations.
You can assign animation clips to the animation component and control playback from your script. The animation system in Unity is weight-based and supports Animation Blending, Additive animations, Animation Mixing, Layers and full control over all aspects of playback.  
  
For an overview of animation scripting in Unity please [read this introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html).  
  
[AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) can be used to change the layer of an animation, modify playback speed, and for direct control over blending and mixing.  
  
Also [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) supports enumerators. Looping through all AnimationStates is performed like this:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        anim = GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();
        foreach (AnimationState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) state in anim)
        {
            state.speed = 0.5F;
        }
    }
}

```

Additional resources: An overview of animation scripting in Unity is [here](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html).
### Properties
Property | Description  
---|---  
[animatePhysics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-animatePhysics.html) | When enabled, the physics system uses animated transforms from GameObjects with kinematic Rigidbody components to influence other GameObjects.  
[clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-clip.html) | The default animation.  
[cullingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-cullingType.html) | Controls culling of this Animation component.  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-isPlaying.html) | Is an animation currently being played?  
[localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-localBounds.html) | AABB of this Animation animation component in local space.  
[playAutomatically](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-playAutomatically.html) | Should the default animation clip (the Animation.clip property) automatically start playing on startup?  
[this[string]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Index_operator.html) | Returns the animation state named name.  
[updateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-updateMode.html) | Specifies the update mode of the Animation.  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation-wrapMode.html) | How should time beyond the playback range of the clip be treated?  
### Public Methods
Method | Description  
---|---  
[AddClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.AddClip.html) | Adds a clip to the animation with name newName.  
[Blend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Blend.html) | Blends the animation named animation towards targetWeight over the next time seconds.  
[CrossFade](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.CrossFade.html) | Fades in the animation with the name animation over a period of time defined by fadeLength.  
[CrossFadeQueued](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.CrossFadeQueued.html) | Cross fades an animation after previous animations has finished playing.  
[GetClipCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.GetClipCount.html) | Get the number of clips currently assigned to this animation.  
[IsPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.IsPlaying.html) | Is the animation named name playing?  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html) | Plays an animation without blending.  
[PlayQueued](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.PlayQueued.html) | Plays an animation after previous animations has finished playing.  
[RemoveClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.RemoveClip.html) | Remove clip from the animation list.  
[Rewind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Rewind.html) | Rewinds the animation named name.  
[Sample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Sample.html) | Samples animations at the current state.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Stop.html) | Stops all playing animations that were started with this Animation.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
