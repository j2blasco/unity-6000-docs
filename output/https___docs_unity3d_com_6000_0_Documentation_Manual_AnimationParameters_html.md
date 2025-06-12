* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  * Animation Parameters


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html)
Animation States
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineTransitions.html)
State Machine Transitions
# Animation Parameters
Animation Parameters are variables that are defined within an **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) that can be accessed and assigned values from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). This is how a script can control or affect the flow of the **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine).
![Animation Parameters in the Animator window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorParametersSection.png) Animation Parameters in the Animator window.
For example, the value of a parameter can be updated by an [animation curve](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimationCurves.html) and then accessed from a script so that, say, the pitch of a sound effect can be varied as if it were a piece of animation. Likewise, a script can set parameter values to be picked up by Mecanim. For example, a script can set a parameter to control a [Blend Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html).
Default parameter values can be set up using the Parameters section of the **Animator window** The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow), selectable in the top right corner of the Animator window. They can be of four basic types: 
  * _Integer_ - a whole number
  * _Float_ - a number with a fractional part
  * _Bool_ - true or false value (represented by a checkbox)
  * _Trigger_ - a boolean parameter that is reset by the controller when consumed by a transition (represented by a circle button)


Parameters can be assigned values from a script using functions in the Animator class: [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetFloat.html), [SetInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetInteger.html), [SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetBool.html), [SetTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTrigger.html), and [ResetTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.ResetTrigger.html).
Here’s an example of a script that modifies parameters based on user input and **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection:
```
using UnityEngine;
using System.Collections;

public class SimplePlayer : MonoBehaviour {

    Animator animator;
    
    // Use this for initialization
    void Start () {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update () {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        bool fire = Input.GetButtonDown("Fire1");

        animator.SetFloat("Forward",v);
        animator.SetFloat("Strafe",h);
        animator.SetBool("Fire", fire);
    }

    void OnCollisionEnter(Collision col) {
        if (col.gameObject.CompareTag("Enemy"))
        {
            animator.SetTrigger("Die");
        }
    }
}


```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html)
Animation States
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineTransitions.html)
State Machine Transitions
