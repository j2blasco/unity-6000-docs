* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Adding material properties to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)
  * Set shader variables with material property values


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties-code.html)
Access material properties in a script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-display-types.html)
Control material properties in the Inspector window
# Set shader variables with material property values
## Using material properties to set variables in ShaderLab code
To set the value of a variable in your **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code from a material property, put the material property name in square brackets in your ShaderLab code. 
This example code demonstrates the syntax for using a material property to set the `units` value of the ShaderLab `Offset` command.
```
Shader "Examples/MaterialPropertyShaderLab"
{
    Properties
    {
        // Change this value in the Material Inspector to affect the value of the Offset command
        _OffsetUnitScale ("Offset unit scale", Integer) = 1
    }
    SubShader
    {
        // The code that defines the rest of the SubShader goes here

        Pass
        {
            Offset 0, [_OffsetUnitScale]

           // The code that defines the rest of the Pass goes here
        }
    }
}

```

## Using material properties to set variables in HLSL code
To set the value of a variable in HLSL code using a material property, give the material property the same name as the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) property.
You can see this technique in the following articles, which include working code examples:
  * [Writing vertex and fragment shaders for the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
  * [Writing custom shaders for the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-use-material-properties-code.html)
Access material properties in a script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-display-types.html)
Control material properties in the Inspector window
