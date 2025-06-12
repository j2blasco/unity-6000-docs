* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-create.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [3D textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html)
  * Create a 3D texture via script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-use-in-shader.html)
Sample a 3D texture in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
Rendering to a texture
# Create a 3D texture via script
Use the [`Texture3D`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) API to create a 3D texture via script.
For example:
```
// Set the texture parameters
int size = 32;
TextureFormat format = TextureFormat.RGBA32;
bool mipChain = false;

// Create a 3D texture with a width, height and depth of 32 pixels
Texture3D texture = new Texture3D(size, size, size, format, mipChain);

```

## Example
The following example creates an instance of the Texture3D class, populates it with color data, then saves it to your project as a serialized asset file.
```
using UnityEditor;
using UnityEngine;

public class ExampleEditorScript : MonoBehaviour
{
    [MenuItem("CreateExamples/3DTexture")]
    static void CreateTexture3D()
    {
        // Set the texture parameters
        int size = 32;
        TextureFormat format = TextureFormat.RGBA32;
        TextureWrapMode wrapMode =  TextureWrapMode.Clamp;

        // Create the texture and apply the parameters
        Texture3D texture = new Texture3D(size, size, size, format, false);
        texture.wrapMode = wrapMode;

        // Create a 3-dimensional array to store color data
        Color[] colors = new Color[size * size * size];

        // Populate the array so that the x, y, and z values of the texture map to red, blue, and green colors
        float inverseResolution = 1.0f / (size - 1.0f);
        for (int z = 0; z < size; z++)
        {
            int zOffset = z * size * size;
            for (int y = 0; y < size; y++)
            {
                int yOffset = y * size;
                for (int x = 0; x < size; x++)
                {
                    colors[x + yOffset + zOffset] = new Color(x * inverseResolution,
                        y * inverseResolution, z * inverseResolution, 1.0f);
                }
            }
        }

        // Copy the color values to the texture
        texture.SetPixels(colors);

        // Apply the changes to the texture and upload the updated texture to the GPU
        texture.Apply();        

        // Save the texture to your Unity Project
        AssetDatabase.CreateAsset(texture, "Assets/Example3DTexture.asset");
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-use-in-shader.html)
Sample a 3D texture in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
Rendering to a texture
