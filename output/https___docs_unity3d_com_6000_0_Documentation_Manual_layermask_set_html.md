* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-set.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
  * [Layers and layerMasks](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
  * Set a layerMask


[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-introduction.html)
Introduction to layerMasks
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html)
Add a layer to a layerMask
# Set a layerMask
This page explains how to set up a layerMask correctly so you can use it in API calls that use a serialized layerMask property.
## Use a serialized layerMask property
The simplest way to set a layermask in the Unity Editor is to create a property that uses Unity’s [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) class. If the property is `public` or uses the [SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html) attribute, Unity provides an interface in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) that you can use to select which layers the layermask represents.
```
using UnityEngine;

public class LayerMaskExample : MonoBehaviour
{
    [SerializeField] private LayerMask layermask;
}

```

## Convert from a layer
If you want to convert a layer to a layermask in a script at runtime, use the [binary left-shift operator](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators#left-shift-operator-) to left-shift `1` by the layer. The result is a layermask that represents the single layer.
```
using UnityEngine;

public class LayerExample : MonoBehaviour
{
    [SerializeField] private int layer = 10;
    private int layerAsLayerMask;

    private void Start()
    {
        layerAsLayerMask = (1 << layer);
    }
}

```

## Additional resources
  * [Add a layer to a layermask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html)
  * [Remove a layer from a layermask](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-introduction.html)
Introduction to layerMasks
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-add.html)
Add a layer to a layerMask
