* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.SetEnvironmentData.html

#  [DynamicGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.html).SetEnvironmentData
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
## Declaration
public static void SetEnvironmentData(float[] input); 
### Parameters
Parameter | Description  
---|---  
input | Array of float values to be used for Enlighten Realtime Global Illumination environment lighting.  
### Description
Allows overriding the distant environment lighting for Enlighten Realtime Global Illumination, without changing the Skybox Material.
The input array represents a cube with each face being 8 x 8 texels and each texel being 4 floats (for the RGBA values of the texel's color), so the size of the array is 8*8*6*4 = 1536 floats.  
Note that changing the Distant Environment Lighting Source or Environment Lighting Intensity will overwrite the data set with this function.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set custom environment data for Enlighten Realtime Global Illumination.
        const int kCubeSize = 8 * 8;
        const int kEnvironmentDataSize = kCubeSize * 6 * 4;
        float[] envData = new float[kEnvironmentDataSize];  
  
        for (int c = 0; c < 6; ++c) // cube has 6 sides.
        {
            for (int i = 0; i < kCubeSize; i += 4)
            {
                int index = c * kCubeSize;  
  
                // Fill with default values.
                envData[index + i + 0] = 0.0f;
                envData[index + i + 1] = 0.0f;
                envData[index + i + 2] = 0.0f;
                envData[index + i + 3] = 1.0f;  
  
                // Funky colors on each cube face.
                envData[index + i + (c / 2)] = 4.0f * (float)i / (float)kCubeSize;
            }
        }  
  
        // Send the generated environment data to the GI system.
        DynamicGI.SetEnvironmentData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.SetEnvironmentData.html)(envData);
    }
}

```

* * *
