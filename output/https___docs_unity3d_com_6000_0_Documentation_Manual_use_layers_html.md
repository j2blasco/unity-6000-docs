* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/use-layers.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
  * Uses of layers in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
Layers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-layers.html)
Create functional layers in Unity
# Uses of layers in Unity
You can use layers to optimize your project and workflow. Common uses of layers include:
  * Layer-based rendering
  * Layer-based collision


## Use the Camera culling mask with layers
You can render only the objects in a particular layer, or selection of layers, if you use the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s **culling mask** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask). To change the culling mask, select the camera you want to use, and select the **Culling Mask** dropdown in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. If you clear the checkbox of a layer, it doesn’t render in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
**Note** : UI elements and screen space canvas children are exceptions to this and render regardless.
## Ray cast with layers
You can use layers to specify which GameObjects that a ray cast can intersect with. To make a ray cast ignore a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), you can assign it to the Ignore Raycast layer, or pass a [LayerMask](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html) to the ray cast API call.
If you don’t pass a LayerMask to the ray cast API call, Unity uses [Physics.DefaultRaycastLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.DefaultRaycastLayers.html) which matches every layer except Ignore Raycast.
The Physics.Raycast function uses a bitmask, and each bit determines if a layer is ignored by rays or not. If all bits in the layerMask are on, the ray collides against all **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider). If the layerMask = 0, there are no **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision).
For example, if you want to cast a ray on layer 8, see the code sample below:
```
int layerMask = 1 << 8;

// Does the ray intersect any objects which are in layer 8?
if (Physics.Raycast(transform.position, Vector3.forward, Mathf.Infinity, layerMask))
{
    Debug.Log("The ray hit the player");
}

```

You can then do the inverse, so that the ray collides with all layers except layer 8.
```
void Update ()
{
    // Bit shift the index of the layer (8) to get a bit mask
    int layerMask = 1 << 8;

    // This casts rays only against colliders in layer 8.
    // But to collide against everything except layer 8, use the ~ operator because it inverts a bitmask.
    layerMask = ~layerMask;

    RaycastHit hit;
    // Does the ray intersect any objects excluding layer 8.
    if (Physics.Raycast(transform.position, transform.TransformDirection (Vector3.forward), out hit, Mathf.Infinity, layerMask))
    {
        Debug.DrawRay(transform.position, transform.TransformDirection (Vector3.forward) * hit.distance, Color.yellow);
        Debug.Log("Did Hit");
    }
    else
    {
        Debug.DrawRay(transform.position, transform.TransformDirection (Vector3.forward) *1000, Color.white);
        Debug.Log("Did not Hit");
    }
}

```

**Note** : If you don’t pass a layerMask to the Raycast function, it still ignores colliders that use the IgnoreRaycast layer.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
Layers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-layers.html)
Create functional layers in Unity
