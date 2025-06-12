* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Handling events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html)
  * Event functions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html)
Handling events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html)
Order of execution for event functions
# Event functions
Event functions are a set of predefined callbacks that all [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html) script components can potentially receive. The callbacks are triggered by various Unity Editor and Engine events, including:
  * [Regular frame and physics updates](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html#regular-updates)
  * Object [lifecycle events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html#initialization-events), such as initialization and destruction of objects in a scene
  * [UI events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html#gui-events)
  * [Physics events](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html#physics-events)


Implement the appropriate method signature in your `MonoBehaviour`-derived class to allow your game objects to react to the source events.
Refer to the [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) Scripting API reference page for a full list of the available callbacks, where they are listed under **Messages**. The rest of this section gives an overview of some of the key groups of event functions.
## Regular update events
A game is like an animation where the animation frames are generated on the fly. A key concept in games programming is making changes to position, state, and behavior of objects just before each frame is rendered. The [`Update`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) function is the main place for this kind of code in Unity. `Update` is called before the frame is rendered and also before animations are calculated.
```
void Update() {
    float distance = speed * Time.deltaTime * Input.GetAxis("Horizontal");
    transform.Translate(Vector3.right * distance);
}


```

The physics system also updates in discrete time steps in a similar way to the frame rendering. A separate event function called [`FixedUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) is called just before each physics update. Since the physics updates and frame updates don’t occur with the same frequency, you can get more accurate results from physics code if you place it in the `FixedUpdate` function rather than `Update`.
```
void FixedUpdate() {
    Vector3 force = transform.forward * driveForce * Input.GetAxis("Vertical");
    rigidbody.AddForce(force);
}


```

It’s also sometimes useful to make additional changes at a point after the `Update` and `FixedUpdate` functions have been called for all objects in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), and after all animations have been calculated. Some examples of this scenario are:
  * When a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) should remain trained on a target object. The adjustment to the camera’s orientation must be made after the target object has moved.
  * When the script code should override the effect of an animation. For example, to make a character’s head look towards a target object in the scene.


The [`LateUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html) function can be used for these kinds of situations.
```
void LateUpdate() {
    Camera.main.transform.LookAt(target.transform);
}


```

## Initialization events
It’s often useful to be able to call initialization code in advance of any updates that occur during gameplay. The [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html) function is called before the first frame or physics update on an object. The [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) function is called for each object in the scene at the time when the scene loads. Note that although the various objects’ `Start` and `Awake` functions are called in arbitrary order, all instances of `Awake` will have finished before the first `Start` is called. This means that code in a `Start` function can make use of other initializations previously carried out in the `Awake` phase.
## GUI events
Unity has a system for rendering GUI controls over the main action in the scene and responding to clicks on these controls. This code is handled somewhat differently from the normal frame update and so it should be placed in the [OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnGUI.html) function, which will be called periodically.
```
void OnGUI() {
    GUI.Label(labelRect, "Game Over");
}


```

You can also detect mouse events that occur over a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) as it appears in the scene. This can be used for targeting weapons or displaying information about the character currently under the mouse pointer. A set of event functions named with the prefix `OnMouse` (e.g., [OnMouseOver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseOver.html), [OnMouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDown.html)) allow a script to react to user actions with the mouse. For example, if the mouse button is pressed while the pointer is over a particular object then an `OnMouseDown` function in that object’s script will be called if it exists.
## Physics events
The **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) will report **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) against an object by calling event functions on that object’s script. The [OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html), [OnCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionStay.html) and [OnCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionExit.html) functions will be called as contact is made, held and broken. The corresponding [OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter.html), [OnTriggerStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerStay.html) and [OnTriggerExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerExit.html) functions will be called when the object’s **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) is configured as a Trigger (ie, a collider that simply detects when something enters it rather than reacting physically). These functions may be called several times in succession if more than one contact is detected during the physics update and so a parameter is passed to the function giving details of the collision (position, identity of the incoming object, etc).
```
void OnCollisionEnter(Collision collision) {
    if (collision.gameObject.tag == "Arrow") {
        ApplyDamage(10);
    }
}


```

## Additional resources
  * [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html)
  * [Execution order of event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html)
  * [MonoBehaviour API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/event-handling.html)
Handling events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html)
Order of execution for event functions
