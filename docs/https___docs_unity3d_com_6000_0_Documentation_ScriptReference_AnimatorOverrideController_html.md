* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html

# AnimatorOverrideController
class in UnityEngine
/
Inherits from:[RuntimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeAnimatorController.html)
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
### Description
Interface to control Animator Override Controller.
Animator Override Controller is used to override Animation Clips from a controller to specialize animations for a given Avatar. Swapping [Animator.runtimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-runtimeAnimatorController.html) with an [AnimatorOverrideController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html) based on the same [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html) at runtime doesn't reset state machine's current state.  
  
There are three ways to use the Animator Override Controller.  
**1. Create an Animator Override Controller in the Editor.**  
**2. Change one Animation Clip per frame at runtime (Basic use case).**  
In this case the indexer operator [AnimatorOverrideController.this[string]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.Index_operator.html) could be used, but be careful as each call will trigger a reallocation of the animator's clip bindings.
```
using UnityEngine;  
  
public class SwapWeapon : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)[] weaponAnimationClip;  
  
    protected Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;
    protected AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html) animatorOverrideController;  
  
    protected int weaponIndex;  
  
    public void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        weaponIndex = 0;  
  
        animatorOverrideController = new AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html)(animator.runtimeAnimatorController);
        animator.runtimeAnimatorController = animatorOverrideController;
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("NextWeapon"))
        {
            weaponIndex = (weaponIndex + 1) % weaponAnimationClip.Length;
            animatorOverrideController["shot"] = weaponAnimationClip[weaponIndex];
        }
    }
}

```

**3. Changing many Animation Clips per frame at runtime (Advanced use case).**   
The [AnimatorOverrideController.ApplyOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.ApplyOverrides.html) method is well suited for this case as it reduce the number of animator's clips bindings reallocation to only one per call.
```
using UnityEngine;
using System.Collections.Generic;  
  
public class AnimationClipOverrides : List<KeyValuePair<AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html), AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)>>
{
    public AnimationClipOverrides(int capacity) : base(capacity) {}  
  
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) this[string name]
    {
        get { return this.Find(x => x.Key.name.Equals(name)).Value; }
        set
        {
            int index = this.FindIndex(x => x.Key.name.Equals(name));
            if (index != -1)
                this[index] = new KeyValuePair<AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html), AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)>(this[index].Key, value);
        }
    }
}  
  
public class Weapon
{
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) singleAttack;
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) comboAttack;
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) dashAttack;
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) smashAttack;
}  
  
public class SwapWeapon : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Weapon[] weapons;  
  
    protected Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;
    protected AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html) animatorOverrideController;  
  
    protected int weaponIndex;  
  
    protected AnimationClipOverrides clipOverrides;
    public void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        weaponIndex = 0;  
  
        animatorOverrideController = new AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html)(animator.runtimeAnimatorController);
        animator.runtimeAnimatorController = animatorOverrideController;  
  
        clipOverrides = new AnimationClipOverrides(animatorOverrideController.overridesCount);
        animatorOverrideController.GetOverrides(clipOverrides);
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("NextWeapon"))
        {
            weaponIndex = (weaponIndex + 1) % weapons.Length;
            clipOverrides["SingleAttack"] = weapons[weaponIndex].singleAttack;
            clipOverrides["ComboAttack"] = weapons[weaponIndex].comboAttack;
            clipOverrides["DashAttack"] = weapons[weaponIndex].dashAttack;
            clipOverrides["SmashAttack"] = weapons[weaponIndex].smashAttack;
            animatorOverrideController.ApplyOverrides(clipOverrides);
        }
    }
}

```

### Properties
Property | Description  
---|---  
[overridesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController-overridesCount.html) | Returns the count of overrides.  
[runtimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController-runtimeAnimatorController.html) | The Runtime Animator Controller that the Animator Override Controller overrides.  
[this[string]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.Index_operator.html) | Returns either the overriding Animation Clip if set or the original Animation Clip named name.  
### Constructors
Constructor | Description  
---|---  
[AnimatorOverrideController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController-ctor.html) | Creates an empty Animator Override Controller.  
### Public Methods
Method | Description  
---|---  
[ApplyOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.ApplyOverrides.html) | Applies the list of overrides on this Animator Override Controller.  
[GetOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.GetOverrides.html) | Gets the list of Animation Clip overrides currently defined in this Animator Override Controller.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[animationClips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeAnimatorController-animationClips.html) | Retrieves all AnimationClip used by the controller.  
### Public Methods
Method | Description  
---|---  
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
