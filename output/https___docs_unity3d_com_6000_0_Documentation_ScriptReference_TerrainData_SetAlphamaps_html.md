* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetAlphamaps.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetAlphamaps
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
public void SetAlphamaps(int x, int y, float[,,] map); 
### Description
Assign all splat values in the given map area.
The array supplied to this function determines the width and height of the portion to be replaced. The third dimension of the array corresponds to the number of splatmap textures. Note that the order of the array is [y,x,i].
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Terrain[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) t;
    // Blend the two terrain textures according to the steepness of
    // the slope at each point.
    void Start()
    {
        float[,,] map = new float[t.terrainData.alphamapWidth, t.terrainData.alphamapHeight, 2];  
  
        // For each point on the alphamap...
        for (int y = 0; y < t.terrainData.alphamapHeight; y++)
        {
            for (int x = 0; x < t.terrainData.alphamapWidth; x++)
            {
                // Get the normalized terrain coordinate that
                // corresponds to the point.
                float normX = x * 1.0f / (t.terrainData.alphamapWidth - 1);
                float normY = y * 1.0f / (t.terrainData.alphamapHeight - 1);  
  
                // Get the steepness value at the normalized coordinate.
                var angle = t.terrainData.GetSteepness(normX, normY);  
  
                // Steepness is given as an angle, 0..90 degrees. Divide
                // by 90 to get an alpha blending value in the range 0..1.
                var frac = angle / 90.0;  
  
                // Note the y and x are not in the traditional order.
                map[y, x, 0] = (float)frac;
                map[y, x, 1] = (float)(1 - frac);
            }
        }
        t.terrainData.SetAlphamaps(0, 0, map);
    }
}

```

* * *
