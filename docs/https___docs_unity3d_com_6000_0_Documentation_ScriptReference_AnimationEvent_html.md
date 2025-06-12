* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html

# AnimationEvent
class in UnityEngine
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
AnimationEvent lets you call a script function similar to SendMessage as part of playing back an animation.
Animation events support functions that take zero or one parameter. The parameter can be a float, an int, a string, an object reference, or an AnimationEvent.
```
// Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) example
// Small example that can be called on each specified frame.
// The code is executed once per animation loop.  
  
using UnityEngine;
using System.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void PrintEvent()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("PrintEvent");
    }
}

```

A more detailed example below shows a more complex way of creating an animation. In this script example the `Animator` component is accessed and a `Clip` from it obtained. (This clip was set up in the Animation window.) The clip lasts for 2 seconds. An `AnimationEvent` is created, and has parameters set. The parameters include the function `PrintEvent()` which will handle the event. The event is then added to the clip. This all happens in `Start()`. Once the game has launched the event is called after 1.3s and then repeats every 2s.
```
// Add an Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)
using UnityEngine;
using System.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        // existing components on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip;
        Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) anim;  
  
        // new event created
        AnimationEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html) evt;
        evt = new AnimationEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html)();  
  
        // put some parameters on the AnimationEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html)
        //  - call the function called PrintEvent()
        //  - the animation on this object lasts 2 seconds
        //    and the new animation created here is
        //    set up to happen 1.3s into the animation
        evt.intParameter = 12345;
        evt.time = 1.3f;
        evt.functionName = "PrintEvent";  
  
        // get the animation clip and add the AnimationEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html)
        anim = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        clip = anim.runtimeAnimatorController.animationClips[0];
        clip.AddEvent(evt);
    }  
  
    // the function to be called as an event
    public void PrintEvent(int i)
    {
        print("PrintEvent: " + i + " called at: " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

### Properties
Property | Description  
---|---  
[animationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-animationState.html) | The animation state that fired this event (Read Only).  
[animatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-animatorClipInfo.html) | The animator clip info related to this event (Read Only).  
[animatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-animatorStateInfo.html) | The animator state info related to this event (Read Only).  
[floatParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-floatParameter.html) | Float parameter that is stored in the event and will be sent to the function.  
[functionName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-functionName.html) | The name of the function that will be called.  
[intParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-intParameter.html) | Int parameter that is stored in the event and will be sent to the function.  
[isFiredByAnimator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-isFiredByAnimator.html) | Returns true if this Animation event has been fired by an Animator component.  
[isFiredByLegacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-isFiredByLegacy.html) | Returns true if this Animation event has been fired by an Animation component.  
[messageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-messageOptions.html) | Function call options.  
[objectReferenceParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-objectReferenceParameter.html) | Object reference parameter that is stored in the event and will be sent to the function.  
[stringParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-stringParameter.html) | String parameter that is stored in the event and will be sent to the function.  
[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-time.html) | The time at which the event will be fired off.  
### Constructors
Constructor | Description  
---|---  
[AnimationEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent-ctor.html) | Creates a new animation event.  
* * *
