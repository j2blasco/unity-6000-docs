* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
  * [Layers and layerMasks](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
  * Add a layer to a layerMask


[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html)
Set a layerMask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html)
Remove a layer from a layerMask
# Add a layer to a layerMask
To add a layer to a layermask, use the [logical OR operator](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators#logical-or-operator-) on the original layermask and the layer to add.
```
originalLayerMask |= (1 << layerToAdd);

```

## Additional resources
  * [Set a layermask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html)
  * [Remove a layer from a layermask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html)
Set a layerMask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html)
Remove a layer from a layerMask
