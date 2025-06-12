* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
  * [Layers and layerMasks](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
  * Remove a layer from a layerMask


[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html)
Add a layer to a layerMask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)
Tags
# Remove a layer from a layerMask
To remove a layer from a layermask, use the [logical AND operator](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators#logical-and-operator-) on the original layermask and the [bitwise complement](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators#bitwise-complement-operator-) of the layer to remove it.
```
originalLayerMask &= ~(1 << layerToRemove);

```

## Additional resources
  * [Set a layermask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html)
  * [Add a layer to a layermask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html)
Add a layer to a layerMask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)
Tags
