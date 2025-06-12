* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateUVDistributionMetrics.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).RecalculateUVDistributionMetrics
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public void RecalculateUVDistributionMetrics(float uvAreaThreshold); 
### Parameters
Parameter | Description  
---|---  
uvAreaThreshold | The minimum UV area to consider. The default value is 1e-9f.  
### Description
Recalculates the UV distribution metrics of the Mesh from the vertices and uv coordinates.
The UV distribution metric can be used to calculate the desired mipmap level based on the position of the camera. It's important to call this function after procedurally generating meshes that have textures that use [Mip Map Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html).  
  
This function can also be used to update the UV distribution metric with an alternative uvAreaThreshold. The uvAreaThreshold can be used to ignore small UV areas from the UV distribution calculation; for example, you may wish to ignore a single texel colour used for a large triangle area. Unity will not consider the density of these areas when calculating mip selection, which may result in some colour tint due to lower mips being selected. The value depends on the texture resolution; for example, for a 256x256 texture, a single texel area would be (1/(256*256)).  
  
Additional resources: [Mip Map Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html) [GetUVDistributionMetric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVDistributionMetric.html), [RecalculateUVDistributionMetric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateUVDistributionMetric.html).
* * *
