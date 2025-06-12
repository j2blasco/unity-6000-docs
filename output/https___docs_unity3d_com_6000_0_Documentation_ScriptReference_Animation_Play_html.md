* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html

#  [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html).Play
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
## Declaration
public bool Play([PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) mode = PlayMode.StopSameLayer); 
## Declaration
public bool Play(string animation, [PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) mode = PlayMode.StopSameLayer); 
### Returns
**bool** If no name is supplied and there is no default animation, then this method returns `false`. Otherwise, it returns `true`. 
### Description
Plays an animation without blending.
If no name is supplied then the default animation plays. Use the optional [PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) to choose how this animation affects animations already playing.  
  
If the specified animation is already playing then other animations will be stopped but the animation will not rewind to the beginning. When the end of the animation is reached it will automatically be stopped and rewound to the start unless the [PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) is set to Loop. If [Animation.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html) is called on an object during a frame update where the object is also [deactivated](https://docs.unity3d.com/6000.0/Documentation/Manual/DeactivatingGameObjects.html) then the call will effectively be cancelled. The animation will not start playing when the object is later reactivated. However, if a call on a subsequent frame (while the object is still inactive) then the animation will start playing after reactivation.  
  
To use [Animation.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html) the animation data must be visible in the Inspector window. This window contains all animations for a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in an array. As an example two animations `jump` and `spin` are stored in the Animations list. [Animation.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html) can play each of these animations. [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) can also combine animations. An (unsupported and undocumented) [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).`layer` is used for this. For example leaving `jump` at layer zero and moving `spin` to layer 123 will allow them to be played together.  
  
Animations must be marked as ‘Legacy’ in the Inspector for the animations to be found by this method. This option appears after switching the Inspector Window to ‘Debug’.
```
using UnityEngine;  
  
// Animation.Play[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html) example. Let the S and J keys start
// a spin or jump animation. Let Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) play back spin and
// jump at the same time. Let Z play spin and jump with
// spin doubled in speed.
//
// Spin: rotate the cube 360 degrees in half or one second
// Jump: bounce up to 2 units and down in one second
//
// Note: AnimationState.layer is no longer supported, but still exists.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        anim = gameObject.GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();
        anim["spin"].layer = 123;
    }  
  
    // double the spin speed when true
    private bool fastSpin = false;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // leave spin or jump to complete before changing
        if (anim.isPlaying)
        {
            return;
        }  
  
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.S[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.S.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Spinning");
            anim.Play("spin");
        }  
  
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.J[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.J.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Jumping");
            anim.Play("jump");
        }  
  
        // combine jump and spin
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Jumping and spinning");
            anim.Play("jump");
            anim.Play("spin");
        }  
  
        // have spin speed reverted to 1.0 second
        if (fastSpin == true)
        {
            anim["spin"].speed = 1.0f;
            fastSpin = false;
        }  
  
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Z[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Z.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Jumping and spinning in half a second");
            anim.Play("jump");
            anim["spin"].speed = 2.0f;
            anim.Play("spin");  
  
            // we've used spin at a speed of two, now mark
            // the spin speed to revert back to one
            fastSpin = true;
        }
    }
}

```

* * *
