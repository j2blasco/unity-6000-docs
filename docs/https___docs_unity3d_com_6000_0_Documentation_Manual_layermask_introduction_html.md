* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-introduction.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
  * [Layers and layerMasks](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
  * Introduction to layerMasks


[](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
Layers and layerMasks
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html)
Set a layerMask
# Introduction to layerMasks
Every **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) exists on a single layer, but Unity APIs that let you set which layers the API affect don’t directly use layers. Instead, they use layerMasks.
A [layer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-layer.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer) is a standard integer, but a layerMask is an integer formatted as a bitmask where every `1` represents a layer to include and every `0` represents a layer to exclude. This means that you can pass a layer to an API that expects a layerMasks and the script will still compile because layers and layerMasks use the same underlying type. However, the API call won’t produce the behavior you expect.
For example, if you want to perform a [RayCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html) against GameObjects on layer 9, if you pass `9` into the Physics.Raycast call as the layerMask, Unity actually performs the ray cast against GameObjects on layers `3` and `0`. This is because the binary representation of 9 is `00001001` and if you interpret this as a mask, the `1`s are in the place of layers `3` and `0`. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
Layers and layerMasks
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html)
Set a layerMask
