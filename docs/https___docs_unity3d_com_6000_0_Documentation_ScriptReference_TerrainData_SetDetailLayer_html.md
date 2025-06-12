* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetDetailLayer.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetDetailLayer
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
public void SetDetailLayer(int xBase, int yBase, int layer, int[,] details); 
### Description
Sets the detail layer density map.
The Terrain system uses detail layer density maps. Each map is essentially a grayscale image where each pixel value specifies the number of detail objects to procedurally place in the terrain area that corresponds to the pixel. These values depend on which [DetailScatterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DetailScatterMode.html) is set. Because several different detail types may be used, the map is arranged into "layers" - the array indices of the layers are determined by the order of the detail types defined in the Terrain inspector (ie, when the Paint Details tool is selected).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Set all pixels in a detail map below a certain threshold to zero.
    void DetailMapCutoff(Terrain[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) t, float threshold)
    {
        // Get all of layer zero.
        var map = t.terrainData.GetDetailLayer(0, 0, t.terrainData.detailWidth, t.terrainData.detailHeight, 0);  
  
        // For each pixel in the detail map...
        for (int y = 0; y < t.terrainData.detailHeight; y++)
        {
            for (int x = 0; x < t.terrainData.detailWidth; x++)
            {
                // If the pixel value is below the threshold then
                // set it to zero.
                if (map[x, y] < threshold)
                {
                    map[x, y] = 0;
                }
            }
        }  
  
        // Assign the modified map back.
        t.terrainData.SetDetailLayer(0, 0, 0, map);
    }
}

```

* * *
