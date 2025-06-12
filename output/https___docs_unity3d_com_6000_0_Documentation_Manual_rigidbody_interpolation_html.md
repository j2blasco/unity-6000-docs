* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-interpolation.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Rigidbody physics](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)
  * Apply interpolation to a Rigidbody


[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-constant-force.html)
Apply constant force to a Rigidbody
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)
Rigidbody component reference
# Apply interpolation to a Rigidbody
Interpolation provides a way to manage the appearance of jitter in the movement of your [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/RigidbodiesOverview.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) at run time.
Jitter can happen when the rate of physics simulation updates (determined by the [Fixed Timestep](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TimeManager.html)A customizable frame-rate-independent interval that dictates when physics calculations and FixedUpdate() events are performed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TimeManager.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FixedTimestep)) is slower than the application’s frame rate. It is most noticeable if you have a Rigidbody with physics-based movement that the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) tracks at run time.
Unity’s PhysX system provides a way to implement interpolation. The **Interpolate** setting on a Rigidbody provides two options to smooth the appearance of a Rigidbody’s motion if it appears jittery at run time. These options are **Interpolate** and **Extrapolate**.
Both interpolation and extrapolation calculate the pose of the Rigidbody (that is, the position and rotation) between physics updates. Which one you should choose depends on which option produces the best visual outcome for your use case.
You should only use interpolation or extrapolation if you see jitter in your Rigidbody’s movement. **Interpolate** is set to **None** by default.
When interpolation or extrapolation is enabled, the physics system takes control of the Rigidbody’s transform. For this reason, you should follow any direct (non-physics) change to the transform with a [Physics.SyncTransforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SyncTransforms.html) call. Otherwise, Unity ignores any transform change that does not originate from the physics system.
## Interpolate
Use the pose of the Rigidbody from the previous two physics updates to calculate and apply the pose of the Rigidbody in the current frame.
Interpolate makes the Rigidbody appear to move slightly behind where it should be. This is because interpolation delays the Rigidbody’s pose by one physics update, so that it has two points to use for its calculation, and enough time to move the Rigidbody to the new pose.
Interpolation is more accurate than extrapolation, but it has a time lag of one physics update.
Interpolate is usually the best option for situations where the Rigidbody’s velocity varies, or if there are other physics elements that influence the Rigidbody’s movement.
Interpolate is represented by the API property [`RigidbodyInterpolation.Interpolate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation.Interpolate.html).
## Extrapolate
Use the pose of the Rigidbody from the previous physics update, and predict the pose of the Rigidbody in the next physics update, to calculate and predict the pose in the current frame.
Extrapolate makes the Rigidbody appear to move slightly ahead of where it should be. This is because extrapolation uses the Rigidbody’s current velocity to predict the Rigidbody’s pose in the next physics update, so that it has two points to use for its calculation.
Extrapolation is often less accurate, and might visibly overshoot **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) bounds (and then correct itself in the next frame, after the next physics update). This is because the extrapolation calculation does not take into account future physics forces or calculations.
Extrapolate is usually only a good option for situations where accuracy is not important; for example, if the Rigidbody moves at a constant velocity, and there are no other physics elements that influence the Rigidbody’s movement.
Extrapolate is represented by the API property [`RigidbodyInterpolation.Extrapolate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation.Extrapolate.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-constant-force.html)
Apply constant force to a Rigidbody
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)
Rigidbody component reference
