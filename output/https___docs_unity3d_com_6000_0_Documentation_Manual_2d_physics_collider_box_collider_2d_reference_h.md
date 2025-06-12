* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/box-collider-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/collider-2d-landing.html)
  * Box Collider 2D component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/circle-collider-2d-reference.html)
Circle Collider 2D component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/polygon-collider-2d-reference.html)
Polygon Collider 2D component reference
# Box Collider 2D component reference
The Box **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2D component is a [Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/collider-2d-landing.html) that interacts with the 2D physics system for **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection. This collider 2D is a rectangle with a defined position, width, and height in the local coordinate space of a **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite). Adjust the component properties to change the shape and behavior of the collider 2D.
**Note** : The selection rectangle is axis-aligned, with its edges parallel to the x or y axes of local space. 
**Property** | **Function**  
---|---  
**Material** | Select the [Physics Material 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-material-2d-reference.html)Use to adjust the friction and bounce that occurs between 2D physics objects when they collide [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-material-2d-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsMaterial2D) that determines properties of collisions, such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Composite Operations** | Select the [composite operation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CompositeOperation.html) used by an attached [Composite Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html) component.  
  
**Note:** When you select any operation besides **None** , the following properties—**Material** , **Is Trigger** , **Used By Effector** , and **Edge Radius** —become controlled by the attached Composite Collider 2D component and are no longer available in this collider’s properties.  
**None** | Select this to have no composite operation take place.  
**Merge** | Select this to have this composite operation compose geometry using a Boolean OR operation.  
**Intersect** | Select this to have this composite operation compose geometry using a Boolean AND operation.  
**Difference** | Select this to have this composite operation compose geometry using a Boolean NOT operation.  
**Flip** | Select this to have this composite operation compose geometry using a Boolean XOR operation.  
**Auto Tiling** | Enable this if the [Sprite Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteRenderer) component for the selected Sprite has the **Draw Mode** set to **Tiled**. This enables automatic updates to the shape of the [Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/collider-2d-landing.html), allowing the shape to automatically readjust when the Sprite’s dimensions change. If you don’t enable **Auto Tiling** , the Collider 2D geometry doesn’t automatically repeat.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Size** | Set the size of the box in local space units.  
**Edge Radius** | Set a value that forms a radius around the edge of the Collider. This results in a larger Collider 2D with rounded convex corners. The default value is 0 (no radius).  
**Layer Overrides** | Expand for the Layer override settings.  
**Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-layerOverridePriority.html) page for more information.  
**Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-includeLayers.html) documentation for more information.  
**Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-excludeLayers.html) documentation for more information.  
**Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceSendLayers.html) documentation for more information.  
**Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceReceiveLayers.html) documentation for more information.  
**Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-contactCaptureLayers.html) documentation for more information.  
**Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its [API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-callbackLayers.html) documentation for more information.  
## Additional resources
  * [Collider 2D API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html)
  * [Rigidbody 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-landing.html)


BoxCollider2D
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/circle-collider-2d-reference.html)
Circle Collider 2D component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/polygon-collider-2d-reference.html)
Polygon Collider 2D component reference
