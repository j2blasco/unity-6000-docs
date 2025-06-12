* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-render-queue.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Set the render queue of a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package.html)
Set a shader to require a package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-pass.html)
Set when Unity runs a shader pass via a LightMode tag
# Set the render queue of a shader
The `Queue` tag tells Unity which render queue to use for geometry that it renders. The render queue is one of the factors that determines the order that Unity renders geometry in.
You can use the `Queue` tag in two ways: you can tell Unity to use a named render queue, or an unnamed render queue that it renders after a named render queue.
## Examples
This example code creates a SubShader that renders geometry as part of the Transparent render queue:
```
Shader "ExampleShader" {
    SubShader {
        Tags { "Queue" = "Transparent" }
        Pass {
            …
        }
    }
}

```

This example code creates a SubShader that renders geometry in an unnamed queue, after the Geometry queue.
```
Shader "ExampleShader" {
    SubShader {
        Tags { "Queue" = "Geometry+1" }
        Pass {
            …
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package.html)
Set a shader to require a package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-pass.html)
Set when Unity runs a shader pass via a LightMode tag
