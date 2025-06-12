* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-particle-trigger.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle physics](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics.html)
  * Configure a particle trigger


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-triggers.html)
Particle triggers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html)
Particle System Force Field component reference
# Configure a particle trigger
To begin, specify which **Colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) the particles can interact with. To do this, assign one or more Colliders to the **Colliders** list property. To increase the number of Colliders in the list, click the Add (+) button beneath the list of Colliders. To remove a Collider from the list, select the Collider and click the Remove (-) button. If you have not yet assigned a Collider to an index of the list, you can use the smaller Add (+) button, to the right of the empty entry, to create and assign a new Collider. This creates a new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) as a child of the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) and attaches a **Sphere Collider** A sphere-shaped collider component that handles collisions for GameObjects like balls or other things that can be roughly approximated as a sphere for the purposes of physics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SphereCollider) to it, then assigns the Collider to the empty entry.
After you add the Colliders, you can then specify what a particle does when it meets the criteria for passing a particular trigger event type. There are four event types that describe how a particle can interact with a Collider. They are:
  * **Inside** : A particle is inside a Collider’s bounds.
  * **Outside** : A particle is outside a Collider’s bounds.
  * **Enter** : A particle enters a Collider’s bounds.
  * **Exit** : A particle exits a Collider’s bounds.


In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), there is a drop-down for each of these event types that lets you select what should happen to a particle if it passes the trigger event’s conditions. The options are:
  * **Callback** : Allows you to access the particle in the OnParticleTrigger() callback function.
  * **Kill** : Destroys the particle. You can not access the particle in the OnParticleTrigger() callback function.
  * **Ignore** : Ignores the particle. You can not access the particle in the OnParticleTrigger() callback function.


## Accessing particles within OnParticleTrigger()
If you select **Callback** as the reaction to one of the trigger events, you can access the particles that fulfill the event condition from an attached script. To do this, you first need to add the `OnParticleTrigger()` function to an attached script. Inside this function, call the [ParticlePhysicsExtensions.GetTriggerParticles()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetTriggerParticles.html) function to get the list of particles that fulfill the trigger event’s criteria. This function takes a [ParticleSystemTriggerEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTriggerEventType.html), which specifies the trigger event you want to get the particles for (**Inside** , **Outside** , **Enter** , or **Exit**), and a list of [Particles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particle) which the function populates with the result. From the list, you can access, modify, or destroy any particle. The function can also take an optional parameter which outputs **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) information, such as which Collider each particle triggered. The **Collider Query Mode** property controls what information is available through this parameter.
For more information on the API and how to use it, see the [below example](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-particle-trigger.html#Example).
## Examples
### Interaction with a collider
The example below causes particles to turn red as they enter the Collider’s bounds, then turn green as they leave the Collider’s bounds.
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

[ExecuteInEditMode]
public class TriggerScript : MonoBehaviour
{
    ParticleSystem ps;

    // these lists are used to contain the particles which match
    // the trigger conditions each frame.
    List<ParticleSystem.Particle> enter = new List<ParticleSystem.Particle>();
    List<ParticleSystem.Particle> exit = new List<ParticleSystem.Particle>();

    void OnEnable()
    {
        ps = GetComponent<ParticleSystem>();
    }

    void OnParticleTrigger()
    {
        // get the particles which matched the trigger conditions this frame
        int numEnter = ps.GetTriggerParticles(ParticleSystemTriggerEventType.Enter, enter);
        int numExit = ps.GetTriggerParticles(ParticleSystemTriggerEventType.Exit, exit);

        // iterate through the particles which entered the trigger and make them red
        for (int i = 0; i < numEnter; i++)
        {
            ParticleSystem.Particle p = enter[i];
            p.startColor = new Color32(255, 0, 0, 255);
            enter[i] = p;
        }

        // iterate through the particles which exited the trigger and make them green
        for (int i = 0; i < numExit; i++)
        {
            ParticleSystem.Particle p = exit[i];
            p.startColor = new Color32(0, 255, 0, 255);
            exit[i] = p;
        }

        // re-assign the modified particles back into the particle system
        ps.SetTriggerParticles(ParticleSystemTriggerEventType.Enter, enter);
        ps.SetTriggerParticles(ParticleSystemTriggerEventType.Exit, exit);
    }
}


```

See the images below for the result of this example:
![Editor view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysTriggersModule-ExampleEditorView.jpg) Editor view ![Game view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysTriggersModule-ExampleGameView.jpg) Game view
### Interaction with multiple colliders
The following example takes advantage of the additional collision data you can extract from the `GetTriggerParticles()` function. It causes particles inside the first Collider’s bounds to turn red, inside the second Collider’s bounds to turn blue, or inside both Colliders to turn green. It also turns particles white if they are not inside a Collider. For this example, **Collider Query Mode** is set to **All**.
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

[ExecuteInEditMode]
public class TriggerScript : MonoBehaviour
{
    void OnParticleTrigger()
    {
        ParticleSystem ps = GetComponent();
 
        // particles
        List inside = new List();
        List exit = new List();
 
        // get
        int numInside = ps.GetTriggerParticles(ParticleSystemTriggerEventType.Inside, inside, out var insideData);
        int numExit = ps.GetTriggerParticles(ParticleSystemTriggerEventType.Exit, exit);
 
        // iterate
        for (int i = 0; i < numInside; i++)
        {
            ParticleSystem.Particle p = inside[i];
            if (insideData.GetColliderCount(i) == 1)
            {
                if (insideData.GetCollider(i, 0) == ps.trigger.GetCollider(0))
                    p.startColor = new Color32(255, 0, 0, 255);
                else
                    p.startColor = new Color32(0, 0, 255, 255);
            }
            else if (insideData.GetColliderCount(i) == 2)
            {
                p.startColor = new Color32(0, 255, 0, 255);
            }
            inside[i] = p;
        }
        for (int i = 0; i < numExit; i++)
        {
            ParticleSystem.Particle p = exit[i];
            p.startColor = new Color32(1, 1, 1, 255);
            exit[i] = p;
        }
 
        // set
        ps.SetTriggerParticles(ParticleSystemTriggerEventType.Inside, inside);
        ps.SetTriggerParticles(ParticleSystemTriggerEventType.Exit, exit);
    }
}


```

See the following image for the result of this example:
![Game view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysTriggersModule-Example2.png) Game view
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-triggers.html)
Particle triggers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html)
Particle System Force Field component reference
