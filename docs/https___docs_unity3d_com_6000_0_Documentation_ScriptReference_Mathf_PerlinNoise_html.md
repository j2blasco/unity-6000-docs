* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PerlinNoise.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).PerlinNoise
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static float PerlinNoise(float x, float y); 
### Parameters
Parameter | Description  
---|---  
x | X-coordinate of sample point.  
y | Y-coordinate of sample point.  
### Returns
**float** Value between 0.0 and 1.0. (Return value might be slightly below 0.0 or beyond 1.0.) 
### Description
Generate 2D Perlin noise.
Perlin noise is a pseudo-random pattern of float values generated across a 2D plane (although the technique does generalise to three or more dimensions, this is not implemented in Unity). The noise does not contain a completely random value at each point but rather consists of "waves" whose values gradually increase and decrease across the pattern. The noise can be used as the basis for texture effects but also for animation, generating terrain heightmaps and many other things.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PerlinExample.png)  
_Perlin noise sampled in the range 0..10 (the greyscale values represent values from 0..1)_  
  
Any point in the plane can be sampled by passing the appropriate X and Y coordinates. The same coordinates will always return the same sample value but the plane is essentially infinite so it is easy to avoid repetition by choosing a random area to sample from.
```
using UnityEngine;
using System.Collections;  
  
// Create a texture and fill it with Perlin noise.
// Try varying the xOrg, yOrg and scale values in the inspector
// while in Play mode to see the effect they have on the noise.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Width and height of the texture in pixels.
    public int pixWidth;
    public int pixHeight;  
  
    // The origin of the sampled area in the plane.
    public float xOrg;
    public float yOrg;  
  
    // The number of cycles of the basic noise pattern that are repeated
    // over the width and height of the texture.
    public float scale = 1.0F;  
  
    private Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) noiseTex;
    private Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] pix;
    private Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
        // Set up the texture and a Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) array to hold pixels during processing.
        noiseTex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(pixWidth, pixHeight);
        pix = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[noiseTex.width * noiseTex.height];
        rend.material.mainTexture = noiseTex;
    }  
  
    void CalcNoise()
    {
        // For each pixel in the texture...
        for (float y = 0.0F; y < noiseTex.height; y++)
        {
            for (float x = 0.0F; x < noiseTex.width; x++)
            {
                float xCoord = xOrg + x / noiseTex.width * scale;
                float yCoord = yOrg + y / noiseTex.height * scale;
                float sample = Mathf.PerlinNoise[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PerlinNoise.html)(xCoord, yCoord);
                pix[(int)y * noiseTex.width + (int)x] = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(sample, sample, sample);
            }
        }  
  
        // Copy the pixel data to the texture and load it into the GPU.
        noiseTex.SetPixels(pix);
        noiseTex.Apply();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        CalcNoise();
    }
}

```

**Note:** The return value can be slightly lower than 0.0f or slightly higher than 1.0f. If you need the range of return values to be between 0.0 and 1.0, clamp the return values.
* * *
